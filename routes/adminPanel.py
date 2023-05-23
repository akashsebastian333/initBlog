from helpers import sqlite3, render_template, Blueprint, session, redirect

adminPanelBlueprint = Blueprint("adminPanel", __name__)


@adminPanelBlueprint.route("/admin")
def adminPanel():
    return redirect('/login')
