"""
This module initializes the Flask application and imports the routes.
It also sets up the secret key for the application from an environment variable.
"""

from os import getenv
from flask import Flask
from flask import send_file
import requests
from io import BytesIO


app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")


import routes


@app.errorhandler(404)
def page_not_found(e):
    response = requests.get("https://http.cat/images/404.jpg")
    return send_file(BytesIO(response.content), mimetype="image/jpeg")


@app.errorhandler(500)
def internal_server_error(e):
    return (
        """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="3">
        <title>Internal Server Error</title>
    </head>
    <body>
        <h1>500 Internal Server Error</h1>
        <p>This is likely due to the server being asleep. The page will refresh in 3 seconds and the server should wake up.</p>
    </body>
    </html>
    """,
        500,
    )
