from application.catalog.queries.catalog_data_query import GetCatalogDataByCatalogQuery, GetCatalogDataByCatalogQueryHandler
from application.disabled_dates.dto import DisabledDateDTO
from application.disabled_dates.queries.disabled_date_query import GetDisabledDatesQuery, GetDisabledDatesQueryHandler
from fastapi import APIRouter, HTTPException
from infraestructure.unit_of_work import SqlAlchemyUnitOfWork
from utils.cache import redis_cache


router = APIRouter()




@router.get("/disabled_dates", response_model=list[DisabledDateDTO])
@redis_cache("disabled_dates", expire=2592000)
def get_disabled_dates():
    with SqlAlchemyUnitOfWork() as uow:
        handler = GetDisabledDatesQueryHandler(uow)
        return handler.handle(GetDisabledDatesQuery())
