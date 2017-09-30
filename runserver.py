"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from project import create_app

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8081'))
    except ValueError:
        PORT = 8081

    app = create_app()
    app.run(HOST, PORT)
