from flask.ext.login import LoginManager
from flask.ext.babel import lazy_gettext
from . import app

loginManager = LoginManager(app)

loginManager.localize_callback = lazy_gettext


@loginManager.user_loader
def load_user(userid):
    pass
