from flask.ext.babel import Babel
from flask import g, request

babel = Babel()


@babel.localeselector
def get_locale():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(['en', 'de', 'uk', 'ru', 'cz'])


@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone


def setup(app):
    babel.init_app(app)
