from helpers import (
    session,
    sqlite3,
    flash,
    message,
    redirect,
    render_template,
    Blueprint,
)

dashboardBlueprint = Blueprint("dashboard", __name__)


@dashboardBlueprint.route("/dashboard/<userName>")
def dashboard(userName):
    return redirect('/login')
