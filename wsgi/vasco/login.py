from flask.ext.login import LoginManager
from flask.ext.babel import lazy_gettext

loginManager = LoginManager()

loginManager.localize_callback = lazy_gettext


@loginManager.user_loader
def load_user(userid):
    pass


def setup(app):
    login_manager.init_app(app)
