# Check if user is logged in: if so, show secret page.
# https://realpython.com/primer-on-python-decorators/#is-the-user-logged-in

# Using Flask to set up a /secret web page that should only be visible to users that are logged in or
# otherwise authenticated

from flask import Flask, g, request, redirect, url_for
import functools

app = Flask(__name__)


def login_required(function):
    # Make sure the user is logged in before proceeding
    @functools.wraps(function)
    def wrapper_login_required(*args, **kwargs):
        # flask.g -> A namespace object that can store data during an application context.
        # https://flask.palletsprojects.com/en/2.0.x/api/#flask.g
        if g.user is None:
            # flask.redirect(location, code=302, Response=None)
            # Returns a response object (a WSGI application) that, if called, redirects the client to the target
            # location.
            # https://flask.palletsprojects.com/en/2.0.x/api/#flask.redirect

            # flask.url_for(endpoint, **values) -> Generates a URL to the given endpoint with the method provided.
            # https://flask.palletsprojects.com/en/2.0.x/api/#flask.url_for
            return redirect(url_for('login', next=request.url))
        return function(*args, **kwargs)

    return wrapper_login_required


@app.route("/secret")
@login_required
def secret():
    """
    some code here
    :return:
    """
