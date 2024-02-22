from main import app


def test_create_user():
    with app.test_client() as client:
        user_data = {
            "firstName": "Jan",
            "lastName": "Kowalski",
            "birthYear": 2000,
            "group": "user"
        }
        response = client.post('/users', json=user_data)
        assert response.status_code == 200


def test_get_users():
    with app.test_client() as client:
        response = client.get('/users')
        assert response.status_code == 200
        assert response.json == [
            {
                "id": 1,
                "firstName": "Jan",
                "lastName": "Kowalski",
                "birthYear": 2000,
                "group": "user"
            }
        ]


def test_delete_user():
    with app.test_client() as client:
        response = client.delete('/users/1')
        assert response.status_code == 200
