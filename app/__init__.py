from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.main_routes import main_bp
    from app.routes.search_routes import search_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(search_bp)

    return app
