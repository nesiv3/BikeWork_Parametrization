from datetime import date, timedelta
from infraestructure.database import DisabledDateORM

class DisabledDateRepository:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(DisabledDateORM).all()

    def get_by_id(self, id: int):
        return self.session.query(DisabledDateORM).filter_by(id=id).first()

    def add(self, disabled_date: DisabledDateORM):
        self.session.add(disabled_date)
        self.session.flush()

    def get_next_15_days(self):
        today = date.today()
        end_date = today + timedelta(days=15)
        return (
            self.session.query(DisabledDateORM)
            .filter(DisabledDateORM.the_date >= today, DisabledDateORM.the_date <= end_date)
            .all()
        )