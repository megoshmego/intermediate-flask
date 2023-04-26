Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "What wasn't covered in Flask", the subsection title "What wasn't covered ", and the section title "Intermediate Flask"?

Transcript


0:00
(upbeat music)
0:05
- [Instructor] All right, everyone.
0:06
We have reached the end of the line for our Flask content.
0:10
So we still have a lot left to cover
0:11
around server-side web development
0:13
and web development in general.
0:15
But we are moving away from Flask.
0:17
We will use other tools to fill in those gaps.
0:19
Things like Node and Express.
0:22
So Flask is obviously a great tool.
0:24
It's a great tool to teach this content.
0:26
But it's also a great framework to use.
0:28
What I'd like to do here is just do a quick wrap-up of what
0:32
we've learned in Flask,
0:33
but also what we have not covered.
0:36
There are different things that we just decided
0:37
not to cover for a couple of different reasons.
0:39
And I'll go into that in a bit.
0:41
But let's start with what we did cover.
0:43
So flask is one of many
0:45
web application frameworks for Python,
0:47
but it's one of two most popular alongside Django.
0:51
The main difference we talked about this early on,
0:54
there's a bunch of differences, of course,
0:55
tons of different syntax that's used in Django.
0:59
Different expectations around the names for your functions
1:02
and the files
1:02
and your folder structure.
1:04
But the main difference if you were just gonna pick one
1:07
is that Flask is a lot more flexible
1:10
and gives you a lot more leeway in how you do things.
1:13
But the flip side of that is that Django comes
1:15
with more features
1:16
and more expectations,
1:18
more rigidity out of the box,
1:20
which can help you make an application faster.
1:23
But it's honestly a terrible framework to learn
1:25
as your first server-side framework.
1:28
It can give you a lot of misconceptions
1:30
about how all frameworks work.
1:33
You don't really have to understand what's happening
1:34
behind the scenes,
1:36
Whereas with flask,
1:37
you still need a general understanding
1:38
of the request response cycle.
1:40
What models are, you need to render templates.
1:44
Different stuff that we've covered, sessions.
1:47
You have to understand that in order to build
1:49
an app with Flask,
1:50
and there are things, there are different frameworks
1:53
out there like Django,
1:55
where some of that is just hidden away from you.
1:57
So what we did cover in general was routes,
2:01
Jinja templating, SQLAlchemy and Flask-SQLAlchemy.
2:05
We did talk about SQL in the middle there on its own.
2:08
We talked about testing Flask,
2:10
cookies and sessions,
2:11
creating JSON API's
2:13
and restful API's.
2:14
And then with the forms,
2:16
as well as authentication.
2:19
Setting up user login.
2:20
Almost all of that is going to translate over to
2:23
whatever framework you use
2:24
whether it's Python or not.
2:26
The syntax will be different.
2:27
You won't write tests using unit test.
2:30
You may not use with the forms,
2:32
but you'll use some sort of form generating library.
2:35
If you choose to you don't have to.
2:36
If you implement authentication in Node
2:38
or in Ruby
2:40
or Java,
2:41
you'll most likely end up using bcrypt.
2:44
You could use Argan or Argon,
2:46
but there are libraries, implementation of bcrypt
2:49
in all of the popular languages.
2:51
You'll follow a pretty similar pattern.
2:53
You're not gonna store a password.
2:55
You'll have some database.
2:57
It's probably going to be PostgreSQL in this course,
2:59
but you may end up using something else down the line.
3:02
You usually have a tool like SQLAlchemy.
3:05
So SQLAlchemy is specific to Python
3:07
but there are other very similar tools for JavaScript
3:10
for Node rather.
3:11
For Ruby, for Java,
3:13
for whatever language you're using.
3:15
So a lot of this is pretty universal
3:17
if you just ignore the specific ins and outs of the syntax.
3:21
Now we covered a lot
3:22
but we also left a lot out.
3:24
And there's really two groups of things that we left out.
3:27
One is things we cut for time.
3:29
We have a lot to cover.
3:30
We've already covered more than a lot of in-person
3:32
boot camps we're about to cover.
3:34
And then there's a second group of tools
3:35
we decided not to cover from an educational perspective
3:40
where they might be a shortcut
3:42
or a nice workaround
3:43
or a library that does a ton of work for you.
3:46
And if you use those, if you learn using those shortcuts,
3:49
you're not gonna understand what's happening
3:51
behind the scenes.
3:52
So some of these things we made you do it the hard way
3:55
so that now you can appreciate
3:56
and understand how the easy way works.
3:59
So here's a rough overview of some of the major things we
4:02
didn't cover within Flask.
4:04
First of all,
4:04
Flask comes with a method called url_for
4:06
for that we didn't talk about.
4:08
Basically it helps you create URLs
4:11
and links to URLs based off of your application,
4:15
where you have an id
4:16
or multiple id's in the route.
4:18
What we've been doing is defining a route.
4:20
Let's say users/an ID, an integer ID.
4:24
And then in our templates,
4:26
if we made an anchor tag,
4:27
we just use ginger brackets to actually put a variable
4:31
for an ID directly inside of href
4:34
or if we want it to redirect to that route, we redirect
4:36
and we use an F string
4:37
where we interpolate the user.id.
4:40
And then we would do the same thing
4:42
if we had profiles
4:43
with the user ID
4:44
or warbler/users/user-id.
4:46
By using url_for, you can define a route
4:50
and then all you need to do
4:52
based off of your view function here, user_profile
4:56
is call url_for
4:58
and then the name of that view function.
5:00
And then you set an id like id = user.id.
5:04
And it will automatically set up the correct route to the
5:08
correct path for this href based off of your view function.
5:13
Also, if you want it to redirect,
5:15
url_for('user_profile', id=user.id).
5:20
So definitely, I recommend checking that out,
5:22
reading the docs about url_for.
5:24
Next step, this is a rather a useful tool
5:27
that we haven't covered called Blueprints.
5:30
So blueprints in Flask are kind of like creating many
5:33
applications that you can sum together
5:36
to build one larger application.
5:38
Right now we've been writing all of our code in an app.py.
5:42
I mean, yes, we have some logic,
5:43
probably moved out into our models.
5:45
We have our forms that are separate files.
5:47
We have all the templates separate
5:49
but all of our routes,
5:50
all of that functionality is in a single app.py file.
5:55
Blueprints allow us to break out portions of an application
6:00
into smaller pieces.
6:02
And each piece can have its own models,
6:04
its own forms, tests, views,
6:06
and then we can recombine them to build an application.
6:10
So it's a way of structuring our application.
6:13
It's not just about breaking up code
6:15
into different files or sections,
6:17
but it's also about reuse and modularity.
6:20
There's a pretty cool explanation on Stack Overflow
6:24
that I'll highlight.
6:25
I'll start by saying that the docs,
6:27
the official Flask docs on blueprints
6:28
are kind of confusing in my experience,
6:31
if you're new
6:32
and you're trying to understand it.
6:33
There are some great tutorials.
6:35
There's this one from a website called Hackers and Slackers.
6:39
There is another one from
6:40
a great book called "Explore Flask" about blueprints.
6:44
But I kind of like this explanation from Stack Overflow.
6:48
A blueprint is a template for generating
6:50
a section of a web app.
6:51
You can think of it as a mold.
6:54
You can take the blueprint
6:55
and apply it to your app in several different places.
6:57
Each time you apply it,
6:58
the blueprint will create a new version of it structure in
7:01
the plaster of your app.
7:03
So they have a demonstration of defining a blueprint for
7:06
working with trees.
7:08
It says that any application that deals with trees
7:11
should provide access to its leaves, its roots
7:13
and its rings by year.
7:15
So we have different routes like /leaves, /roots
7:18
/rings slash, /rings by year or with a year id.
7:23
And these are all part of this tree mold blueprint.
7:27
Then further down, here's this example
7:30
where we can use app.register_blueprint
7:32
with that tree mold.
7:34
And then we can create three different imprints
7:36
of that tree mold blueprint,
7:38
where we have /oak, /fir and /ash.
7:42
So this one blueprint,
7:44
this one mold is now being used to define three different
7:48
pieces of our application,
7:49
oak, fir and ash.
7:52
Now that's just one example.
7:53
I'm not gonna go into too much detail here
7:55
because really the point is just that
7:56
we didn't cover blueprints.
7:57
And I definitely recommend checking them out
8:00
especially if you plan on building much larger apps
8:03
with Flask.
8:04
And if you take a look on GitHub at some production
8:07
applications built with flask,
8:09
you'll see that there's not just one large app.py.
8:13
Things might end up looking like this,
8:16
where we have different sections.
8:17
A landing portion of our application has templates.
8:21
It has a static folder.
8:22
It has routes, a logged in portion of the application,
8:25
a charts portion, a dashboard section of the application
8:29
and all of them have their own routes.
8:31
They have their own templates
8:32
and their own static.
8:34
So again, we're not gonna go into it now,
8:36
but I highly recommend you do some research on blueprints.
8:39
This is definitely useful for larger,
8:41
more complicated websites.
8:43
And when I say useful,
8:44
it's more of imperative for larger sites.
8:47
You might lose your mind if you're trying to write
8:49
a large app only in your app.py.
8:52
Another topic in Flask we didn't cover is Signals.
8:56
Signals are relatively easy ways of saying when this one
9:00
thing happens, do this other thing.
9:03
So when I use a registers,
9:04
to send an email or send them a text,
9:06
no matter how they actually end up registering.
9:09
Next up in a separate video,
9:10
I'm gonna talk about the features
9:12
we did not cover in Jinja.
9:15
That's coming up next, it gets its own video.
9:18
(upbeat music)
