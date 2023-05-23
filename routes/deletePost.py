from helpers import (
    session,
    sqlite3,
    message,
    redirect,
    Blueprint,
)

deletePostBlueprint = Blueprint("deletePost", __name__)


@deletePostBlueprint.route("/deletepost/<int:postID>/redirect=<direct>")
def deletePost(postID, direct):
    direct = direct.replace("&", "/")
    if "userName" in session:
        connection = sqlite3.connect("db/posts.db")
        cursor = connection.cursor()
        cursor.execute(f"select author from posts where id = {postID}")
        author = cursor.fetchone()
        if author[0] == session["userName"]:
            cursor.execute(f"delete from posts where id = {postID}")
            cursor.execute(f"update sqlite_sequence set seq = seq-1")
            connection.commit()
            message("2", f'POST: "{postID}" DELETED')
            return redirect(f"/")
        else:
            message(
                "1",
                f'POST: "{postID}" NOT DELETED "{postID}" DOES NOT BELONG TO USER: {session["userName"]}',
            )
            return redirect(f"/")
        return redirect(f"/{direct}")
    else:
        message("1", f'USER NEEDS TO LOGIN FOR DELETE POST: "{postID}"')
        return redirect(f"/login/redirect=&post&{postID}")
