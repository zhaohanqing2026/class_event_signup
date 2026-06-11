from flask import Flask, redirect, render_template, request, url_for

from data.event_info import EVENT_DESCRIPTION, EVENT_NAME, EVENT_NOTICE
from data.options import ACTIVITY_OPTIONS, GROUP_OPTIONS
from data.page_text import FORM_TIPS, RESULT_TITLE, WELCOME_TEXT
from data.registrations import REGISTRATIONS

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        event_name=EVENT_NAME,
        event_description=EVENT_DESCRIPTION,
        event_notice=EVENT_NOTICE,
        welcome_text=WELCOME_TEXT,
        form_tips=FORM_TIPS,
        group_options=GROUP_OPTIONS,
        activity_options=ACTIVITY_OPTIONS,
        registrations=REGISTRATIONS,
        total=len(REGISTRATIONS),
    )


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form.get("name", "").strip()
    group = request.form.get("group", "").strip()
    activity = request.form.get("activity", "").strip()
    reason = request.form.get("reason", "").strip() or "想参与本次班级活动。"

    return redirect(
        url_for(
            "result",
            name=name,
            group=group,
            activity=activity,
            reason=reason,
        )
    )


@app.route("/result", methods=["GET"])
def result():
    registrations = list(REGISTRATIONS)
    name = request.args.get("name", "").strip()
    group = request.args.get("group", "").strip()
    activity = request.args.get("activity", "").strip()
    reason = request.args.get("reason", "").strip()

    if name and group and activity:
        registrations.append(
            {
                "name": name,
                "group": group,
                "activity": activity,
                "reason": reason or "想参与本次班级活动。",
            }
        )

    stats = {activity_name: 0 for activity_name in ACTIVITY_OPTIONS}
    for item in registrations:
        stats[item["activity"]] = stats.get(item["activity"], 0) + 1

    return render_template(
        "result.html",
        event_name=EVENT_NAME,
        result_title=RESULT_TITLE,
        registrations=registrations,
        total=len(registrations),
        stats=stats,
    )


if __name__ == "__main__":
    app.run(debug=True)
