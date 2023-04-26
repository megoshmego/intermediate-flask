0:00
(bright upbeat music)
0:04
- [Instructor] All right, so we have our basic
0:06
auth implemented, we can register,
0:08
we can log in and we can log out.
0:11
Now let's also add in some other functionality.
0:14
We're gonna keep this simple.
0:15
We'll add a tweet model and a user can create a tweet,
0:19
and that tweet will be associated
0:20
with whoever is the currently logged in user.
0:23
And then we'll be able to see other people's tweets.
0:27
And basically we'll just see how we can associate a tweet
0:30
with the person who's currently logged in,
0:32
as well as potentially prevent someone from deleting a tweet
0:35
that they didn't create.
0:37
So let's start with a new model in our model's file.
0:41
This one will be called tweets,
0:43
and it's gonna be extremely simple.
0:46
db.model, we're not gonna bother with hashtags
0:49
or likes or anything like that.
0:50
It will just have some text, we'll call it tweet text.
0:54
It's going to have an ID
0:56
and it will have a user ID as a reference
0:59
to the user table or user's table.
1:03
The user who created the tweet.
1:05
So we can't just have a tweet that doesn't have a user ID.
1:07
It has to belong to somebody.
1:09
So we'll start with our dunder table name,
1:14
which will be tweets.
1:17
We'll add in an ID and just copy this line.
1:22
Then we'll add in the text, which is db.Column Text
1:28
or db.Text.
1:30
It's required so no level will be false.
1:35
And a user ID,
1:38
user underscore ID equals db.Column.
1:43
It will just be an integer.
1:47
And then we'll set up the foreign key constraint
1:49
to make sure this is a actual user ID that exists
1:52
on the user's table.
1:54
db.ForeignKey users, that's the table name.id.
2:00
And we could also set up a relationship with SQLAlchemy.
2:03
So from tweets, we'll be able to access the user.
2:07
So we'll just call that user,
2:08
if we wanna know the person's name who created it,
2:11
or if we wanted to know, I don't know.
2:14
I guess that's pretty much it (chuckles).
2:16
We won't want the password hash,
2:17
but we could also set up a back ref
2:19
so that we could go from a user and view their tweets.
2:22
It's a one to many relationship,
2:23
a tweet belongs to one user,
2:25
a user can have multiple tweets, db.relationship user,
2:30
and then we'll add back ref what name makes sense?
2:33
Probably just tweets.
2:34
This will be the other relationship going from tweet
2:37
or from user rather to tweets.
2:40
So we'll call it tweets, plural.
2:43
All right, so it's always a good idea
2:45
just to start with this and make sure that this works.
2:49
I'm gonna stop our server.
2:52
I do need to make sure I'm importing tweets
2:54
in my app from models.
2:58
And then add Python.
3:02
Clear and then we'll do percent run app.py,
3:08
and we need to do a db.create_all as a method.
3:14
And that will now make our tweet table.
3:17
Now let's take some user.
3:19
Let's just look at all of our users,
3:21
user.query.all, let's pick one ID.
3:24
It doesn't really matter which one.
3:26
Let's take user ID of three and make a new tweet.
3:29
So we'll go with T equals tweet, which has text set two.
3:35
This is my first tweets.
3:40
And then we'll set user ID
3:44
to be three or four.
3:47
All right, so we've got T now db.session.add(t)
3:53
db.session.commit.
3:57
All righty, let's look at T, it has an ID.
4:01
It has some text.
4:04
No, it's not called tweet, it's called text.
4:07
This is my first tweets and it has a user ID
4:11
and we set up that relationship
4:13
so I should be able to ask for t.user and get that user.
4:17
And I should be able to go the other way around
4:19
if I have that user, I'll save that to a variable, U.
4:24
And I should ask for u.tweets,
4:26
or I should be able to ask for u.tweets.
4:28
There's only one that belongs to that user.
4:31
So our models are now set up.
4:33
Let's create a form and a route
4:35
so that we can create a new tweet.
4:37
So we have our get route for slash tweets.
4:40
I think what I'm going to do is have...
4:42
Let me go to slash tweets here,
4:44
have the tweets show up that are currently in the database,
4:47
as well as a form on this exact page that will allow you
4:50
to make a new tweet.
4:52
So we don't just have to have a separate route
4:54
to show the form and a separate route to view the tweets.
4:56
We'll just embed the add new tweet form here as well.
5:00
And then it will submit a post request to slash tweets,
5:03
just like we've been doing.
5:05
So let's make this both a GET and POST.
5:11
GET, POST.
5:14
And then in here we will need to create a new form
5:18
which doesn't exist yet.
5:20
And to make our form, it's going to be extremely simple
5:23
for a tweets because there's really only one thing
5:26
that a user is going to specify in the form.
5:29
So we'll create our class tweet form, rather,
5:32
not just tweet, which inherits from FlaskForm.
5:36
And it's only going to have a text attribute,
5:40
one text field, and that will be a string field.
5:44
I guess we could do a text area field.
5:47
We can play around with it and see what works best.
5:50
And we'll go with, what's a good label?
5:52
Tweet text, and that will be required.
5:58
We don't want you to make an empty tweets.
6:00
So passing validators input required.
6:04
And that's really it for our tweet form.
6:07
We will need to specify the user ID,
6:09
but we don't ask a user to do that.
6:11
We will instead just automatically do it
6:13
based off of whoever is logged in,
6:15
whatever's in the session,
6:16
we'll just take that user ID.
6:18
So tweet form, let's import that from forms.
6:23
Great, now here we are going to create a new instance.
6:28
So form equals tweet form just like that.
6:33
And then we'll add in our basic logic
6:36
and I'm gonna reorder this.
6:37
We won't even bother making the form.
6:40
If a user is not logged in,
6:42
we'll just redirect them right away.
6:44
And then we can make the form.
6:46
It won't really make a difference
6:47
in terms of what a user sees,
6:49
but there's no reason to make this
6:51
and instantiate a new instance of our form
6:54
if we're going to redirect anyway.
6:56
So then we will pass that form in, form equals form.
7:01
And then in our tweets file, tweets at HTML,
7:04
we can display the form.
7:06
So we'll have viewing tweets.
7:07
Maybe up top, we'll put the form,
7:11
so above, where should we do that?
7:14
Maybe tweets, and then we'll have the form here.
7:17
So we'll do a form action equals POST,
7:20
rather that's method, not action.
7:22
We'll keep the action the same,
7:24
because we're just sending a post request to the same route.
7:27
And then I'm just gonna steal my loop from...
7:30
I mean, I don't even need to loop, honestly.
7:33
There's just one field, but we can modify this.
7:37
So we'll take our loop there.
7:39
Probably even keep this button from our register form
7:43
and put it inside of this form here.
7:46
So we've got our CSRF hidden tag with the token.
7:51
And then if we had other forms or other fields eventually,
7:54
which we definitely could,
7:56
might as well just loop through all of them.
7:58
We'll add form control, what else?
8:01
Text danger if there's an error and then button success,
8:05
we'll go with post tweets, tweets.
8:09
What should we go with, post?
8:11
I don't really use Twitter,
8:12
so I don't know what they call it.
8:13
Make tweet and save tweet.
8:16
Let's see if we're getting this form.
8:18
So if we refresh the page, oh, gotta start that server.
8:23
Amateur flask run .
8:29
Refresh again, all right.
8:31
So now we have a place where we can type some tweets.
8:35
Let's also display the current tweets down here.
8:38
So an app.py, we will want to get all the tweets.
8:42
For now we'll just get all of them.
8:44
Obviously real Twitter has some pretty intense logic
8:49
to figure out what tweets to show somebody
8:50
based off of who they follow, but also what's trending
8:54
and further within that there might be a thousand tweets
8:58
that could be shown on your page
9:00
that you follow, from users that you follow.
9:04
It's going to be limited or sorted or ordered in some way,
9:07
but we're just gonna show everything.
9:08
Right now we have one tweet in our database,
9:11
so let's get all tweets equals tweet.query.all.
9:18
So we're not gonna have the idea of following.
9:21
We're just gonna show everybody everyone's tweets
9:23
once you're logged in.
9:25
Now later on in just actually just a bit,
9:28
we're gonna wrap up flask and talk about deploying
9:31
and that sort of thing.
9:32
Then you'll have an exercise
9:33
that is a much more feature intense version of Twitter.
9:38
It's still not recreating Twitter from scratch,
9:41
but you will have things like following relationships
9:43
so that you can follow certain people or unfollow them.
9:46
We'll have likes so you can like a tweets and unlike it.
9:50
So it's a lot more involved, but this is a good start.
9:53
So all tweets and we'll pass that through.
9:56
So form equals form and then tweets equals all tweets.
10:02
Now let's iterate over tweets in our tweets at HTML.
10:06
We'll put it down below the form.
10:08
We'll just start with something super boring, a UL,
10:12
and then we'll loop over tweets
10:13
or, yeah, it's called tweets so for tweet in tweets.
10:20
Just like that,
10:23
and our loop endfor.
10:28
We'll make an LI for each one
10:30
where we just display tweets.text
10:34
and that's pretty much it to start.
10:35
So let's see if that works.
10:36
All right, this is my first tweet.
10:39
Okay, if we wanted to show the username, by the way,
10:43
what would be the best way for us to...
10:46
I guess we could start by just bolding the username.
10:49
So to get that username,
10:51
it's not on the tweet itself, right?
10:53
It's only the user ID that's stored,
10:55
but we added that relationship.
10:56
So we can do tweet.user.username
11:00
and maybe just a dash.
11:02
Why don't we make a bold tag or a strong tag or something?
11:07
Put that in there.
11:10
All right, Blue the cat, this is my first tweet.
11:13
We can worry about styling it later.
11:15
It really is not the focus here.
11:17
So if we had more tweets, they'd all be showing up here.
11:20
Great, now let's make it so that we can actually create
11:23
a new tweet and hopefully see it show up down here.
11:26
Right now, I do have the post route
11:28
that my form will submit to,
11:30
but I don't have the logic to validate the form,
11:34
so I'm just gonna do that down here.
11:36
If form.validate on submit,
11:39
we just need to get the text equals form.text.data.
11:47
Then we'll want to make a new tweet
11:50
and save that db.session.ad, db.session.commit.
11:55
But before we do that,
11:56
we'll want to set the user ID on that tweet.
12:00
So we'll do new tweet equals tweet,
12:06
or we pass in text equals the text from the form,
12:10
and we wanna pass in the user ID,
12:13
but where's the user ID stored?
12:15
Well in order to make it to this point,
12:16
remember that we're checking if user ID is in the session.
12:19
If not none of this code runs anyway.
12:22
We're redirecting you, asking you to log in first.
12:25
So we can get that user ID from session, session of user ID.
12:30
So user ID equals session of user ID.
12:39
Now later on, like in this tweet exercise
12:43
or the Twitter exercise you have coming up,
12:45
we'll see some nice helper methods we can make.
12:48
Instead of having to always ask session user ID,
12:51
we'll be able to designate certain routes
12:53
as ones that you must be logged in for.
12:57
So we could add, think of like a decorator here that...
13:00
All we would have to write is authenticate before.
13:04
And I wouldn't have to do any of this logic.
13:06
It would just automatically redirect if you're not logged in
13:11
and I could put that before any route that I want,
13:13
but right now we're just learning the basics.
13:15
So we'll just pass this in manually,
13:17
we'll reference session of user ID.
13:20
We'll also see that you could make a current user variable
13:23
instead of having to reference the session itself.
13:26
This is fine though, session of user ID.
13:30
And then once we do that,
13:32
we wanna do a db.session.add new tweet
13:37
and then a db.session.commits.
13:40
And then we want to redirect just back to the same route
13:44
slash tweets, but as a GET request,
13:46
so redirect slash tweets, and why don't we flash a message?
13:52
Tweet created, great.
13:59
Okay, moment of truth here.
14:02
Always forget first to return that redirect,
14:04
gotta return it.
14:05
All right, let's see what happens.
14:08
Fingers crossed.
14:09
So I'm logged in as somebody right now, I believe.
14:12
Let's try making a new tweets.
14:14
So I've typed out my first tweet.
14:16
I don't know who I'm logged in as at the moment.
14:18
We definitely could add a username up in the NAF bar.
14:21
A lot of sites do that,
14:23
but let's click post tweet.
14:26
Tweet created, and it says it was created by Bob.
14:29
It does persist in our database.
14:31
I'm refreshing, if I go over to Postgres,
14:34
we do a select star from tweets.
14:39
We can see that the first one was created
14:41
with a user ID of three.
14:43
This one was created by a user ID of four, which is Bob.
14:47
Now, if I were to log out goodbye.
14:50
If I try and go back to slash tweets,
14:52
of course, it's not gonna work if I spell it correctly.
14:56
We're not allowed to go there.
14:57
It's just taking us back to the roots,
14:59
but if I log in, let's use a different account
15:01
who's not Bob, how about...
15:03
Do we still have Willy Wonka in our database?
15:06
Nope, I guess not, do we?
15:09
Oh no, that was earlier.
15:11
All right, so we've got Bob and Blue the cat.
15:14
Maybe I'll just make a new account,
15:16
so instead of Bob, how about...
15:19
How about I love Lucy
15:25
and password will be chickens.
15:30
I know it's boring, I'm obsessed with my chickens, aren't I?
15:34
All right so we're just registered.
15:35
Now if I post a tweets, hello, is this thing on?
15:37
Post tweets, it's coming from, I love Lucy.
15:41
So we are using that user ID in the session
15:43
to display the username of a tweets.
15:46
It's working pretty well, right?
15:48
We're actually authenticating somebody,
15:50
but we're also associating them with some content
15:53
that we're storing, so it's not just gate-keeping
15:55
and showing and hiding a page
15:57
and forcing someone to log in.
15:58
We're also able to know who that person is
16:01
and associate them with the form or with the data
16:05
that we're creating with the new tweets.
16:07
They don't have to type in their username.
16:09
They don't have to type in their user ID.
16:11
It's pretty nice.
16:12
A couple of things to consider here.
16:14
First of all, every time we are printing out the username,
16:18
we're making a separate query.
16:20
We're getting each tweet and then printing each tweets
16:23
or not printing, but rendering the tweet text
16:26
and tweet.user.username,
16:30
and that results in a query for each one of those tweets.
16:34
At least right now, we have three distinct usernames.
16:37
So we'll get three separate queries to get that username.
16:41
So we kinda talked about this
16:42
back when we were covering SQLAlchemy.
16:44
It would definitely be more efficient
16:46
to fetch all of them at once.
16:47
So send a single query using a join
16:51
and go and just get the appropriate usernames
16:54
and whatever other information you want
16:56
about a user and the tweet all at once.
16:59
But we'll keep it simple.
17:00
But that is something that you should keep in mind
17:02
because if this was real Twitter
17:04
with thousands or millions of tweets,
17:06
I guess we're not gonna fetch millions at once.
17:08
But if we had even just a couple hundred,
17:10
we would be making a lot of additional queries
17:12
just to get that username.
17:15
Okay so we've got this set up.
17:16
Next let's do one more feature where we can delete a tweet,
17:22
but you can only delete a tweet you've created.
17:24
So that will be next.
17:26
(bright upbeat music)
