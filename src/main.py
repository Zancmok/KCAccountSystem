from flask import Flask
import config
import database.database
import routes.common
import routes.pages


def main() -> None:
    print(f"version: {config.VERSION}", flush=True)

    app: Flask = Flask(__name__)
    app.config["SECRET_KEY"] = config.FLASK_SECRET_KEY

    # Blueprints
    app.register_blueprint(routes.common.blueprint)
    app.register_blueprint(routes.pages.blueprint)

    database.database.initialize()
    app.run(
        port=config.PORT,
        host=config.HOST,
        debug=config.DEBUG
    )


if __name__ == '__main__':
    main()
