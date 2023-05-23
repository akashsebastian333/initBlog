from helpers import (
    session,
    sqlite3,
    request,
    flash,
    message,
    redirect,
    currentDate,
    currentTime,
    render_template,
    Blueprint,
    createPostForm,
)

editPostBlueprint = Blueprint("editPost", __name__)


@editPostBlueprint.route("/editpost/<int:postID>", methods=["GET", "POST"])
def editPost(postID):
    return redirect('/login')
