from helpers import sqlite3, render_template, Blueprint, session, redirect

adminPanelPostsBlueprint = Blueprint("adminPanelPosts", __name__)


@adminPanelPostsBlueprint.route("/admin/posts")
@adminPanelPostsBlueprint.route("/adminpanel/posts")
def adminPanelPosts():
    return redirect('/login')
