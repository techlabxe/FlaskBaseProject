from flask import Flask, Blueprint

app = Blueprint( 'api', __name__, url_prefix = '/api' )

@app.route('/')
def index():
    return 'WebAPIindex'

