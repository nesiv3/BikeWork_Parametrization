from infraestructure.unit_of_work import IUnitOfWork
from application.catalog.dto import CatalogDataDTO
from utils.exceptions import NotFoundException

class GetCatalogDataByCatalogQuery:
    def __init__(self, catalog_identity: str):
        self.catalog_identity = catalog_identity

class GetCatalogDataByCatalogQueryHandler:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def handle(self, query: GetCatalogDataByCatalogQuery):
        catalog_data = self.uow.catalog_data.get_data_by_catalog_identity(query.catalog_identity)
        if not catalog_data:
            raise NotFoundException(f"CatalogData for catalog {query.catalog_identity}")
        return [CatalogDataDTO.from_orm(data) for data in catalog_data]