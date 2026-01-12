from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)

import os

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

app.secret_key = os.environ.get("SECRET_KEY", "dev-key")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    contact = Contact(
        name=request.form.get("name"),
        email=request.form.get("email"),
        phone=request.form.get("phone"),
        message=request.form.get("message")
    )

    db.session.add(contact)
    db.session.commit()

    flash("Your message has been saved successfully!")
    return redirect(url_for("home"))

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(50))
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Contact {self.email}>"
