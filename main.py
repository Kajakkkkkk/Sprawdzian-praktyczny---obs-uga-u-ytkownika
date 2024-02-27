from flask import Flask, Response, jsonify, request
from user_service import UserService, users

app = Flask(__name__)


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
        return Response(status=200)
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
        return Response(status=200)
    else:
        return Response(status=404)


if __name__ == "__main__":
    app.run()
