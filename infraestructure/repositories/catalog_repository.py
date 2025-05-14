from infraestructure.database import CatalogDataORM, CatalogORM


class CatalogRepository:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(CatalogORM).all()

    def get_by_id(self, identity: str):
        return self.session.query(CatalogORM).filter_by(identity=identity).first()
    
    def get_data_by_catalog_identity(self, catalog_identity: str):
        return self.session.query(CatalogDataORM).filter_by(catalog_identity=catalog_identity).all()

