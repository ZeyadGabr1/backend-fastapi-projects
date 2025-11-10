from sqlalchemy.orm import Session
from routes.schemas import  OrderBase, OrderStatus
from db.models import DbUser, DbProducts, DbOrders
from fastapi import HTTPException, status
from db.db_oprations.exptions import Exptions

exption = Exptions()

class OrderManager:

    def get_my_orders(self, user: DbUser, db: Session):

        if not user:
            raise exption.login_required()
        
        user_orders = db.query(DbOrders).filter(DbOrders.user_id == user.id).all()

        if not user_orders:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="You Don't Have Any Orders")
        
        return user_orders
    
    def place_order(self, user: DbUser, request: OrderBase, db: Session):

        if not user:
            raise exption.login_required()
        
        product = db.query(DbProducts).filter(DbProducts.id == request.product_id).one_or_none()

        if not product:
                raise exption.product_not_found(request.product_id)
        
        if product.owner_id == user.id:
            raise exption.not_owner()
        
        
        elif request.capcity > product.stock:
             raise exption.quantity_insufficient()
        

        
        order = DbOrders(user_id=user.id,
                        product_id=product.id,
                        price=product.price,
                        capcity=request.capcity
                        )
        
        product.stock -= request.capcity

        db.add(order)
        db.commit()
        db.refresh(order)
        return order
    

    def update_order_status(self, order_id: int, user: DbUser, new_status: OrderStatus, db: Session):
         
         order = db.query(DbOrders).filter(DbOrders.id == order_id).one_or_none()

         if not order:
              raise exption.order_not_found(order_id)
         
         elif not user:
              raise exption.login_required()
         
         elif not user.is_admin:
              raise exption.not_admin()
         
         
         else:
              order.status = new_status
              db.commit()
              return {
                   "status": "Done",
                   "msg": "Order Updated Succsefuly"
              }
         
        
    def show_all_orders(self, user: DbUser, db: Session):
         
         orders = db.query(DbOrders).all()

         if not user:
                raise exption.login_required()
         
         elif not user.is_admin:
              raise exption.not_admin()
         
         elif not orders:
                raise exption.no_orders_found()
         
         else:
              return orders
         
     
    def search(self, user: DbUser, status: OrderStatus, db: Session,):

        if not user:
            raise exption.login_required()
        
        if not user.is_admin:
             raise exption.not_admin()
        
        all_orders = db.query(DbOrders).filter(DbOrders.status == status).all()

        if not all_orders:
            raise exption.no_orders_found()
        
        return all_orders 
              
