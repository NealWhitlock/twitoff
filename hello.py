"""Minimal flask app"""

from flask import Flask

# Make the application
app = Flask(__name__)

# Make the route
@app.route("/")

# Now define a function (assigned to the route right above it).
# A new function requires a new route.
def hello():
    return "Hello World!"
