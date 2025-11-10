from fastapi import HTTPException, status




class Exptions:

    def login_required(self):
        exption = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Unauthorized, Please Login In")
        return exption
    
    def product_not_found(self, id):
        exption = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Product With Id {id} Not Found, Please Check It Again!")
        
        return exption
    
    def order_not_found(self, id):
        exption = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Order With Id {id} Not Found, Please Check It Again!")
        return exption
    
    def no_products_found(self):
        exption = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="There are no products available at the moment. Come back later.")
        return exption
    
    def no_orders_found(self):
        exption = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="There are no Orders available at the moment. Come back later.")
        return exption    
        
    def not_owner(self):
        exption = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="You Are Not The Owner!")
        return exption
    
    def not_admin(self):
        exption = HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="Admin Account Is Required")
        return exption
    
    def quantity_insufficient(self):
        exption = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="The quantity is insufficient")
        return exption
    
    def email_exists(self):
        exption = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="The email already exists")
        return exption
    
    def wrong_password(self):
        exption = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="Wrong Password, Try It Again!")
        
        return exption
    