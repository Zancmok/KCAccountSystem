from flask import Blueprint, jsonify
from flask.typing import ResponseReturnValue
from datetime import datetime, timezone
import config

blueprint: Blueprint = Blueprint(
    name="common",
    import_name=__name__
)


@blueprint.route("/ping", methods=["GET"])
def ping() -> ResponseReturnValue:
    return jsonify({
        "status": "ok"
    }), 200


@blueprint.route("/health", methods=["GET"])
def health() -> ResponseReturnValue:
    return jsonify({
        "status": "ok",
        "service": "kc-account-system",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "app_version": config.VERSION
    }), 200


__all__ = ["blueprint"]
