from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/Database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class contact_info(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("Name", db.String)
    email = db.Column("Email", db.String)
    message = db.Column("Message", db.String)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message


class user_info(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("Username", db.String)
    password = db.Column("Password", db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/learnmoreaboutme')
def moreAboutMe():
    return render_template("learnMoreAboutMe.html")


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        user = contact_info(name, email, message)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("thankyou", name=name, email=email, message=message))

    else:
        return render_template("contact.html")


@app.route('/contact/thankyou/<name>/<email>/<message>')
def thankyou(name, email, message):
    return render_template("thankyou.html", name=name, email=email, message=message)


@app.route('/project')
def project():
    return render_template("project.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/media')
def media():
    return render_template("media.html")


@app.route('/makeyourday')
def makeYourDay():
    return render_template("makeYourDay.html")


@app.route('/login', methods=["POST", "GET"])
def logIn():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        print(user_info.query.all())

        users = user_info.query.all()
        for user in users:
            print(user.username)

        #     if same name and same pw  create session sinon error message

        log_user = user_info(username, password)
        db.session.add(log_user)
        db.session.commit()

        if "username" in session:
            flash("You have been logged in!")
    return render_template("logUser.html")


@app.route('/view')
def view():
    return render_template("view.html", values=user_info.query.all())


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
