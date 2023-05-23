from helpers import (
    session,
    redirect,
    render_template,
    Blueprint,
)

accountSettingsBlueprint = Blueprint("accountSettings", __name__)


@accountSettingsBlueprint.route("/accountsettings")
def accountSettings():
    return redirect('/login')
