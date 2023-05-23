from helpers import sqlite3, render_template, Blueprint, session, redirect

adminPanelUsersBlueprint = Blueprint("adminPanelUsers", __name__)


@adminPanelUsersBlueprint.route("/admin/users")
@adminPanelUsersBlueprint.route("/adminpanel/users")
def adminPanelUsers():
    return redirect('/login')
