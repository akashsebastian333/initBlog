from helpers import (
    session,
    secrets,
    sqlite3,
    request,
    flash,
    message,
    redirect,
    currentDate,
    currentTime,
    render_template,
    Blueprint,
    signUpForm,
    sha256_crypt,
)

signUpBlueprint = Blueprint("signup", __name__)


@signUpBlueprint.route("/signup", methods=["GET", "POST"])
def signup():
    return redirect('/login')
