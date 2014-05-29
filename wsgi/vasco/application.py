from flask import Flask, render_template, request, url_for
from .config import config

app = Flask(__name__)
app.debug = True
app.secret_key = config['secret_key']
app.config['SERVER_NAME'] = config['server_name']


@app.errorhandler(404)
def not_found(error):
    #for rule in app.url_map.iter_rules():
        #print('%s => %s' % (url_for(rule.endpoint), rule.endpoint))
    print('%s' % request.headers)
    return 'Not Found: %s %s' % (request.path, error), 404


@app.route('/')
def index():
    return render_template('index.html', title='Plan your journey! - Vasco')
