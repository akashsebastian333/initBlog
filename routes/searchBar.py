from flask import redirect
from helpers import (
    render_template,
    Blueprint,
)

searchBarBlueprint = Blueprint("searchBar", __name__)


@searchBarBlueprint.route("/searchbar")
def searchBar():
    return redirect('/login')
