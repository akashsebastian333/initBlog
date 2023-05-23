from helpers import (
    sqlite3,
    render_template,
    Blueprint,
)
from flask import redirect, render_template_string

searchBlueprint = Blueprint("search", __name__)

@searchBlueprint.route("/search/<query>", methods=["GET", "POST"])
def search(query):
    return redirect('/login')