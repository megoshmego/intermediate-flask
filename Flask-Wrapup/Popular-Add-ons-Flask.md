Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Popular Flask Add-ons", the subsection title "Flask-Wrapup", and the section title "Intermediate Flask"?

0:00
(upbeat music)
0:05
- [Instructor] There's one more group of tools
0:06
that we did not cover
0:07
that are definitely worth knowing about.
0:09
I'm calling these popular add-ons.
0:12
So the first one combines two things
0:14
that we've been using already, WTForms and SQLAlchemy.
0:18
At the moment, our forms and our models have nothing
0:22
to do with one another.
0:23
The intersection between them, is when a form is submitted,
0:27
then we call validate on submit,
0:29
and if that's all good, then we go ahead
0:31
and pull each piece of data out of the form,
0:34
and then we'll update
0:35
or create a new model instance based off of that form data.
0:39
So here I'm getting a pet; pet.query using the ID
0:43
from the path, my route definition.
0:46
And then I'm getting my form, using WTForm;
0:49
it's automatically populated with the data,
0:52
and then I pull out name from the form and I save that
0:55
or update the model name.
0:57
Species from the form, I update the model species.
1:01
And I do that for every field.
1:03
Now, one thing I haven't shown you is
1:04
that you actually can do this in one line.
1:07
Form.populate object,
1:09
and then you can pass in a particular instance of a model.
1:13
But this still has no connection
1:15
between the actual pet model and our edit pet form.
1:19
For this to work, you have to make sure
1:21
that you know the form field weight matches a model column
1:26
called weight.
1:27
They have to be exactly the same name.
1:29
You can't have additional data in the form.
1:32
That will screw up this populate object.
1:35
So, another option is to use a tool called, WTForms-Alchemy.
1:40
It combines these two tools,
1:43
and it's really useful
1:44
if you want to generate forms directly based off
1:48
of your SQLAlchemy model.
1:49
So here's an example
1:50
of creating a form using WTForms-Alchemy.
1:55
We create let's say a pet form,
1:58
and all we do is specify for this form the model
2:01
that it should be based off of is our pet model,
2:04
which we're assuming already exists.
2:05
We're importing from models.
2:07
So we don't have to specify.
2:09
There's gotta be a text fields called pet name
2:11
and a integer field called pet age or whatever it is.
2:16
This will create a form for us based entirely off
2:19
of the model.
2:20
If you look at the documentation
2:22
for WTForms-Alchemy, just on the intro, you can get a feel
2:25
for how this works.
2:27
If we have some user model, it has an ID, a name,
2:31
and an email.
2:32
And we have some additional constraints.
2:34
Like the name has a maximum
2:36
of 100 characters, email has a maximum of 255 characters.
2:41
When we define the form, class user form, inherits
2:44
from model form.
2:45
We set model to user. This user class.
2:49
It automatically will generate a form
2:51
that looks just like this.
2:52
If we were to type it ourself, name, is a text field,
2:56
and it already has a data required,
2:58
and has a length validator,
3:01
two different validators; max 100.
3:03
Email is a text field. Validators, data required,
3:06
length, max equals two, five, five.
3:09
So it's pretty smart.
3:10
If it sees nullable false,
3:12
it is going to add a data required validator.
3:16
If it sees things like an ID,
3:19
that is going to auto increment,
3:21
it knows not to add that to the form.
3:23
It's not going to ask a user to enter an ID manually.
3:27
Also, you can learn more
3:28
about how it converts a SQLAlchemy column type
3:31
to a form field.
3:32
So if you have something like a float
3:35
in your SQLAlchemy model, it will make you a float field.
3:39
Other things include validators. This one's really useful.
3:43
One of the most annoying things to do
3:45
in SQLAlchemy without this tool,
3:49
and with WTForms is to create a unique validation,
3:52
so a user can not have a duplicated user name.
3:56
It's not that annoying to create,
3:57
but there's no built-in out of the box, unique validator
4:02
for WTForms, because that relies on data
4:05
that's in our database.
4:06
We could have thousands of usernames or millions.
4:08
But when we combine the two using WTForms-Alchemy,
4:12
it will automatically add a unique validator,
4:14
if that column, whatever's in your model has a unique index.
4:19
So you can read the docs to see how to set this up.
4:21
But anyway, the whole point of this is that
4:23
it makes your life easier, if you are trying
4:25
to create forms using WTForms, based off of models.
4:28
Which is what we want to do a lot of the time.
4:30
And then you can also still create your own forms
4:33
that aren't based off of models if you'd like.
4:35
The reason we did not go over this is really, there's two.
4:39
One, it's just something that I feel like
4:41
at this point you can pick up on your own.
4:43
And I definitely recommend that you look into this tool,
4:45
and you consider using it,
4:46
on some of your upcoming larger projects.
4:49
It can really speed up development.
4:51
But the other important reason we didn't cover it, is that
4:53
it relies on two tools, WTForms and SQLAlchemy,
4:58
that are already somewhat magical,
5:00
and they do a lot for you.
5:01
And then you combine them
5:02
into this one other massive magical tool
5:05
called WTForms-Alchemy.
5:07
And if that was the only thing we showed you,
5:09
and we didn't start first with WTForms and SQLAlchemy
5:12
as their own tools,
5:13
it's really hard to understand what is going on.
5:16
What the form is going on with your application
5:20
and how everything connects,
5:21
and what's magic, and what's not.
5:23
So I recommend you use it,
5:25
but I didn't want to force it upon you, especially not
5:28
as the first introduction to WTForms.
5:32
But I would use it honestly on larger projects,
5:34
and a lot of people do.
5:36
Another add-on is called Flask-Login.
5:39
This will provide a lot of functionality
5:41
around authentication.
5:42
It makes it very, very easy, essentially
5:44
to do what we've already done.
5:46
But we wrote most of the logic.
5:48
We worked with bcrypt.
5:50
We hashed the password.
5:51
We have to set up all the models and everything.
5:53
Flask-Login makes that even easier.
5:56
This is another one of those situations where
5:58
if we had taught you this instead, you wouldn't have
6:01
as solid of an understanding
6:03
of how things actually work, how authentication works
6:05
and what's happening behind the scenes.
6:07
But if we look at a simple example,
6:09
it's pretty straightforward.
6:11
It includes methods like login user, already set up.
6:14
So you don't have to write your own register
6:16
or login methods.
6:18
It has a built an attribute called current user,
6:20
that will just give you information
6:22
about the currently logged in user, the login method
6:25
that we've already talked about, login user.
6:28
You can also specify a duration for how long
6:30
that cookie should remain before it expires.
6:33
There's a logout method already built in.
6:36
There's other things like functions you can use
6:39
to protect your views.
6:40
Login required, is a simple decorator you can add
6:43
between different routes or view functions rather.
6:46
So there's a lot that it does for you.
6:49
It's really just a couple of methods you end up using,
6:51
but it can save you time.
6:53
But if we just led with this, you really wouldn't understand
6:56
what's happening behind the scenes.
6:57
So hopefully you'll forgive me for that.
6:59
It's definitely worth it to know how to implement all
7:02
from scratch.
7:03
But now that you do, there's nothing wrong with resorting
7:06
to using a tool like Flask-Login.
7:08
It's just the other way around is kind of not as good
7:12
from a teaching perspective.
7:13
As attractive as it might be
7:14
to just learn the easy tool, the easy way out
7:17
and get something working as fast as possible,
7:19
it's definitely better for you in the long-term
7:21
to understand what's going on
7:23
in terms of, I mean, just being a solid developer
7:26
and interviewing, having
7:28
that conceptual foundation is important.
7:31
But yes, there is a tool called Flask-Login.
7:33
Nothing wrong with using it.
7:35
There's another add-on called Flask-Mail,
7:37
which you can use to send mail from flask.
7:40
So this is one that's pretty useful.
7:42
Sending mail without a tool
7:43
like this can be somewhat annoying.
7:46
There's a lot that can go wrong,
7:48
and this just makes it easy.
7:51
So, it's an add-on called Flask-Mail.
7:53
Just show you a simple example here
7:55
to send a message once you have Flask-Mail set up.
7:58
You can just go with message,
8:00
and then create it with the actual text.
8:03
A sender, recipient. You can have multiple recipients.
8:07
And then you can call mail.send of message.
8:11
You can do bulk emails. You can even add attachments.
8:14
So if you were trying to implement,
8:16
even something as simple as a reminder email,
8:19
or something devious and annoying,
8:21
like when users sign up for your website,
8:23
and they haven't visited your website
8:25
in 30 days, you could remind them
8:28
if you really wanted to; hopefully a lot
8:30
of them will unsubscribe,
8:32
but if you wanted to you could use a tool like Flask-Mail
8:34
to help you send those emails dynamically based off
8:38
of when a user actually signed in or last signed in,
8:41
and how long it's been.
8:43
So that's the tool, that's worth knowing about.
8:46
Another add-on is called Flask-Admin.
8:49
Flask-Admin helps you very quickly create
8:52
an administrator interface on top of some existing model.
8:55
So it works well with SQLAlchemy.
8:58
Takes pretty little effort
9:00
and it can build you a UI like this here,
9:04
where you don't have to go into your database
9:06
and look at stuff using Postgres and text.
9:09
You can see an actual interface
9:11
to view data based off of a model,
9:13
but also delete things, edit things, create new entities.
9:19
Having to do this yourself, is not that difficult
9:22
but it takes a lot of time.
9:23
You're setting up a full CRUD,
9:25
in this case for a single; what is this?
9:27
A user or post. I think it's a post.
9:30
And then if you had a whole bunch of models
9:32
and you wanted an admin to be able
9:34
to administrate all of them and have access to views
9:37
like this for your user models,
9:40
for your I don't know comments, and subreddits,
9:43
that's a lot of effort to set that up.
9:45
So that's Flask-Admin.
9:47
You can read more about it on the docs.
9:49
And then lastly, this one I saved for the end,
9:52
because it does a whole lot for you.
9:54
And there's good reason that we didn't show it
9:56
to you upfront. It's called Flask-Restless.
10:00
And this will create a RESTFul CRUD API for you, based off
10:05
of SQLAlchemy models.
10:08
So if we go to the docs for this.
10:10
If you wanted to make a RESTFul interface...
10:13
Let's just go to the quick start.
10:14
If you have some model like computer or person,
10:17
and you want to create a RESTFul API based off of
10:21
that model, so that you can create a new computer
10:25
or a new person, you can update one, you can delete one,
10:28
you can view a single one, or you can view all of them,
10:32
all those routes that we've talked about that pattern.
10:34
We spent quite a lot of time discussing it.
10:37
You don't have to define it all yourself
10:38
if you use a tool like this one, Flask-Restless.
10:42
The only line of code...
10:43
I guess there's a couple. You have
10:44
to set up this API manager.
10:46
But then the only line of code to actually make all
10:49
of those routes, and the corresponding view function logic,
10:52
to respond to the correct data, is this right here
10:55
for a single model.
10:57
For the person model, I want full CRUD routes...
11:00
Well, I want get post and delete routes.
11:03
You can configure it and pass in the different HTTP verbs.
11:06
So here we're only making the HTTP methods that are allowed
11:10
for the computer API that it will generate.
11:13
And then that's pretty much it.
11:15
So it does a lot for you. It saves time. Of course,
11:18
if we just showed you this upfront, you wouldn't have
11:21
to understand RESTFul routing and APIs,
11:24
and responding with JSON and everything yourself.
11:27
Why would you? You would just use this.
11:28
But now that you know it,
11:30
to save time, you can definitely use a tool like this.
11:33
You still need to add in your own routes
11:35
for any sort of unique functionality.
11:38
This is just to make your basic RESTFul CRUD API,
11:41
but most apps are not just RESTFul CRUD routes.
11:44
We usually have some other stuff going on.
11:47
Or maybe we have a full RESTFul CRUD back end,
11:49
and then a lot of logic on the front end.
11:52
But this isn't going to make a full application for you.
11:53
It just sets up your end points and it responds
11:56
with the correct information automatically
11:59
by connecting to your model
12:00
and your flask SQLAlchemy database.
12:03
So when you request slash computers, as a get request,
12:06
it's going to go and find all the computers in the database.
12:10
And it knows what your database is,
12:11
it knows what model to use.
12:13
When you try and create one, it knows what model to create,
12:16
and it knows everything.
12:18
So that is Flask-Restless.
12:20
Also useful, but hopefully you understand why we didn't lead
12:24
with this either.
12:25
But now that we've talked
12:26
about these different add-ons, maybe, just maybe there's
12:29
at least one that sounds good to you,
12:31
whether it's, WTForms-Alchemy, Flask-Login, Flask-Mail,
12:35
Flask-Admin, Flask-Restless, these are all very popular,
12:39
and for good reason. They can save you a lot of time.
12:42
So definitely feel free to incorporate them
12:44
in future projects. Inside projects. Read the docs.
12:47
At this point, you understand the underpinnings
12:50
of most of them.
12:51
You understand how to make a RESTFul API.
12:53
You understand how to set up something like this,
12:55
even if it would take you a lot of time.
12:57
I guess mail is an exception.
12:59
You understand authentication.
13:01
You understand WTForms and SQLAlchemy.
13:04
So why not use these add-ons.
13:06
(upbeat music)
