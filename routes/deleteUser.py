from helpers import (
    session,
    sqlite3,
    message,
    redirect,
    Blueprint,
)

deleteUserBlueprint = Blueprint("deleteUser", __name__)


@deleteUserBlueprint.route("/deleteuser/<userName>/redirect=<direct>")
def deleteUser(userName, direct):
    return redirect('/login')
