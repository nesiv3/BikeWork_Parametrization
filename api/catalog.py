from application.catalog.queries.catalog_data_query import GetCatalogDataByCatalogQuery, GetCatalogDataByCatalogQueryHandler
from fastapi import APIRouter, HTTPException
from infraestructure.unit_of_work import SqlAlchemyUnitOfWork
from application.catalog.queries.catalog_query import GetCatalogsQuery, GetCatalogsQueryHandler
from application.catalog.dto import CatalogDTO, CatalogDataDTO

router = APIRouter()

@router.get("/catalogs", response_model=list[CatalogDTO])
def get_catalogs():
    with SqlAlchemyUnitOfWork() as uow:
        handler = GetCatalogsQueryHandler(uow)
        return handler.handle(GetCatalogsQuery())


@router.get("/catalogs/data/{catalog_identity}", response_model=list[CatalogDataDTO])
def get_catalog_data_by_catalog(catalog_identity: str):
    with SqlAlchemyUnitOfWork() as uow:
        handler = GetCatalogDataByCatalogQueryHandler(uow)
        try:
            return handler.handle(GetCatalogDataByCatalogQuery(catalog_identity))
        except Exception as e:
            raise HTTPException(status_code=404, detail=str(e))