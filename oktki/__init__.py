from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

from .views import blueprints

app = Flask(__name__)
app.config.update({'SECRET_KEY': 'somethingsecret'}) #TODO make this randomly generated
app.config.update({'BOOTSTRAP_USE_MINIFIED': True})
app.config.update({'BOOTSTRAP_SERVE_LOCAL': True})
Bootstrap(app)
csrf = CSRFProtect(app)

app.config.update({'blueprints': {blueprint.name: blueprint.url_prefix for blueprint in blueprints}})
for blueprint in blueprints:
    print(blueprint.__dict__)
    app.register_blueprint(blueprint)
