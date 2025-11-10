from sqlalchemy.orm import Session
from sqlalchemy import and_
from routes.schemas import ProductBase
from db.models import DbUser, DbProducts, DbOrders
from db.db_oprations.exptions import Exptions


exption = Exptions()

class ProductManage:

    def show_all_products(self, user: DbUser, db: Session):

        if not user:
            raise exption.login_required()

        all_products = db.query(DbProducts).filter(DbProducts.owner_id != user.id).filter(DbProducts.stock > 0).all()

        if not all_products:
            raise exption.no_products_found()
        
        return all_products
    
    def add_product(self, user: DbUser, request: ProductBase, db: Session):

        if not user:
            raise exption.login_required()
        
        product = DbProducts(
            name=request.name,
            description=request.description,
            price=request.price,
            stock=request.stock,
            owner_id=user.id
        )

        db.add(product)
        db.commit()
        db.refresh(product)
        return product


    def delete_product(self, user: DbUser, product_id, db: Session):

        if not user:
            raise exption.login_required()
        
        product = db.query(DbProducts).filter(DbProducts.id == product_id).one_or_none()
        all_orders = db.query(DbOrders).filter(DbOrders.product_id == product_id).all()

        if not product:
            raise exption.product_not_found(product_id)
        
        elif product.owner_id != user.id and user.is_admin == False:
            raise exption.not_owner()
        
        
        elif all_orders:
            for order in all_orders:
                db.delete(order)


        db.delete(product)
        db.commit()
        return {'status': 'Succsefuly',
            'msg': 'Product Removed Done'
            }


    def edit_product(self, user: DbUser, product_id: int, request: ProductBase, db: Session):

        if not user.is_admin:
            raise exption.not_admin()
        
        product = db.query(DbProducts).filter(DbProducts.id == product_id).one_or_none()

        if not product:
            raise exption.product_not_found(product_id)
        
        product.name = request.name
        product.description = request.description
        product.price = request.price
        product.stock = request.stock

        db.commit()
        return {
            "msg": "Product Updated Done"
        }


    def search(self, user: DbUser, price: int, stock: int, db: Session):

        if not user:
            raise exption.login_required()
        
        all_products = db.query(DbProducts).filter(and_(DbProducts.price >= price,
                                                        DbProducts.stock >= stock),
                                                        DbProducts.owner_id != user.id).all()

        if not all_products:
            raise exption.no_products_found()
        
        return all_products