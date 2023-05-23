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
    commentForm,
)

postBlueprint = Blueprint("post", __name__)

@postBlueprint.route("/post/<int:postID>", methods=["GET", "POST"])
def post(postID):
    form = commentForm(request.form)
    connection = sqlite3.connect("db/posts.db")
    cursor = connection.cursor()
    cursor.execute(f"select id from posts")
    posts = str(cursor.fetchall())
    if str(postID) in posts:
        message("2", f'POST: "{postID}" FOUND')
        connection = sqlite3.connect("db/posts.db")
        cursor = connection.cursor()
        cursor.execute(f'select * from posts where id = "{postID}"')
        post = cursor.fetchone()
        cursor.execute(f'update posts set views = views+1 where id = "{postID}"')
        connection.commit()
        if request.method == "POST":
            comment = request.form["comment"]
            connection = sqlite3.connect("db/comments.db")
            cursor = connection.cursor()
            cursor.execute(
                f"""
                insert into comments(post,comment,user,date,time)
                values({postID},"{comment}","{session["userName"]}",
                "{currentDate()}",
                "{currentTime()}")
                """
            )
            connection.commit()
            addPoints(5, session["userName"])
            flash("You earned 5 points by commenting ", "success")
            return redirect(f"/post/{postID}")
        connection = sqlite3.connect("db/comments.db")
        cursor = connection.cursor()
        cursor.execute(f'select * from comments where post = "{postID}"')
        comments = cursor.fetchall()
        return render_template(
            "post.html",
            id=post[0],
            tags=post[2],
            content=post[3],
            author=post[4],
            views=post[5],
            comments=comments,
            form=form,
        )
