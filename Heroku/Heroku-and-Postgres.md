Would you please evaluate the transcript I provide for its key terms, ideas, concepts and their defintions. Would you also please include the video title "Heroku and Postgres", the subsection title "Heroku", and the section title "Intermediate Flask"?


and connect our application to that database
0:12
rather than trying to have our app connect
0:14
to auth demo, which does not exist.
0:17
Nevermind the fact that there is no Postgres servers,
0:19
there is no Postgres database on Heroku at the moment.
0:22
So we need to tackle that first.
0:24
Before that, I just wanna show you
0:26
if you do go to your Heroku dashboard,
0:28
you go to the website, heroku. what is it?
0:31
heroku.com I guess, probably very obvious.
0:34
And if you're logged in, you click on your profile
0:36
or your dashboard, it will take you here.
0:37
You can see the apps that you have.
0:40
There is a limit for free plans.
0:42
I think it's five apps,
0:43
but we can see a couple of different things
0:45
that sometimes are useful.
0:47
You can view a log of the most recent build.
0:51
So that's what was printed out.
0:52
We can see the different things that were installed,
0:54
the versions if you ever need to find that,
0:56
but you can also see things like usage of your app.
1:00
You can see things around config variables,
1:04
and you can actually set them here
1:05
if you prefer to do it in the browser
1:08
rather than the terminal,
1:10
we have a way to delete our app obviously.
1:12
You can change ownership.
1:14
You also can configure a custom domain.
1:16
So at the moment, the domain we get is just set up for us.
1:19
It's the name of the app called
1:21
authdemo2.heroku app.com/in this case,
1:24
my route is register, but you can configure that
1:27
to be whatever you want if you buy a domain name,
1:30
if you all ready have one, you can configure things
1:32
through your dashboard.
1:34
All right, so next we need to get a Postgres database going.
1:38
And this is relatively simple, thankfully,
1:41
there's a nice command we can run
1:43
called heroku addons:create heroku postgresql hobby-dev.
1:49
So Heroku Add-ons is a command,
1:51
well technically Heroku Add-ons creates is a command
1:54
that we can use to create different add-ons
1:56
to an individual Heroku app.
1:58
So add-ons, if we, somewhere on here,
2:01
we can see a list of add-ons under Products platforms.
2:06
Now, where is it?
2:07
Marketplace, here we go, add-ons.
2:10
There's a bunch of different add-ons for your applications.
2:13
They're like nice little pre-packaged things
2:14
that are pretty straightforward to install.
2:17
If you're trying to use MongoDB,
2:18
if you want some fancy error handling stuff,
2:22
if you want logging tools to help you log issues,
2:26
and what's going on with your server,
2:28
and your application, tools to send email.
2:31
So these are add-ons that we can install very easily,
2:36
and one of them that we definitely want
2:38
is the Postgres add-on.
2:40
Now, if we look at this commands,
2:42
Heroku Postgres SQL or Postgresql:hobby dev,
2:47
you might think, Oh, that's the name of our database
2:49
or something? No,
2:50
this is the actual command and this is the tier,
2:53
the plan that we're using,
2:55
there are multiple plans for Heroku postgres,
2:59
hobby dev is the free one.
3:00
It has restrictions on the number of rows and the amount
3:03
of RAM, the speed of things and how long it will take.
3:07
There are different tiers.
3:08
For example, you pay nine bucks a month,
3:10
you get 10 million rows.
3:12
If you pay $12,000 a month,
3:16
you get no row limit, three terabytes storage capacity,
3:20
488 gigabytes of RAM.
3:23
So there's these different tiers,
3:24
but we're sticking with the free stuff for now.
3:26
If you are at a point where you have enough users
3:29
or enough data where you need to pay for something,
3:32
that's probably a good sign, you're doing something right,
3:35
and it's pretty easy to upgrade,
3:36
but you will need a credit card of course,
3:38
right now we don't have a credit card assigned
3:40
or included with our account details.
3:42
So we want hobby dev.
3:43
I just wanted to clear that up,
3:45
that it is not the name of a database.
3:47
I've seen some students replace this with, you know, my app.
3:50
Now, that is not what we do.
3:52
That is exactly as it should be in the command
3:56
and Heroku is going to you install Postgres
3:59
and automatically set up a database URL for us.
4:02
And we should be able to see it once we run this command.
4:05
So I'll stop the Postgres logs or the Heroku logs,
4:08
and I'll paste in this command,
4:12
creating Heroku Postgres hobby dev on my app.
4:16
Colt auth demo 2
4:18
Okay, database has been created and is available.
4:20
It's empty.
4:22
We can transfer it for upgrading data
4:25
from another database using PG copy.
4:27
All right, and it created database URL
4:31
set to Postgresql corrugated 50390.
4:36
So we can also just do heroku config and it has set
4:41
an environment variable called database URL,
4:43
check out that massive database URL.
4:46
We don't wanna hard code that into our application.
4:48
It could change in the future.
4:50
So we use an environment variable it's all ready been set up
4:53
for us by Heroku can also go to my dashboard
4:56
and view those environment variables.
4:58
I think it needs to refresh to get that latest change
5:02
reveal, config, VARs, and never go database URL.
5:05
So we're not going to put that URL directly in our app.
5:08
Instead, we'll do the exact same thing
5:11
that we've done before import os
5:13
and then app.config.
5:15
We're going to set the SQLALCHEMY database URI
5:18
to be os.environ.get database URL.
5:23
So if that exists,
5:24
which right now, it only exists on Heroku in production.
5:27
It's not on our local machine.
5:29
It's only on Heroku, use that
5:31
otherwise set it to whatever we want.
5:33
In my case, it's called auth demo I believe.
5:38
So let's see.
5:39
Where are we setting that?
5:39
I'm gonna get rid of this print right here.
5:42
SQLALCHEMY database URI.
5:44
This will be my default,
5:46
but I'm going to change it to os.environ.get.
5:49
And then the name is,
5:52
I think it's just database always good to double check
5:55
DATABASE_URL, in all caps and then comma.
6:01
Our default value will be this string right there,
6:06
and then close that like that.
6:09
Okay, so hopefully this will all work out.
6:12
when we push this code up,
6:14
we'll be using this database URL.
6:16
That is an environment variable.
6:18
It looks like this right here or like this right here.
6:21
It was set up automatically for us.
6:23
We did not actually configure this URL.
6:26
We just asked Heroku to create a Heroku Postgres instance
6:29
installed Postgres, it gives us a URL automatically,
6:33
and we just use that.
6:35
And if we're in our local development mode,
6:37
we still want to use auth demo.
6:39
So let's add in commit this change.
6:42
First, we can just try running our server locally,
6:44
flask run,
6:46
and make sure that we can still connect to that database.
6:48
If we go to local host 5,000 I'll log in, it still works.
6:53
We're connecting to auth demo.
6:55
And I have the data that was in there before,
6:58
because it did not find this database URL
7:01
as an environment variable.
7:03
But now if I add in commit and push to Heroku,
7:05
so get status, get add app.py get commit -m
7:12
we'll go with add Heroku Postgres URL.
7:18
Okay, and then git push heroku master.
7:22
I'm working on the master branch.
7:24
So I'm pushing that up, it will take a moment
7:28
and we'll rebuild the entire app.
7:31
And depending on how long this takes, I may edit this out.
7:35
All right, it should be good to go now.
7:38
It doesn't mean our app won't have any errors,
7:40
but the database should be created and it should be
7:43
connecting to that database.
7:45
So if I refresh my app, I try and sign up.
7:48
I'll put in some username and a password,
7:50
just one, two, three, so I can remember it.
7:53
And Oh no, we get an error again.
7:55
Remember we made our database
7:57
and hopefully that isn't the error.
7:59
It should be connecting,
8:00
but we still haven't actually created the tables.
8:03
So let's see what's going on.
8:04
Let's do our heroku logs -- tail.
8:10
And here we are.
8:10
So it is able to connect.
8:12
That's great. We're getting a different error,
8:14
insert into users
8:16
and it's gonna tell us somewhere,
8:18
something about users, not existing, no relation.
8:21
Okay, here we go.
8:22
Relation users does not exist.
8:24
There's no users table.
8:26
So normally what we've done locally at least
8:29
is have a seed file and then we call
8:32
db.drop all, db.create all.
8:34
And then if you want to seed some information,
8:37
whatever you have,
8:38
let's say you want to make some dummy users
8:39
or you wanna make some tweets
8:41
or something that will be seated into the database.
8:44
You would put it in here, but at a bare minimum,
8:47
we need to make our tables, db.create all.
8:50
Usually we've been running that from IP Python,
8:53
if we're just typing at once, but we do it from a seed file.
8:56
And that's what we'll see in the next video,
8:58
how we can actually run a single file,
9:01
how we can run commands on Heroku,
9:03
just like we would locally to do something like seed
9:06
our database because at the moment our tables don't exist.
9:09
(upbeat music)
