from flask import Flask, render_template
from database.database import AlertDatabase


app = Flask(__name__)


@app.route("/")
def dashboard():

    database = AlertDatabase()

    alerts = database.get_alerts()

    return render_template(
        "dashboard.html",
        alerts=alerts
    )


if __name__ == "__main__":
    app.run(debug=True)