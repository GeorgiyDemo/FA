from flask import Flask, request
from pydantic import ValidationError

from models import User, AuthUser
from storage import Storage

app = Flask(__name__)
data_storage = Storage()


@app.route("/users/auth", methods=["POST"])
def user_authorization():
    """Авторизация пользователя"""
    try:
        auth_user = AuthUser.parse_obj(request.json)
        result = data_storage.user_auth(auth_user)
        if not result:
            return {"result": False}
        return {"result": True, "data": result.dict(exclude={"password", "email"})}
    except ValidationError as e:
        return e.json()


@app.route("/users/reg", methods=["POST"])
def user_registration():
    """Регистрация пользователя"""
    try:
        new_user = User.parse_obj(request.json)
        data_storage.user_reg(new_user)
    except ValidationError as e:
        return e.json()

    return new_user.dict(exclude={"password", "email", "api_key"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
