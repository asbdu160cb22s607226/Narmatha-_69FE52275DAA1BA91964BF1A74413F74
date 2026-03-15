from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from .routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.get("/health")
    def health() -> dict:
        return {"status": "ok"}

    return app
