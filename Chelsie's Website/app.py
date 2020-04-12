from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Q5Y5tM4G8vDHav7z"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/Database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('Sign In')


class ContactInfo(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("Name", db.String)
    email = db.Column("Email", db.String)
    message = db.Column("Message", db.String)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message


class UserInfo(db.Model):
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

        user = ContactInfo(name, email, message)
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
    form = LoginForm()
    # if form.validate_on_submit():
    #     log_user = UserInfo(username=form.username.data, password=form.username.data)
    #     db.session.add(log_user)
    #     db.session.commit()
    #     return flash("User has been created")
    if request.method == "POST":
        if form.validate_on_submit():
            username = request.form["username"]
            password = request.form["password"]
            user = UserInfo.query.filter_by(username=username).first()
            if user and user.password == password:
                flash('Login requested for user {}'.format(form.username.data))
                return redirect('/home')

    # if request.method == "POST":
    #     username = request.form["username"]
    #     password = request.form["password"]
    #     session["username"] = username
    #     print(UserInfo.query.all())
    #
    #     users = UserInfo.query.all()
    #     for user in users:
    #         print(user.username)
    #
    #     #     if same name and same pw  create session sinon error message
    #
    #     log_user = UserInfo(username, password)
    #     db.session.add(log_user)
    #     db.session.commit()

    # if "username" in session:
    #     flash("You have been logged in!")

    return render_template("logUser.html", form=form, message="Log in ")


@app.route('/view')
def view():
    return render_template("view.html", values=UserInfo.query.all())


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
