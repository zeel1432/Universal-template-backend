class CRUDBase(Generic[ModelType]):
    def get_all(self, db: Session):
        return db.query(self.model).all()


class ProductService(CRUDBase[Product]):
    pass
