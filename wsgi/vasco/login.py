from flask.ext.login import LoginManager
from flask.ext.babel import lazy_gettext
from flask_oauthlib.client import OAuth
from flask import abort, url_for, request
from . import app
from .config import config

loginManager = LoginManager(app)

loginManager.localize_callback = lazy_gettext

oauth = OAuth(app)

providers = {k: oauth.remote_app(k,
                                 consumer_key=config['providers'][k]['appId'],
                                 consumer_secret=
                                 config['providers'][k]['secret'],
                                 request_token_params=
                                 config['providers'][k]['request'],
                                 base_url=config['providers'][k]['url'],
                                 request_token_url=None,
                                 access_token_url=
                                 config['providers'][k]['token_url'],
                                 authorize_url=
                                 config['providers'][k]['authorize_url'])
             for k in config['providers']}


def authorized_handler(f):
    w = f
    for p in providers:
        provider = providers[p]
        w = provider.authorized_handler(w)
    return w


def tokengetter(f):
    w = f
    for p in providers:
        provider = providers[p]
        w = provider.tokengetter(w)
    return w


@loginManager.user_loader
def load_user(userid):
    pass


@app.route('/login/<providername>')
def login(providername):
    if not providername in providers:
        abort(404)
    #for rule in app.url_map.iter_rules():
        #print('%s => %s' % (url_for(rule.endpoint, provider='facebook'), rule.endpoint))
    provider = providers[providername]
    callback = url_for('authorized',
                       next=request.args.get('next') or request.referrer
                       or None,
                       _external=True,
                       provider=providername)
    return provider.authorize(callback=callback)


@app.route('/login/authorized/<provider>')
@authorized_handler
def authorized(resp, provider):
    print('dupa')
