"""
Blog Website Flask Application
------------------------------

This application is a Flask-based blog site with the following features:

Features:
---------
1. Home Page (`/`):
   - Displays all blog posts retrieved from an external API.

2. Post Page (`/post/<int:index>`):
   - Displays the content of a single blog post, dynamically based on the post's ID.

3. About Page (`/about`):
   - A static "About" page.

4. Contact Page (`/contact`):
   - Users can fill out a form to send a message.
   - Form submission triggers an email sent to the site owner.
   - Success or failure feedback is displayed.

5. Email Integration:
   - Emails are sent via Gmail using the `smtplib` library.
   - Environment variables (`My_Email`, `PASSWORD`) are used for security.

External Dependencies:
----------------------
1. `requests`: For fetching blog posts from an API.
2. `smtplib` and `ssl`: For email communication.
3. `dotenv`: For managing environment variables.

How to Run:
-----------
1. Set up a `.env` file with the following:
   - `My_Email`: Your Gmail address.
   - `PASSWORD`: Your Gmail app password (not the actual account password; use an App Password).
2. Run the application with:
   ```bash
   python app.py
"""

import ssl
from flask import Flask, render_template,request
import requests
import smtplib
import os
import dotenv
from flask.cli import load_dotenv


load_dotenv()

# Create connection to send email.
my_email = os.environ.get("My_Email")
password = os.environ.get("PASSWORD")

connection = smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email,password=password)
context= ssl.create_default_context() # CREATES A SECURE SSL CONTEXT

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        email_message = f"Subject: Contact Inquiry\n\n Name: {name}\n Email: {email}\n Phone: {phone}\n\nMessage: {message}"

        connection.sendmail(from_addr=my_email,to_addrs="dimplekaware@gmail.com",msg=email_message)
        connection.quit()
        return render_template("contact.html",msg_sent=True)

    return render_template("contact.html",msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
