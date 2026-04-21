from flask import Blueprint, render_template
from flask.typing import ResponseReturnValue
from HTTPCode import HTTPCode

blueprint: Blueprint = Blueprint(
    name="pages",
    import_name=__name__
)


@blueprint.route("/", methods=["GET"])
def index() -> ResponseReturnValue:
    return render_template("index.html"), HTTPCode.OK


@blueprint.route("/auth", methods=["GET"])
def auth() -> ResponseReturnValue:
    return render_template("auth.html"), HTTPCode.OK


@blueprint.route("/dev", methods=["GET"])
def dev() -> ResponseReturnValue:
    return render_template("dev.html"), HTTPCode.OK
