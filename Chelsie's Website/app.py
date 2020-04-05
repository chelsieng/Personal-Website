from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
