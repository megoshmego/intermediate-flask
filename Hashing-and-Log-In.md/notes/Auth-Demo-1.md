0:00
(upbeat music)
0:05
- [Instructor] All right.
0:05
So let's go ahead and try implementing what we just learned
0:08
about authentication and log in and the session, bcrypt
0:13
all of that stuff in a simple example website
0:16
but rather than just showing you the slides.
0:18
I'll actually go through the basic steps of the process.
0:22
So I have a app I've already started,
0:24
so I don't, I don't want this to take forever
0:27
where I have to install every dependency
0:28
and set up my template and a base template
0:31
and my models file.
0:33
So I've already done some stuff.
0:35
My app.py is pretty much empty
0:38
except I do have a single route the root route
0:42
and it just renders index at HTML
0:45
and that just has a single h1.
0:47
The name of our app is going to be Stupid Twitter
0:50
will allow users to make tweets
0:52
which is just going to be a piece of text that we display.
0:55
So we're not gonna have any of the real features
0:57
of Twitter except that you can make a tweet
0:59
but everyone will be able to see them when they're signed in
1:02
but only certain people will be able
1:03
to create them or delete them.
1:06
Also, I am using a base template.
1:08
I've included bootstrap.
1:10
I'm using a themed version from https://bootswatch.com.
1:13
So I'm getting some nice colors
1:14
without having to actually customize it myself.
1:17
I have a navbar up top
1:18
and the navbar right now has a login and sign up link
1:21
and they're just always showing up.
1:23
Also, I am displaying my flash messages here.
1:26
So if I did have anything to flash to a user
1:29
it would show up here
1:30
and then I have my content block here
1:32
so that I can insert content from my child's templates.
1:36
So we're extending base HTML
1:38
and that's pretty much it at this point
1:41
I have installed most of the things we'll need.
1:43
So I have the debug toolbar.
1:44
I have what the form, SQLAlchemy.
1:48
What else is here?
1:50
I think that's pretty much it bcrypt
1:52
and I'll all the basics.
1:54
Flask obviously Jinja all that stuff is here.
1:57
All right.
1:58
So what I wanna do is start by making my user model
2:02
by the way, I need to set up a database.
2:04
I'm just calling this auth_demo.
2:06
I should connect my db and create all
2:10
and I'll define my user here.
2:12
So class user, very simple model.
2:14
It's just going to have ID, username, and password.
2:18
So class user which inherits from db.model.
2:23
We're going to have an id,
2:25
which is db.Column
2:27
and that will be an integer
2:29
primary key is true
2:32
and autoincrement is also true.
2:36
Then I'll have my username,
2:40
which is a db.Column.
2:42
This one is text
2:44
and it can not be empty
2:47
and it has to be unique.
2:48
So nullable equals false and unique equals true
2:54
and then we have password which is also text
3:00
and also nullable equals false
3:03
but it does not have to be unique.
3:06
Okay, there we go.
3:08
So we've got ID, username, and password.
3:10
We also need to add the table name
3:13
_table name_ = users.
3:19
Great.
3:20
Now we have our model set up.
3:21
Let's go ahead and run, connect db at this point
3:25
and also I wanna make sure in IPython.
3:29
So I'm just going to run my file first of all,
3:30
app.py that I do db.create_all
3:38
and Oh I forgot to make my database
3:40
so I should probably do that.
3:42
So I will run createdb auth_demo.
3:47
Now go back here.
3:49
Run that again.
3:50
All right.
3:51
So hopefully it made our users table
3:53
let's see in our database connect to auth_demo
3:57
and then take a look at users.
4:00
Whoops
4:02
All right we do have the user's table
4:04
and I meant to do deep plus to see the schema.
4:09
I'm a bit zoomed in here
4:10
but we've got ID, username and password.
4:13
They're all required
4:14
but ID is auto incrementing IDs is an integer.
4:17
The other two are text.
4:18
All right.
4:19
So that's good enough for us.
4:21
Let's get out of here.
4:22
Now we need to finish up our user model
4:25
and I'm going to add in our methods for authentication
4:29
and for logging in.
4:30
So for registration and logging in.
4:32
So here is the register method that we talked about
4:35
in the previous two videos ago.
4:37
I need to make sure
4:38
that I import bcrypt from flask bcrypt.
4:42
Of course, you need to install flask bcrypt
4:44
and then we get that method generate password_hash
4:48
and we'll call this on the user class
4:50
because this method is going to create a new user.
4:54
It doesn't actually belong to an instance of the user model
4:57
or the user class.
4:59
So it's a class method which is a pretty common pattern
5:02
when you have a class
5:03
and you wanna generate a new instance of that class
5:06
and you have some special logic
5:07
or constraints in our case our logic
5:09
is that we're actually generating a password
5:11
and storing that password on that new user we're returning.
5:14
So it doesn't really make sense to put that
5:16
as an instance method on a user
5:18
and then we need to make sure
5:20
that we have bcrypt imported from flask B crypt,
5:23
so install that if you haven't
5:26
and then also we need to initialize bcrypt here
5:29
and whatever name we give this
5:31
is the name we need to refer to in our methods.
5:34
All ready and I guess just one more time to explain this.
5:38
We are taking a password in as well as a username
5:42
and that password will be turned into a hash
5:44
thanks to bcrypt.
5:45
It returns that massive string,
5:47
which is a byte string
5:48
and we turn it into a unicode utf8 standard string
5:52
that we can store in our database
5:54
and then that's pretty much it.
5:56
Then we just create that object
5:58
the user instance
6:00
and then we return a new user but we're using class,
6:04
which is just the standard way of doing this
6:06
on a class method
6:08
just like self as passed into an instance method already.
6:12
So let's test it out in IPython
6:15
I'll run my file
6:17
make sure you're importing user into your app.py
6:21
and it should be able to call user.register at this point.
6:23
Let's just see if it auto completes.
6:25
There we go
6:26
and we'll pass into username.
6:28
How about monkey1?
6:33
That sounds like a password.
6:34
How about mrmonkey1
6:39
and then the username will be bananas B a n a n a s l o l
6:46
just like that
6:47
and there we go.
6:48
Well, it looks like it may have worked,
6:51
but we didn't save it to a variable.
6:52
So let's do that.
6:53
We'll call this you
6:56
and then we need to do a db. ...
6:59
maybe we can start by just looking at u.username,
7:01
u.password
7:04
cool
7:05
and then u.id is not going to be there yet.
7:08
It's not in our database.
7:09
So db.session.add(u)
7:12
db.session.commit.
7:18
If we hop over to Postgres
7:18
and do a select star from users,
7:22
hooray, it worked all right.
7:25
So that is our register method.
7:28
Now we can add in the authenticate method
7:30
and then we can start using them in our application.
7:33
So here is our authenticate method.
7:36
It takes a username and a password as well
7:38
and it's going to start by taking that username
7:40
and trying to find a user with a username.
7:44
and if it doesn't find one
7:45
then this part short circuits,
7:47
because it starts with if u
7:49
and u will be the found user if no user was found,
7:53
if u is none then we return false
7:56
because we can't authenticate u
7:57
If we can't even find that username
7:59
then if we do find the username
8:01
then we call bcrypt.check_password_hash.
8:04
We pass in the database password.
8:06
So this thing right here
8:10
and whatever the user entered into a form
8:12
we don't have the form yet.
8:13
So we'll just pass it in manually to verify that it works
8:17
and we returned that user if the password is correct
8:21
if it's a match once bcrypt hashes the past in password
8:25
and compares it to what we passed in from the database.
8:29
So let's try it go over to IPython here.
8:33
I'm gonna quit,
8:36
run my file.
8:39
Where are you?
8:40
And then user.authenticates
8:45
and then we're going pass in.
8:47
What do we want to pass in the username?
8:49
Which I already forgot.
8:50
I think it was just mrmonkey right
8:53
and then the password was bananaslol.
8:56
I hope.
8:57
Oh, so that's false.
8:59
My memory is terrible.
9:00
Mrmonkey1,
9:02
I was very close.
9:04
All right.
9:04
Well, you can see that it is working.
9:06
We pass an invalid username
9:08
and now when we pass in the correct user,
9:11
a username that exists
9:12
and the correct corresponding password
9:14
we get back user with id of one
9:17
that is the only user we have at the moment
9:19
but we can assume that it's working great.
9:22
So next, what I'd like to do is implement our forms
9:25
and the routes to actually sign up or register and login.
9:29
(upbeat music)
