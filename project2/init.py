from hyper.ma import ma
from hyper.db import db
from flask import Flask
def create_app():

    app = Flask(__name__)

    # Config
    ...

    # Initialize DB and Marshmallow
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():

        # Import Models
        import models

        # Import MethodViews
        ...

        # Import Blueprints
        ...

        # Commands

        return app