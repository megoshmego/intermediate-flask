Video Title: Authorization Demo 5
Section Title: Intermediate Flask
Subsection Title: Hashing and Logging In

Key Terms, Ideas, Concepts, and Definitions:

Authentication: The process of verifying the identity of a user in a web application. The instructor demonstrates how to register, log in, and log out.

Tweet Model: A simple model that represents a tweet in the web application. It has an ID, tweet text, and a user ID as a reference to the user's table. The model is created using SQLAlchemy and associated with the currently logged-in user.

One-to-many relationship: In the context of the video, a tweet belongs to one user, while a user can have multiple tweets.

FlaskForm: A class from Flask-WTF library used to create and handle web forms.

GET and POST: HTTP methods for sending and receiving data in a web application. In the example, the instructor uses both methods for the '/tweets' route to display and add new tweets.

CSRF token: A hidden form input used to protect against Cross-Site Request Forgery attacks.

db.create_all(): A method used to create all the tables in the database based on the defined models.

form.validate_on_submit(): A method from FlaskForm that checks if the form has been submitted and if its data is valid.

In this tutorial, you implemented user authentication and created a tweet association with the user who posted it. You displayed the username of the author for each tweet on the page. Next, you want to add a feature to delete a tweet, but only if the logged-in user is the one who created it. Here's how you can do that:

Add a delete button next to each tweet in the HTML template:
html
Copy code
{% for tweet in tweets %}
  <p>{{ tweet.text }} - {{ tweet.user.username }}
  {% if tweet.user_id == session['user_id'] %}
    <form action="{{ url_for('delete_tweet', tweet_id=tweet.id) }}" method="POST">
      <input type="submit" value="Delete">
    </form>
  {% endif %}
  </p>
{% endfor %}
In your Python file, create a new route to handle the deletion of a tweet:
python
Copy code
@app.route('/delete_tweet/<int:tweet_id>', methods=['POST'])
def delete_tweet(tweet_id):
    if 'user_id' not in session:
        flash('You must be logged in to delete a tweet.')
        return redirect(url_for('login'))

    tweet = Tweet.query.get(tweet_id)
    if not tweet:
        flash('Tweet not found.')
        return redirect(url_for('tweets'))

    if tweet.user_id != session['user_id']:
        flash("You can't delete someone else's tweet!")
        return redirect(url_for('tweets'))

    db.session.delete(tweet)
    db.session.commit()
    flash('Tweet deleted.')
    return redirect(url_for('tweets'))
In this code, you first check if the user is logged in. If not, you redirect them to the login page. Then, you query the database for the tweet with the given ID. If the tweet doesn't exist, you inform the user and redirect them back to the main tweets page. If the user is not the creator of the tweet, you display an error message and prevent them from deleting it. If the user is the creator, you delete the tweet from the database and redirect the user back to the main tweets page.

Now you have a working delete feature that only allows users to delete their own tweets.
