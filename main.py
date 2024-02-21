from flask import Flask, Response, jsonify, request

app = Flask(__name__)
users = []
user_id_counter = 1


class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        for user in users:
            if user['id'] == user_id:
                return user
        return None

    @staticmethod
    def validate_user_data(user_data):
        valid_groups = ["user", "premium", "admin"]
        if not all(key in user_data for key in ['firstName', 'lastName', 'birthYear', 'group']):
            return False
        if not isinstance(user_data['birthYear'], int) or user_data['birthYear'] <= 0:
            return False
        if user_data['group'] not in valid_groups:
            return False
        return True

    @staticmethod
    def create_user(user_data):
        global user_id_counter
        if UserService.validate_user_data(user_data):
            user_data['id'] = user_id_counter
            users.append(user_data)
            user_id_counter += 1
            return user_data['id']
        return None

    @staticmethod
    def update_user(user_id, user_data):
        if UserService.get_user_by_id(user_id):
            if UserService.validate_user_data(user_data):
                for user in users:
                    if user['id'] == user_id:
                        user.update(user_data)
                        return True
        return False

    @staticmethod
    def delete_user(user_id):
        for user in users:
            if user['id'] == user_id:
                users.remove(user)
                return True
        return False


@app.get("/users")
def get_users() -> Response:
    return jsonify(users)


@app.get("/users/<int:user_id>")
def get_user(user_id: int) -> Response:
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    else:
        return Response(status=404)


@app.post("/users")
def create_user() -> Response:
    user_data = request.json
    user_id = UserService.create_user(user_data)
    if user_id:
        return Response(status=201)
    else:
        return Response(status=400)


@app.patch("/users/<int:user_id>")
def update_user(user_id: int) -> Response:
    user_data = request.json
    if UserService.update_user(user_id, user_data):
        return Response(status=200)
    else:
        return Response(status=404)


@app.delete("/users/<int:user_id>")
def delete_user(user_id: int) -> Response:
    if UserService.delete_user(user_id):
        return Response(status=204)
    else:
        return Response(status=404)


if __name__ == "__main__":
    app.run()
