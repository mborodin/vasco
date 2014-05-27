from flask.ext.babel import Babel
from flask import g, request
from . import app

babel = Babel(app)


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
