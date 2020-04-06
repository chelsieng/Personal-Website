from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/contact.sqlite3'
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


@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html")


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

@app.route('/view')
def view():
    return render_template("view.html", values=contact_info.query.all())

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


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
