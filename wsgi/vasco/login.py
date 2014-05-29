from flask.ext.login import LoginManager
from flask.ext.babel import lazy_gettext
from flask_oauthlib.client import OAuth, OAuthException
from flask import abort, url_for, request, session
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
    for p in providers:
        provider = providers[p]
        provider.tokengetter(lambda: f(provider.name))
    return f


@loginManager.user_loader
def load_user(userid):
    pass


@app.route('/login/<providername>')
def login(providername):
    if not providername in providers:
        abort(404)
    #for rule in app.url_map.iter_rules():
        #print('%s => %s' %
              #(url_for(rule.endpoint, provider='facebook'),
               #rule.endpoint))
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
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    if isinstance(resp, OAuthException):
        return 'Access denied: %s' % resp.message

    session['%s_oauth_token' % provider] = (resp['access_token'], '')
    me = providers[provider].get('/me')
    return 'Logged in as id=%s name=%s redirect=%s' % \
        (me.data['id'], me.data['name'], request.args.get('next'))


@tokengetter
def get_oauth_token(provider):
    return session.get('%s_oauth_token' % provider)
