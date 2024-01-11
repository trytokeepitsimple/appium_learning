import pytest
from utilities.generate_logs import log_creation
def get_data():
    return [
        ["deveshone@mail.com"],
        ["deveshtwo@mail.com"],
        ["deveshthree@mail.com"],
        ["deveshfour@mail.com"]
    ]


@pytest.mark.parametrize("email",get_data())
def test_mail_fetch(email):
    print(email)
    log_create = log_creation()
    log_create.info("kjvhedhawvd")