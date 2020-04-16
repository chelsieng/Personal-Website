from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "Q5Y5tM4G8vDHav7z"
app.permanent_session_lifetime = timedelta(minutes=20)  # session time out (20 minutes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/Database.sqlite3'  # creating database in data folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# configuring mail setting
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'chelsiewebsite@gmail.com'  # enter your email here
app.config['MAIL_DEFAULT_SENDER'] = 'chelsiewebsite@gmail.com'  # enter your email here
app.config['MAIL_PASSWORD'] = 'cnnavjtiyspwpsih'  # enter your password here
mail = Mail(app)


# Post form from justForFun.html
class PostForm(FlaskForm):
    post = TextAreaField('post', validators=[InputRequired()])
    post_submit = SubmitField('Post')


# Play form from justForFun.html
class PlayForm(FlaskForm):
    play_post = StringField('play_post', validators=[InputRequired()])
    have_btn = SubmitField('I have')
    have_not_btn = SubmitField('I have not')


# SignUp form from signUp.html
class SignUpForm(FlaskForm):
    signup_username = StringField('signup_username', validators=[InputRequired()])
    signup_password = PasswordField('signup_password01', validators=[InputRequired()])
    signup_confirm_password = PasswordField('signup_password02', validators=[InputRequired()])
    signup_confirm_btn = SubmitField('Sign Up')


# Contact from from contact.html
class ContactForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired()])
    message = TextAreaField('message', validators=[InputRequired()])
    send = SubmitField('Send')


# Log in form from login.html
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    submit = SubmitField('Log In')


# database for contact form
class ContactInfo(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("Name", db.String)
    email = db.Column("Email", db.String)
    message = db.Column("Message", db.String)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

    @property
    def id(self):
        return self._id


# database for log in and sign up form
class UserInfo(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    username = db.Column("Username", db.String)
    password = db.Column("Password", db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password


# database for never have i ever game
class PostInfo(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    post = db.Column("Post", db.String)
    have = db.Column("I have", db.Integer)
    have_not = db.Column("I have not", db.Integer)

    def __init__(self, post, have, have_not):
        self.post = post
        self.have = have
        self.have_not = have_not


# hashing user password
def hashPwd(password):
    hash_password = generate_password_hash(password)
    return hash_password


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
            # adding contact info in database
            user = ContactInfo(name, email, message)
            db.session.add(user)
            db.session.commit()
            user_id = user.id
            # getting contact info from database
            user_info = ContactInfo.query.filter_by(_id=user_id).first()
            name = user_info.name
            email = user_info.email
            message = user_info.message
            # sending email to confirm message was sent successfully
            msg = Message("Email Received!", recipients=[email])
            msg.html = "<p>Dear " + name + ",</p><p>Thank you for your email. I will contact you shortly.</p><p>All the best,</p>Chelsie</p><hr><p>Your message:</p>" + message
            mail.send(msg)
            # sending email to owner of website to notify about new messages
            msg1 = Message("New Message from Contact Form", recipients=["chelsiewebsite@gmail.com"])
            msg1.html = "<p>From: " + name + "</p><p>Email: " + email + "</p><p>Message: " + message + "</p>"
            mail.send(msg1)
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
    have = request.form.get('have_btn')
    have_not = request.form.get('have_not_btn')
    post_submit = request.form.get('post_submit')
    db_dict = PostInfo.query.all()
    if "play" in session:
        if request.method == "POST":
            if form.validate_on_submit():
                if post_submit == "Post":
                    post = request.form["post"]
                    # getting post from database
                    user_post = PostInfo.query.filter_by(post=post).first()
                    # when post does not exists, add in database
                    if user_post is None:
                        user = PostInfo(post, 0, 0)
                        db.session.add(user)
                        db.session.commit()
                        return redirect(url_for("justForFun"))
                    # when post already exists, flash message
                    else:
                        flash('Post already exists!', 'red')
            if play.validate_on_submit():
                post_vote = request.form["play_post"]
                # when user clicks I have button
                if have == "I Have":
                    # getting post related to button, update results
                    user_have = PostInfo.query.filter_by(post=post_vote).first()
                    user_have.have += 1
                    db.session.commit()
                    db_dict = PostInfo.query.all()
                    # adding player in  session
                    playlist = session["play"]
                    playlist.append(user_have._id)
                    session["play"] = playlist
                    for item in db_dict:
                        # when player already pressed button for related post in session, disable button
                        if item._id == user_have._id or (item._id in session["play"]):
                            item.display = 'block'
                            item.disable = True
                        # when player press button for related post for the first time in session, enable button
                        elif not (item._id in session["play"]):
                            item.display = 'none'
                            item.disable = False
                        # when post has no results yet
                        if item.have == 0 and item.have_not == 0:
                            item.havePercentage = 0
                            item.haveNotPercentage = 0
                        else:
                            # calculating have% and havenot% button clicked
                            item.havePercentage = (item.have / (item.have + item.have_not)) * 100
                            item.haveNotPercentage = (item.have_not / (item.have + item.have_not)) * 100
                # when user clicks I have not button
                elif have_not == "I Have Not":
                    user_have_not = PostInfo.query.filter_by(post=post_vote).first()
                    user_have_not.have_not += 1
                    db.session.commit()
                    db_dict = PostInfo.query.all()
                    playlist = session["play"]
                    playlist.append(user_have_not._id)
                    session["play"] = playlist
                    for item in db_dict:
                        if item._id == user_have_not._id or (item._id in session["play"]):
                            item.display = 'block'
                            item.disable = True
                        elif not (item._id in session["play"]):
                            item.display = 'none'
                            item.disable = False
                        if item.have == 0 and item.have_not == 0:
                            item.havePercentage = 0
                            item.haveNotPercentage = 0
                        else:
                            item.havePercentage = (item.have / (item.have + item.have_not)) * 100
                            item.haveNotPercentage = (item.have_not / (item.have + item.have_not)) * 100
        # when user does not play
        else:
            for item in db_dict:
                if not (item._id in session["play"]):
                    item.display = "none"
                    item.disable = False
                    item.haveNotPercentage = 0
                    item.havePercentage = 0
                else:
                    item.display = 'block'
                    item.disable = True
                    item.havePercentage = (item.have / (item.have + item.have_not)) * 100
                    item.haveNotPercentage = (item.have_not / (item.have + item.have_not)) * 100

    return render_template("justForFun.html", form=form, form1=play, values=db_dict)


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
            # getting user from database by username
            user = UserInfo.query.filter_by(username=username).first()
            # checking if user's password and entered password are the same
            if user and check_password_hash(user.password, password):
                session["user"] = username
                session["play"] = []
                session.permanent = True
                return render_template("home.html")
            else:
                flash('Log in unsuccessful!', 'red')
    # user already logged in
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
            # getting user info from database by username
            signup_user = UserInfo.query.filter_by(username=signup_username).first()
            # if username does not exists, add info in database
            if signup_user is None:
                log_user = UserInfo(signup_username, hashPwd(signup_confirm_password))
                db.session.add(log_user)
                db.session.commit()
                flash('Successfully signed up!', 'green')
                return redirect('/login')
            # username already occupied
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
