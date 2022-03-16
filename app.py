from flask import Flask, render_template
from data import test_posts, post1 #importing the test data and keeping that in a separate python file
from data import users

app = Flask(__name__)

@app.route('/')
def feed():

    title = "My Feed"

    return render_template('feed.html', title=title, posts=test_posts)

@app.route('/comments/<int:post_id>')
def comments(post_id):

    title = "Comments"

    post = test_posts[post_id]

    return render_template('comments.html', title=title, post=post)

@app.route('/profile/<int:user_id>')
def profile(user_id):

    profile = users[user_id]

    title = f"{profile['Name']}'s Profile"

    return render_template('profile.html', title=title, profile=profile, posts=test_posts)