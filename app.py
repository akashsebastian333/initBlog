import socket

from helpers import (
    secrets,
    message,
    render_template,
    getProfilePicture,
    Flask,
)

from routes.post import postBlueprint
from routes.user import userBlueprint
from routes.index import indexBlueprint
from routes.login import loginBlueprint
from routes.signup import signUpBlueprint
from routes.logout import logoutBlueprint
from routes.search import searchBlueprint
from routes.searchBar import searchBarBlueprint
from routes.editPost import editPostBlueprint
from routes.dashboard import dashboardBlueprint
from routes.adminPanel import adminPanelBlueprint
from routes.deleteUser import deleteUserBlueprint
from routes.deletePost import deletePostBlueprint
from routes.createPost import createPostBlueprint
from routes.setUserRole import setUserRoleBlueprint
from routes.deleteComment import deleteCommentBlueprint
from routes.changeUserName import changeUserNameBlueprint
from routes.changePassword import changePasswordBlueprint
from routes.adminPanelUsers import adminPanelUsersBlueprint
from routes.adminPanelPosts import adminPanelPostsBlueprint
from routes.accountSettings import accountSettingsBlueprint
from routes.adminPanelComments import adminPanelCommentsBlueprint
from dbChecker import dbFolder, usersTable, postsTable, commentsTable


dbFolder()
usersTable()
postsTable()
commentsTable()



app = Flask(__name__)


@app.context_processor
def utility_processor():
    getProfilePicture
    return dict(getProfilePicture=getProfilePicture)


@app.errorhandler(404)
def notFound(e):
    message("1", "404")
    return render_template("404.html"), 404


app.register_blueprint(postBlueprint)
app.register_blueprint(userBlueprint)
app.register_blueprint(indexBlueprint)
app.register_blueprint(loginBlueprint)
app.register_blueprint(signUpBlueprint)
app.register_blueprint(logoutBlueprint)
app.register_blueprint(searchBlueprint)
app.register_blueprint(editPostBlueprint)
app.register_blueprint(dashboardBlueprint)
app.register_blueprint(searchBarBlueprint)
app.register_blueprint(adminPanelBlueprint)
app.register_blueprint(deleteUserBlueprint)
app.register_blueprint(deletePostBlueprint)
app.register_blueprint(createPostBlueprint)
app.register_blueprint(setUserRoleBlueprint)
app.register_blueprint(deleteCommentBlueprint)
app.register_blueprint(changeUserNameBlueprint)
app.register_blueprint(changePasswordBlueprint)
app.register_blueprint(adminPanelUsersBlueprint)
app.register_blueprint(adminPanelPostsBlueprint)
app.register_blueprint(accountSettingsBlueprint)
app.register_blueprint(adminPanelCommentsBlueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

