import os
from flask import Flask, render_template
from webapp.glossary_routes import glossary_bp

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    template_dir = os.path.join(base_dir, "webapp", "templates")
    static_dir = os.path.join(base_dir, "webapp", "static")

    app = Flask(
        __name__,
        static_folder=static_dir,
        template_folder=template_dir,
        static_url_path="/static"
    )

    app.register_blueprint(glossary_bp, url_prefix="/glossary")

    @app.route("/")
    def index():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    app = create_app()
    print("Template folder:", app.template_folder)  # sanity check
    app.run(debug=True)
