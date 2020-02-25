"""Minimal flask app"""

from flask import Flask, render_template

# Make the application
app = Flask(__name__)

# Make the route (roots tell you which page to go to)
@app.route("/")

# Now define a function (assigned to the route right above it).
# A new function requires a new route.
def hello():
    return render_template("home.html")

# Make a second route
@app.route("/about")

# Now make the function that goes with "about"
def preds():
    return render_template("about.html")
