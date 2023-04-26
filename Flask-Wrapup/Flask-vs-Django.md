Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Flask vs. Django", the subsection title "What wasn't covered ", and the section title "Intermediate Flask"?

0:00
(soft music)
0:05
- [Man] So that's pretty much it
0:05
for the list of topics,
0:07
at least that I would like you to know about
0:09
and be aware of,
0:10
that we did not cover.
0:11
There are probably unending topics
0:14
that we did not cover.
0:15
But those are the highlights,
0:17
the different add-ons, the Jinja syntax,
0:19
I recommend you take a look at things like URL four.
0:23
Those are worth knowing,
0:24
we're just not gonna spend time to learn them together.
0:27
But that shouldn't stop you at this point.
0:29
Hopefully, you're relatively comfortable
0:30
with the basics of Flask,
0:32
and feel free to level up your skills
0:33
with some of those tools.
0:35
So let's quickly talk about something that I assume
0:38
some of you are wondering about,
0:39
will you actually use Flask on the job?
0:43
Maybe, it's hard to say,
0:45
Flask is popular.
0:47
It's the number one or number two
0:49
most popular Python framework out there,
0:51
at least according to last year's
0:53
developer survey on Stack Overflow.
0:55
And it tends to fluctuate between one and two
0:59
over the last couple years, alongside Django.
1:03
It is popular, it's used by real companies,
1:05
whether they're large or small.
1:07
I know from personal experience,
1:08
some companies use Flask for some of their smaller apps
1:11
on the side,
1:12
still essential to the operations of the company.
1:16
But a lot of developers just really like Flask.
1:19
It's relatively straightforward,
1:21
it helps you, it does a lot of stuff for you,
1:23
but it doesn't just take the wheel.
1:25
And you're not just in the backseat along for the ride,
1:27
like some people would say,
1:29
you are with Django,
1:30
which is something we're about to talk about Django
1:32
in more detail.
1:34
But the point is, it's hard to say,
1:35
if you're going to use it or not,
1:37
you'll be using it at least for one or more projects
1:40
in this course.
1:41
But for us, teaching Flask is really more about
1:44
giving you a foundation for how server frameworks work,
1:47
and web development works,
1:48
and requests and responses,
1:50
templating, routes, authentication, cookies, and sessions,
1:55
all of that stuff is pretty universal.
1:57
And Flask was just the vehicle
1:59
we use to deliver that medicine, I guess.
2:03
And also Flask is a great choice
2:05
just for your own personal projects.
2:07
If you are interviewing and you have a take home
2:09
coding challenge they want you to build,
2:11
some sort of application, I don't know.
2:13
A college basketball bracket application,
2:17
or a clone of some website,
2:20
Flask is a great tool to turn to
2:22
in those situations.
2:23
Now let's wrap up this section by talking about Flask,
2:26
and how it compares to other frameworks.
2:28
So, we'll be talking about a framework called "Express",
2:31
which is a Node.js framework.
2:33
And Flask is actually pretty similar to express,
2:37
they work at the same level of framework Enos,
2:41
the same level of how many rules they have,
2:43
the level of concepts,
2:44
they share a lot of ideas and general beliefs
2:47
about what a framework should be and shouldn't be.
2:49
You can even use Jinja within Express.
2:52
So you could say that Express,
2:54
is kind of like the Flask of Node.js.
2:57
So we'll be learning Express and node in just a bit.
3:01
But now let's talk about the tool
3:03
that is always compared to Flask, which is Django.
3:06
Django and Flask is already mentioned,
3:07
are the number one and number two most popular frameworks
3:10
for web development in Python.
3:12
But they're quite different.
3:14
Django is larger, it's more featureful.
3:18
You could say out of the box,
3:20
it does more, it's more powerful,
3:22
but it's also a lot more opinionated.
3:25
So I'm gonna give you some comparisons of code,
3:28
to make a model in Flask,
3:30
we have something like this with SQLAlchemy.
3:32
Right, we've seen this before.
3:34
In Django, it's pretty similar, right?
3:37
We've got the same pattern.
3:38
Obviously, these dot, dot, dots, aren't real code,
3:41
you got to fill in the blanks there.
3:43
However, Django when we create a foreign key,
3:47
in this case for the owner model,
3:49
it automatically defines a relationship for us,
3:52
and it automatically makes an owner ID column.
3:55
When we're in Flask with SQLAlchemy,
3:57
we have to make that owner ID first,
3:59
then we also have to set up the db.relationship
4:02
with a backref.
4:04
With Django you don't.
4:05
Also, we don't have to create an ID in Django,
4:09
it automatically does that,
4:10
it makes it auto incrementing int.
4:12
In Flask, with SQLAlchemy we do.
4:15
So this is a simple example.
4:17
But it does demonstrate
4:18
that Django does a lot for you.
4:20
And if we had led with this,
4:21
it's another example of why we went with Flask,
4:24
you wouldn't understand what a relationship necessarily is,
4:28
or that we need to have an owner ID column
4:30
like we did in flask.
4:32
This makes us understand how everything is working together.
4:36
We have an owner ID,
4:37
that's just a column,
4:38
it doesn't do anything in terms of SQLAlchemy
4:40
and setting up a connection between tables
4:43
until we create our db.relationship,
4:46
which does not actually have any impact on our schema.
4:49
Postgres doesn't know about this relationship.
4:52
But SQLAlchemy will fill this data in for us
4:55
as we've seen,
4:56
pet.owner will fill in some information about the owner.
4:59
Now here's another example that is a bit more extreme,
5:03
here is our code in Flask
5:05
to set up an edit form,
5:07
and say get in a post route.
5:09
And then we have our view function
5:10
that renders a template with a form.
5:13
And then when the form is submitted,
5:14
it goes to the same exact route
5:16
as a POST request.
5:17
So same path but a POST.
5:18
And then we validate the form,
5:21
we create our model or in this case,
5:22
update, the existing pet.
5:25
And then db.session.commit, we redirect.
5:28
So this is not terribly long.
5:31
And it's important that we understand
5:33
how this all works.
5:34
But in Django, this is the equivalent.
5:37
All you need to set up an edit form,
5:40
and a route to also handle the editing
5:43
and actually update your pet model,
5:45
is this right here.
5:47
So this is what I mean when I say it's opinionated,
5:51
it does a lot more for you out of the box.
5:53
But it can be a pretty bad experience
5:55
to learn how to code and to learn frameworks,
5:58
using a tool like Django,
5:59
because it seems like nothing's...
6:01
It's just completely hidden from view,
6:03
you don't have to understand a single thing
6:05
about models and forms,
6:07
and CSRF tokens, redirecting,
6:10
committing, db.session.commit,
6:12
it's just all hidden away.
6:15
So this is very fast.
6:16
And it's kind of shocking,
6:17
maybe if you haven't seen this before,
6:19
all that we need is this generic.UpdateView.
6:22
It saves a lot of time,
6:23
but it's also magic.
6:27
So then the question is,
6:28
is Django better because of that?
6:31
In some ways, you could argue yes,
6:32
but in a lot of ways you could also argue no.
6:34
For people that enjoy
6:36
or like Django's patterns and opinions,
6:39
then it works great.
6:40
If you can get along with Django,
6:42
you can make apps very quickly,
6:44
if it fits your use case.
6:46
But then there are a lot of times
6:47
where you butt up against the opinions
6:50
and the expectations of a framework like Django,
6:53
it can take a lot longer to learn, definitely.
6:57
But it can be a lot faster to make an app
6:59
until something goes wrong.
7:01
If something is going wrong
7:03
with this one line of code instead of this class here,
7:07
it's a little bit difficult to understand
7:09
where it's going wrong.
7:11
It feels like this magical thing
7:13
that was supposed to be taken care of for you,
7:15
if it's not working,
7:16
it's more intimidating and more challenging
7:18
to actually fix,
7:19
especially if you don't fully understand what's going on.
7:22
At this point, you should have a good understanding,
7:24
and by the end of this course,
7:26
I don't recommend you going into Django right now,
7:29
because we've got a lot left to talk about.
7:31
And we're moving on to node and react.
7:33
But if you do feel like learning Django
7:35
by the end of, say, when you graduate.
7:38
Picking up Django is definitely something
7:40
that you would be equipped enough to do at this point.
7:43
Also, if you do wanna work outside
7:46
of the expectations or break the Django mold,
7:49
it can be a lot harder to modify things
7:51
or to add on certain features
7:53
and just alter how it behaves.
7:56
Versus with Flask, you have tons of flexibility,
7:59
lots of options,
8:00
it does take longer to make an application.
8:03
I mean, you've got to type code,
8:05
what is this, 10 times longer?
8:07
To set up a single edit form and an edit handler.
8:10
But you have complete control over your code,
8:12
and you have to understand how it works.
8:15
With Django you could possibly scrape by
8:17
without really getting what's going on.
8:19
But that's just a bad experience.
8:21
And all of these pros and cons of Django versus Flask,
8:26
are not just coming from me as a teacher, as an educator.
8:29
I hate saying educator, sounds so pretentious.
8:33
But it's not just coming from that perspective
8:35
of teaching new students,
8:36
and why I think Flask is a better way to start out.
8:39
These are also opinions shared
8:41
by a lot of senior experienced developers,
8:44
who are running teams,
8:45
who are deciding what tools to use.
8:47
A lot of people love Django,
8:49
but there's a lot of developers
8:50
who really don't like tools like Django,
8:53
or Ruby and Rails is another example.
8:55
Ruby and Rails and Django are pretty similar
8:57
in their control that they exert
9:00
in their opinions, their beliefs,
9:03
and their patterns that you have to follow.
9:05
They can really help you make an app fast,
9:07
but a lot of developers rebel against that.
9:09
They want more freedom,
9:10
they want something to be lightweight,
9:13
they don't need all of that crazy structure.
9:16
So long story short,
9:16
it's not just me who's saying this.
9:19
But I do like Django if you're wondering.
9:22
If I was just firing some app up
9:24
and I just wanted to make something super quickly,
9:26
I definitely would go with Django.
9:28
But overall, I'd say I prefer Flask.
9:30
But that doesn't really matter what I prefer,
9:32
it's up to you.
9:33
At this point, you only know Flask,
9:34
I would pick up some Django basics,
9:36
maybe follow a tutorial or something
9:38
and roll in a free course in a couple months.
9:40
But for now, let's move on.
9:43
(soft music)
