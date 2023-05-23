from helpers import (
    session,
    sqlite3,
    request,
    flash,
    message,
    redirect,
    addPoints,
    currentDate,
    currentTime,
    render_template,
    Blueprint,
    createPostForm,
)

createPostBlueprint = Blueprint("createPost", __name__)


@createPostBlueprint.route("/createpost", methods=["GET", "POST"])
def createPost():
    return redirect('/login')
