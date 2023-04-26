anscript


0:00
(upbeat music)
0:04
- [Instructor] Alrighty.
0:05
So to implement delete functionality,
0:08
we need to first have a button or a form
0:10
or something we'll click to actually send a delete request
0:14
or some sort of request.
0:16
Now, if we were following RESTful routing conventions,
0:18
it would send a delete request.
0:20
But to keep things simple,
0:22
since we can't make a delete request from a form,
0:24
and I don't want to use JavaScript
0:26
or involve Ajax or anything,
0:28
we're just going to make a form that sends a post request
0:30
and we'll have a delete route that is a post route.
0:33
But we're only going to show that form,
0:35
and the form itself will only consist of a button.
0:38
We're only going to show it
0:40
for users who created a given tweet.
0:43
So if I'm logged in as ILoveLucy,
0:45
I'll only see a delete button here.
0:47
I won't be able to delete these two.
0:50
So let's first show a button on all those tweets.
0:55
So right here for tweet in tweets,
0:59
what should we do here?
1:00
It's going to be crowded in this LI.
1:02
Eventually we'll style this better.
1:05
It's not really the focus.
1:06
But let's just put a button in there.
1:09
Even just a form to start.
1:10
Action will be slash tweets.
1:13
How about just slash delete.
1:16
But we will need to also include
1:17
an ID of what we're deleting.
1:20
And then our form will have a button.
1:25
Let's do a class from bootstrap,
1:27
BTN button small, and danger, maybe?
1:33
And then just an X or a delete icon or something.
1:37
So this should show up for every single tweet at the moment.
1:41
Also on our form, it's kind of hacky,
1:43
but let's just give it a display style of display inline.
1:51
Let's see if that will work for us.
1:53
All right.
1:54
So a form is a block level element,
1:56
so we'll end up just getting all those extra lines,
1:59
which we don't want.
2:00
So at the moment, if I click one of these,
2:02
first of all they're showing up on every single tweet
2:05
regardless as to whether this person,
2:07
whoever's logged in, I'm logged in as ILoveLucy,
2:10
created that tweet or not.
2:12
So we could show that, or hide it, based off of
2:15
if the session user ID equals the tweet user ID.
2:21
And we can just add in some logic here.
2:23
So if session of user ID,
2:32
so if session of user ID equals the particular tweet
2:37
that we're looping over each individual tweet.user_id,
2:43
display this form
2:45
and otherwise we're not going to show anything.
2:49
So just this form, there's no else.
2:52
And there we go, I can only see the button
2:54
if I'm logged in as ILoveLucy on this one tweet
2:57
that ILoveLucy created.
2:59
If I had more tweets, just put some gibberish in here,
3:03
I'll see a button there too,
3:05
but not for the other tweets created by other users.
3:08
So we are showing and hiding that button.
3:11
That's good.
3:12
But technically once we implement our route
3:15
somebody could still send a delete request to any of these
3:19
and we're not preventing them from deleting something.
3:22
We're just hiding the button.
3:23
So that is not really securing that route.
3:25
We're not making sure that a user has permission to delete.
3:29
We're only making sure that a user
3:30
has permission to see the delete button.
3:33
But we also need to secure it
3:34
on the actual app.py route.
3:38
So let's make our routes to delete something.
3:40
As I mentioned, it will just be a post request.
3:43
Just do it next to my tweets here.
3:46
And we're not following RESTful routing conventions.
3:48
So I'm just going to make a route slash tweets,
3:53
and then we want the tweet ID.
3:56
Most likely we could send that as part of the form data,
3:59
but it's easiest if it's just in the URL.
4:01
So we want that tweet ID in here.
4:03
We'll call this, what should we call it, just ID?
4:07
Sure, and then slash delete.
4:10
Or we could just do this:
4:12
slash tweets slash ID as a post request.
4:21
And then define our view function,
4:23
delete tweets, which will be passed in an ID.
4:28
And I'll add a little doc string here, delete tweet.
4:36
Eh, not the best, but short.
4:38
Good enough for now.
4:40
And we want to take that ID that we'll get
4:43
from this route or from the path
4:45
and find the tweet and then delete it.
4:48
But we also want to make sure that a user,
4:50
the current user signed in, session of user ID,
4:53
is the owner of that tweet.
4:56
So we don't want someone to be able
4:57
to just send a post request to slash tweets slash five
5:01
if they don't own that tweet.
5:03
And they need to be logged in too,
5:04
in order for us to know that.
5:06
So let's get the tweet first, tweet.query,
5:10
and then we can do the simple get_or_404 method
5:14
from Flask SQLAlchemy, pass in that ID.
5:19
We'll call that tweet.
5:21
If we find that tweet, which if we make it to this point,
5:25
we will otherwise we'll have a 404.
5:27
If we find it, we want to make sure
5:29
the user can delete that.
5:30
So if tweets.user_id equals session of user_id,
5:38
If the person who is logged in is the owner of that tweet,
5:42
then we'll actually delete it.
5:44
So db.session.delete(tweet),
5:51
db.session.commit(),
5:55
and then we'll just redirect them to slash tweets.
5:58
Return redirect slash tweets.
6:03
And we'll flash something first.
6:05
Flash tweet deleted.
6:10
Now, if they don't own it, what do we want to do?
6:15
Why don't we just flash something like,
6:17
"You don't have permission to do that."
6:24
And then redirect back to tweets again.
6:27
Return redirect slash tweets as well.
6:32
All right, so one thing that we're not handling,
6:35
or one scenario, is if a user is not logged in at all
6:39
and they somehow submit a post request
6:41
to slash tweets slash five or three or two.
6:44
Right now what will happen is we'll try and find that tweet.
6:47
Assuming it does exist, this will be false,
6:49
because there's nothing in the session for user ID.
6:52
And we're just going to flash,
6:53
"You don't have permission to do that."
6:55
We could add separate feedback that says,
6:57
"Please log in first."
7:00
That is a different case from somebody who is logged in
7:03
trying to submit a request here
7:05
to delete something they don't own.
7:07
But we'll just use this double purpose message.
7:10
"You don't have permission to do that."
7:12
Because technically if you're not logged in,
7:13
you don't have permission to do that either.
7:16
So now we'll see if it works.
7:19
We will cross our fingers and pray.
7:22
Let's try refreshing.
7:24
All right.
7:25
Make sure at the moment,
7:26
our form is not even submitting to the right spot.
7:29
It's slash tweets slash delete.
7:31
That's not what we want.
7:32
We want tweets slash that ID from the tweet.
7:35
So we'll add in our Jinja braces, and we want tweet.id.
7:43
And this should be a post request, so method equals post.
7:50
Okay, let's refresh.
7:52
Let's see what the form looks like.
7:54
Where is it submitting to?
7:56
It's going to tweet slash four.
7:59
This one above it is hopefully tweet slash three,
8:02
I would assume.
8:04
Great, now let's try clicking one
8:06
and see if our tweet is actually deleted.
8:10
Okay, it says it was deleted.
8:11
Let's look in our database.
8:14
It's not showing up.
8:17
Let's refresh.
8:18
It's gone!
8:20
All right.
8:21
Now, if I were to try and send a post request,
8:23
let's say from Insomnia, I'll try sending a post request.
8:27
So local host 5,000, slash tweets slash two as a post.
8:33
Let's see what happens here.
8:34
Send, and I'm getting a key error.
8:39
All right, so there is a problem with how
8:41
we're trying to access session of user ID,
8:45
instead of just checking immediately.
8:47
This is kind of what I was hinting at in this route.
8:50
Nope, in this route here.
8:52
We're just looking in session for user ID.
8:54
Remember that in a dictionary, if a key is not found,
8:57
we get this key error.
8:58
So we should add in a bit of protection first.
9:01
If user_id not in session then we will do another redirect,
9:11
we'll flash, "Please log in first",
9:17
and then return redirect to slash tweets.
9:23
And we could reduce some duplication here.
9:25
We're redirecting to slash tweets in multiple places,
9:29
but let's just see if it works, to start.
9:31
All right, so let's try it.
9:33
Just send the same post request.
9:36
Now it's telling me, please log in first.
9:39
Oh, we're getting a double flash
9:42
because we're redirecting to slash tweets.
9:44
We should redirect to either slash or maybe slash login.
9:48
Please log in first, try one more time.
9:51
Send.
9:52
Now we're seeing this: "Please log in first."
9:55
So now we have protection on both ends of things.
9:58
On the client side, we are only showing the delete link
10:01
or the button for that form,
10:03
to the user who owns that particular tweet.
10:06
But we also have protection on the server side
10:09
to make sure that in the event that someone
10:12
tried to delete someone else's
10:13
by sending a post request to a tweet that they don't own,
10:17
if they're not logged in, we're going to ask them to log in.
10:19
So you can't just circumvent this button showing and hiding
10:23
by trying to send your own request from scratch.
10:25
It still won't work.
10:27
And also if that tweet username does not match,
10:30
or the user ID does not match session of user ID,
10:33
we'll give you a different message.
10:34
"You don't have permission to do that",
10:35
and then redirect to slash tweets.
10:38
Okay?
10:39
So we now have some simple authentication
10:43
which is registering and logging in
10:45
and all of that, and authorization.
10:48
Remember authorization is permissions.
10:51
What is somebody allowed to do or not allowed to do
10:53
once you know who they are.
10:55
So authentication, finding out who someone is,
10:58
that they are who they say they are.
11:00
You log in with the correct credentials.
11:02
Okay?
11:02
Then we have authorization.
11:04
We have it in a pretty simple, at least in this application
11:08
right now, it's quite straightforward.
11:10
Only certain people, only the owner of a given tweet,
11:13
is authorized to view this delete button
11:16
and to actually delete the tweet.
11:19
Let's just go through the steps one more time
11:20
of signing up, let's make a new account.
11:23
How about CatFreak47?
11:27
And the password will be meowmeow.
11:32
We'll register, save that sure.
11:36
I'll make a new tweet,
11:37
which is just MEOW MEOW MEOW MEOW MEOW MEOW.
11:41
And we'll post the tweet.
11:43
Okay, I'm logged in as CatFreak47.
11:46
I can view it, I can delete it.
11:48
Let's log out and try and go to slash tweets again.
11:52
No cigar.
11:53
I'll log in as CatFreak47, I still see that tweet.
11:58
It's the only one I can delete.
12:00
We get our message up here.
12:02
It looks pretty good.
12:03
Styling is not great,
12:04
but you know, it's not the worst I've ever seen.
12:08
We're at least trying, we're making a slight effort.
12:11
And that's pretty much it for what I wanted to show you.
12:14
So you could easily extend what we've seen already
12:17
into editing tweets and following people.
12:21
We've seen the basics of how you show and hide
12:23
an entire route, or you close off a route
12:26
to people who are not authenticated.
12:28
And we've also explored the basics
12:30
of authorization where only certain people
12:33
have permission to delete or to even see that button.
12:37
So you could do the same thing for editing.
12:39
Or you could add in some other stuff,
12:41
like following a particular user.
12:43
You could make a user page, so we could have slash users,
12:47
and I could go to a particular, let's say CatFreak47,
12:51
to see all of CatFreak47's tweets.
12:53
I could follow CatFreak47.
12:56
There's a lot more that we can do.
12:58
We could add in some simple validation
13:00
to make sure our tweet is not longer
13:01
than what is it on Twitter, 140 characters, right?
13:05
So we could add some of that in styling.
13:09
What else?
13:10
Hashtags, being able to view by hashtags.
13:13
So I could view all tweets that have the hashtag
13:15
of cats or something.
13:17
There's a lot more that we could add on.
13:19
But really the goal was just to demonstrate authentication
13:22
and some simple authorization where we have
13:25
one relationship really between the user and tweets.
13:29
Coming up, you will have a more involved exercise
13:31
that also involves Twitter.
13:33
It involves authentication, authorization.
13:35
We've got multiple models, multiple views.
13:38
You'll have to do quite a bit of work, but it's a fun one.
13:41
So that's coming up next.
13:42
Well, not right after this,
13:43
we've got a bit more to talk about with Flask,
13:45
but it is coming up soon.
13:46
So look forward to that.
13:47
And stick around if you want to see me
13:48
clean things up a little bit,
13:50
maybe add some styles, but I won't do much.
13:53
That's next.
13:54
(upbeat music)
