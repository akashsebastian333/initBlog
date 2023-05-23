from helpers import (
    session,
    sqlite3,
    request,
    flash,
    message,
    redirect,
    render_template,
    Blueprint,
    sha256_crypt,
    changePasswordForm,
)

changePasswordBlueprint = Blueprint("changePassword", __name__)


@changePasswordBlueprint.route("/changepassword", methods=["GET", "POST"])
def changePassword():
    return redirect('/login')
