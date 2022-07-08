from pprint import pprint  # pylint: disable=unused-import

import pytest

from libs import db
from apps import app
from apps.app_employee import schemas as employee_sch, services as employee_svc, models as employee_models


@pytest.fixture(name="admin1")
def fixture_admin1() -> employee_sch.PostEmployee:
    employee_data = employee_sch.PostEmployee(password="admin1234")
    employee_data.name      = "admin1"
    employee_data.username  = "adminsatu"
    employee_data.gender    = "Laki-laki"
    employee_data.birthdate = "1998-03-26"
    # employee_data.password  = "admin1234"
    return employee_data


# @pytest.fixture(name="reset_table")
@pytest.fixture(name="reset_table", scope="session")
def fixture_reset_table():
    employee_data = employee_sch.PostEmployee(password="admin1234")
    employee_data.name      = "admin1"
    employee_data.username  = "adminsatu"
    employee_data.gender    = "Laki-laki"
    employee_data.birthdate = "1998-03-26"

    db.Base.metadata.drop_all(bind=db.engine)
    db.Base.metadata.create_all(bind=db.engine)
    with db.session() as db_:
        employee_service = employee_svc.EmployeeServices(db_)
        employee_service.create(employee_data)

    yield

@pytest.fixture(name="admin1_token")
def fixture_admin1_token(admin1, reset_table):
    with app.app_context():
        with db.session() as db_:

            employee_service = employee_svc.EmployeeServices(db_)
            response = employee_service.login(admin1)

    return response.access_token
