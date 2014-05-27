#!/usr/bin/env python3
from flask import Flask, render_template
from vasco import localization

app = Flask(__name__)

app.debug = True

localization.setup(app)


@app.route('/')
def index():
    return render_template('index.html', title='Plan your journey! - Vasco')
