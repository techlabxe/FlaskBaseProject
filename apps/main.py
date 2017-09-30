from flask import Flask, Blueprint

app = Blueprint( 'main', __name__, url_prefix = '/' )

@app.route('/')
def index():
    return 'Hello Flask Base application'

