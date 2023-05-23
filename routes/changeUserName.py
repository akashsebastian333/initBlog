from helpers import (
    session,
    sqlite3,
    request,
    flash,
    message,
    redirect,
    render_template,
    Blueprint,
    changeUserNameForm,
)

changeUserNameBlueprint = Blueprint("changeUserName", __name__)


@changeUserNameBlueprint.route("/changeusername", methods=["GET", "POST"])
def changeUserName():
    return redirect('/login')
