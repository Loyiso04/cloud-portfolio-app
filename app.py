from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
#app.secret_key = "super-secret-key"

import os

app.secret_key = os.environ.get("SECRET_KEY", "dev-key")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")

    print("New Contact Submission")
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)
    print("Message:", message)
    print("-" * 30)

    flash(" Your message has been sent successfully!")

    # Redirect BACK to contact section
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
