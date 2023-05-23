from helpers import sqlite3, render_template, Blueprint, session, redirect

adminPanelCommentsBlueprint = Blueprint("adminPanelComments", __name__)


@adminPanelCommentsBlueprint.route("/admin/comments")
@adminPanelCommentsBlueprint.route("/adminpanel/comments")
def adminPanelComments():
    return redirect('/login')
