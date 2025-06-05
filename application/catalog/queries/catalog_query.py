from infraestructure.unit_of_work import IUnitOfWork
from application.catalog.dto import CatalogDTO
from utils.exceptions import NotFoundException

class GetCatalogsQuery:
    pass

class GetCatalogsQueryHandler:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def handle(self, query: GetCatalogsQuery):
        catalogs = self.uow.catalogs.get_all()
        if not catalogs:
             raise NotFoundException("Catalogs")
        return [CatalogDTO.from_orm(catalog) for catalog in catalogs]