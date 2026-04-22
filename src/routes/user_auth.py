from typing import Any
import re
from re import Pattern
from errors import UserAlreadyExistsError, InvalidCretentialsError
import services.auth_service as auth_service
from services.AccessToken import AccessToken
from flask import Blueprint, jsonify, request, redirect
from flask.typing import ResponseReturnValue
from HTTPCode import HTTPCode

blueprint: Blueprint = Blueprint(
    name="user_auth",
    import_name=__name__,
    url_prefix="/user_auth"
)

username_regex: Pattern[str] = re.compile(r'^[a-z0-9][a-z0-9_-]{1,30}[a-z0-9]$')
password_regex: Pattern[str] = re.compile(r'^.{6,64}$')


@blueprint.route("/signup", methods=["POST"])
def signup() -> ResponseReturnValue:
    if not isinstance(json_data := request.get_json(silent=True), dict):
        return jsonify({
            "success": False,
            "reason": "'json_data' not provided!"
        }), HTTPCode.BAD_REQUEST
    json_data: dict[str, Any]

    if not ((username := json_data.get("username")) and isinstance(username, str)):
        return jsonify({
            "success": False,
            "reason": "'username' in 'json_data' must be of type string!"
        }), HTTPCode.BAD_REQUEST
    username: str

    if not ((password := json_data.get("password")) and isinstance(password, str)):
        return jsonify({
            "success": False,
            "reason": "'password' in 'json_data' must be of type string!"
        }), HTTPCode.BAD_REQUEST
    password: str

    if not username_regex.fullmatch(username):
        return jsonify({
            "success": False,
            "reason": "Username does not follow the naming convention!"
        }), HTTPCode.BAD_REQUEST

    if not password_regex.fullmatch(password):
        return jsonify({
            "success": False,
            "reason": "Password does not follow the naming convention!"
        }), HTTPCode.BAD_REQUEST

    try:
        auth_service.create_user(
            username=username,
            password=password
        )
    except UserAlreadyExistsError:
        return jsonify({
            "success": False,
            "reason": "A user with this username already exists!"
        }), HTTPCode.CONFLICT

    return jsonify({
        "success": True,
    }), HTTPCode.CREATED


@blueprint.route("/login", methods=["POST"])
def login() -> ResponseReturnValue:
    if not isinstance(json_data := request.get_json(silent=True), dict):
        return jsonify({
            "success": False,
            "reason": "'json_data' not provided!"
        }), HTTPCode.BAD_REQUEST
    json_data: dict[str, Any]

    if not ((username := json_data.get("username")) and isinstance(username, str)):
        return jsonify({
            "success": False,
            "reason": "'username' in 'json_data' must be of type string!"
        }), HTTPCode.BAD_REQUEST
    username: str

    if not ((password := json_data.get("password")) and isinstance(password, str)):
        return jsonify({
            "success": False,
            "reason": "'password' in 'json_data' must be of type string!"
        }), HTTPCode.BAD_REQUEST
    password: str

    try:
        access_token: AccessToken = auth_service.try_login(
            username=username,
            password=password
        )
    except InvalidCretentialsError as e:
        return jsonify({
            "success": False,
            "reason": str(e)
        })
    
    return jsonify({
        "success": True,
        "access_token": access_token.code
    })
