from flask import Blueprint, jsonify
from flask.typing import ResponseReturnValue
from datetime import datetime, timezone
from HTTPCode import HTTPCode
import config

blueprint: Blueprint = Blueprint(
    name="common",
    import_name=__name__
)


@blueprint.route("/ping", methods=["GET"])
def ping() -> ResponseReturnValue:
    return jsonify({
        "status": "ok"
    }), HTTPCode.OK


@blueprint.route("/health", methods=["GET"])
def health() -> ResponseReturnValue:
    return jsonify({
        "status": "ok",
        "service": "kc-account-system",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "app_version": config.VERSION
    }), HTTPCode.OK
