from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Q5Y5tM4G8vDHav7z"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/Database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class PostForm(FlaskForm):
    post = TextAreaField('post', validators=[InputRequired()])
    post_submit = SubmitField('Post')


class PlayForm(FlaskForm):
    have_btn = SubmitField('I have')
    have_not_btn = SubmitField('I have not')


class SignUpForm(FlaskForm):
    signup_username = StringField('signup_username', validators=[InputRequired()])
    signup_password = PasswordField('signup_password01', validators=[InputRequired()])
    signup_confirm_password = PasswordField('signup_password02', validators=[InputRequired()])
    signup_confirm_btn = SubmitField('Sign Up')


class ContactForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired()])
    message = TextAreaField('message', validators=[InputRequired()])
    send = SubmitField('Send')


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('Log In')


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


class PostInfo(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    post = db.Column("Post", db.String)
    have = db.Column("I have", db.Integer)
    have_not = db.Column("I have not", db.Integer)

    def __init__(self, post, have, have_not):
        self.post = post
        self.have = have
        self.have_not = have_not


@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/learnmoreaboutme')
def moreAboutMe():
    return render_template("learnMoreAboutMe.html")


@app.route('/contact', methods=["POST", "GET"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate_on_submit():
            name = request.form["name"]
            email = request.form["email"]
            message = request.form["message"]
            user = ContactInfo(name, email, message)
            db.session.add(user)
            db.session.commit()

            # query

        return redirect(url_for("thankyou", name=name, email=email, message=message))

    else:
        return render_template("contact.html", form=form)


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


@app.route('/justforfun', methods=["POST", "GET"])
def justForFun():
    form = PostForm()
    play = PlayForm()
    if request.method == "POST":
        if form.validate_on_submit():
            post = request.form["post"]
            user_post = PostInfo.query.filter_by(post=post).first()
            if user_post is None:
                user = PostInfo(post, None, None)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("justForFun"))
            else:
                flash('Post already exists!', 'red')
                return render_template("justForFun.html", form=form, form1=play, values=PostInfo.query.all())

    return render_template("justForFun.html", form=form, form1=play, values=PostInfo.query.all())


@app.route('/logout')
def logOut():
    if "user" in session:
        session.clear()
        flash('Logged out successfully!', 'green')
        return redirect(url_for("logIn"))
    else:
        flash('Not logged in', 'red')
        return redirect(url_for("logIn"))


@app.route('/login', methods=["POST", "GET"])
def logIn():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            username = request.form["username"]
            password = request.form["password"]
            user = UserInfo.query.filter_by(username=username).first()
            if user and user.password == password:
                session["user"] = username
                return render_template("home.html")
            else:
                flash('Log in unsuccessful!', 'red')
    else:
        if "user" in session:
            return redirect(url_for("home"))
    return render_template("login.html", form=form)


@app.route('/signup', methods=["POST", "GET"])
def signup():
    form = SignUpForm()
    if request.method == "POST":
        if form.validate_on_submit():
            signup_username = request.form["signup_username"]
            signup_confirm_password = request.form["signup_password"]
            signup_user = UserInfo.query.filter_by(username=signup_username).first()
            if signup_user is None:
                log_user = UserInfo(signup_username, signup_confirm_password)
                db.session.add(log_user)
                db.session.commit()
                flash('Successfully signed up!', 'green')
                return redirect('/login')
            else:
                flash('Username already exists!', 'red')
                return render_template("signUp.html", form=form)
    else:
        return render_template("signUp.html", form=form)


@app.route('/view')
def view():
    return render_template("view.html", values=PostInfo.query.all())


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
