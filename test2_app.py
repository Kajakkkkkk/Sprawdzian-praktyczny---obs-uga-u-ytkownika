from main import create_user, app, delete_user
from main import users


def test_create_user() -> None:
    payload = {
        "firstName": "Jan",
        "lastName": "Kowal",
        "birthYear": 1999,
        "id": 1,
        "group": "user"
    }
    with app.test_request_context('/users', json=payload):
        create_user()
    assert payload in users


def test_delete_user() -> None:
    payload = {
        "id": 1,
        "firstName": "Jan",
        "lastName": "Kowal",
        "birthYear": 1999,
        "group": "user"
    }

    with app.test_request_context('/users/1', json=payload):
        delete_user(1)
    assert payload not in users
