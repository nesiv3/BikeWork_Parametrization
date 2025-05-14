from infraestructure.database import SessionLocal
from infraestructure.repositories.catalog_repository import CatalogRepository
from infraestructure.repositories.disabled_date_repository import DisabledDateRepository

class IUnitOfWork:
    def __enter__(self): ...
    def __exit__(self, *args): ...
    def commit(self): ...
    @property
    def catalogs(self): ...

class SqlAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session = SessionLocal()
        self._catalogs = CatalogRepository(self.session)
        self._catalog_data = CatalogRepository(self.session)
        self._disabled_dates = DisabledDateRepository(self.session)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.commit()
        self.session.close()

    def commit(self):
        self.session.commit()

    @property
    def catalogs(self):
        return self._catalogs
    
    @property
    def catalog_data(self):
        return self._catalog_data
    
    @property
    def disabled_dates(self):
        return self._disabled_dates
