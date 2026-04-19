from flask import Flask
import config
import database.database
import routes.common


def main() -> None:
    app: Flask = Flask(__name__)

    app.config["SECRET_KEY"] = config.FLASK_SECRET_KEY

    app.register_blueprint(routes.common.blueprint)

    database.database.initialize()

    app.run(
        port=config.PORT,
        host=config.HOST,
        debug=config.DEBUG
    )


if __name__ == '__main__':
    main()
