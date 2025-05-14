from infraestructure.unit_of_work import IUnitOfWork
from application.disabled_dates.dto import DisabledDateDTO
from utils.exceptions import NotFoundException

class GetDisabledDatesQuery:
    pass

class GetDisabledDatesQueryHandler:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    def handle(self, query: GetDisabledDatesQuery):
        dates = self.uow.disabled_dates.get_all()
        if not dates:
            raise NotFoundException("DisabledDates")
        return [DisabledDateDTO.from_orm(date) for date in dates]