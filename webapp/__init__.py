from flask import Flask
from webapp.routes import views
from webapp.glossary_routes import glossary_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(views)
    app.register_blueprint(glossary_bp)
    return app
