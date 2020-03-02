from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/project')
def project():
    return render_template("project.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/media')
def media():
    return render_template("media.html")


@app.route('/makeYourDay')
def makeYourDay():
    return render_template("makeYourDay.html")


if __name__ == '__main__':
    app.run(debug=True)
