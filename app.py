from flask import *
import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", username = session.get("username"))

# User Registration
@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Whether there is the same user name
        if db.get_user_by_name(username) is None:
            db.add_user(username, password)
            session["username"] = username
            return render_template("index.html", username = session["username"])
    return render_template("create.html")

app.secret_key = 'TGK3QRDN738YPTGDDSHB'

if __name__ == "__main__":
    app.run(debug=True)
