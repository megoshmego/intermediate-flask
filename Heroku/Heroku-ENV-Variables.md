
Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Heroku", the subsection title "Heroku-ENV variables", and the section title "Intermediate Flask"?


0:00
(upbeat music)
0:04
- [Instructor] All right.
0:05
So yes, we're getting an error from Heroku, but don't fear.
0:08
It's pretty common.
0:10
It just happens.
0:11
And it should not be a source of panic, maybe frustration.
0:14
It's always harder to fix things
0:16
when they're taking place remotely.
0:18
But most of the issues you'll run into are pretty common,
0:22
and they're things she'll learn to anticipate.
0:24
So if I want to view the output, the actual errors
0:27
at the moment, I need to go run this command right here
0:31
Heroku logs, dash dash tail.
0:34
So let's clear this output
0:36
Heroku logs, oh boy, dash dash tail.
0:41
And this will go
0:43
and fetch the latest logs from the server on Heroku.
0:49
And you can view whole bunch of stuff.
0:51
But specifically we are interested
0:53
in the last error.
0:54
Looks like it was Heroku slash register
0:58
that caused a problem.
0:59
And it was trying
1:00
to connect to a database.
1:02
SQL alchemy operation could not connect to server
1:05
No such file or directory.
1:07
Is the server running locally
1:08
and accepting connections?
1:10
It's referring to the Postgres server.
1:12
And if we look at my code,
1:13
we go to our app dot PY,
1:15
where we are connecting or specifying our database.
1:17
It's looking for a database called auth demo that exists
1:21
on my machine locally.
1:23
And I have Postgres running the Postgres server.
1:26
It's all installed and up.
1:27
So it works great locally.
1:29
But when I pushed to Heroku,
1:31
it doesn't know that they're supposed to be
1:33
a Postgres database.
1:34
It doesn't know what database to connect to
1:36
even if there was one.
1:38
So that's what we need to do now.
1:40
So anytime you have an error on Heroku,
1:42
you can get more information
1:43
by running Heroku logs, dash dash tail.
1:47
So to set up our database,
1:49
and to set up any other environment variables
1:52
that we want for production, which is very common,
1:55
we have different values
1:56
that we might want to run on Heroku versus locally.
1:59
We can set environment variables like this:
2:03
Heroku config colon set.
2:05
And we can set a secret key on Heroku.
2:08
We can set a Flask environment to be production.
2:11
So if we look at this right now,
2:13
well, we've been running our Flask apps
2:15
in development automatically.
2:17
We added that line to the bash profile.
2:19
So we haven't even been, you know, writing it manually.
2:22
But we can set these environment variables.
2:24
We can also set the secret key on Heroku.
2:28
But then we'll have to modify our code.
2:29
We don't want to hardcode the secret key
2:31
to be ABC one, two three.
2:33
So we'll set one on Heroku using this syntax:
2:36
Heroku config, colon sets.
2:39
So let's do that now.
2:40
I'm going to get out of my Heroku logs.
2:42
Heroku config, colon set.
2:46
And then we'll specify the secret key and Flask ENV.
2:51
So let's just do FlaskENV to start.
2:53
And we want that to be production,
2:56
so that our app is running in production.
2:59
Okay?
3:00
Now, if we look at our config variables,
3:02
so we can just do Heroku config, just like this.
3:08
And we can see FlaskENV is set to production.
3:13
Next we'll set up a secret key.
3:15
You actually want to generate one that is useful,
3:18
not useful, but one that is relatively secure.
3:22
There are guides on the Flask docs and how to set one up.
3:25
I'm just going to go with something short, secret key.
3:28
So I'm going to Heroku config set,
3:31
and then secret underscore key equals I am secret,
3:38
like that.
3:39
Sure. It's not great, but it's better than just never tell.
3:44
And it takes a moment.
3:46
You can see that it's setting a variable
3:48
an environment variable, on Heroku server,
3:50
and restarting my app.
3:52
But my app is still not using these variables.
3:54
The app that I pushed has a hard coded secret key.
3:58
So I need to make sure
3:59
that I change my code here
4:01
to use those new environment variables
4:03
and we'll see how to do that.
4:04
But first let's just verify
4:06
that we now have two environment variables set
4:09
on Heroku server.
4:11
So not on my machine here, not locally
4:13
but I'm asking when I run Heroku config, I'm saying
4:17
okay, go to my Heroku app and get the environment variables
4:20
on that machine and print them out here in my terminal.
4:23
So it's actually making a request.
4:25
There's a lot going on behind the scenes.
4:27
In order to then use these config variables,
4:29
our environment variables on Heroku,
4:32
I can import in my app dot PY,
4:35
or wherever I'm using these environment variables.
4:37
Import a module called OS,
4:38
and there's a method called
4:41
OS dot environ environment dot get.
4:44
And I can ask it to get a secret key if it finds one.
4:49
And on Heroku, it will.
4:50
Otherwise here's a backup value, a default.
4:55
So let's do that now.
4:56
Let's import OS just do that
4:59
in my app dot PY, import OS.
5:03
And we'll have to save and add, and commit these changes.
5:06
And then instead of hard coding secret key
5:08
I'm going to go OS dot environ dot get,
5:13
and then the name of the config variable is secret key.
5:18
And then the default will just be
5:21
I don't know, hello, secret one.
5:24
So if I run this locally right now
5:27
I have not set up a secret key as an environment variable.
5:30
We can just do this, which is mildly hacky.
5:33
It's not a great idea to print your config variables.
5:36
But let's do print app dot config of secret key.
5:41
And we should see hello secret one printed out.
5:45
because we have not set up an environment variable,
5:47
but on Heroku we have.
5:49
So it should be able to find that environment variable
5:51
and use the Heroku value, not hello, secret one.
5:55
So let's run it locally first.
5:57
Where's my terminal?
5:58
Here we go.
6:00
Flask run.
6:01
And there it goes.
6:03
Hello. Secret one is what's printed out.
6:06
Okay.
6:06
So that's the first bit.
6:08
As far as the other environment variable, FlaskENV,
6:12
remember that we've set this up automatically
6:14
and Flask always looks for that environment variable.
6:17
So we're running in development here.
6:19
And we see that it's printed out.
6:21
When we run Flask it is not going to be set to production.
6:24
But on Heroku, we've set that variable,
6:27
and it will run in production.
6:28
We don't actually specify that in the app code.
6:32
We simply set that as an environment variable
6:34
and Flask looks for it.
6:36
So we should be good to go there.
6:37
Next up, we need to talk about our database.
6:39
But first we can add and commit and push our code,
6:43
just to get more practice.
6:44
We did make a change, very small,
6:47
but we imported OS,
6:48
and we set our secret key.
6:50
I'm going to stop printing it.
6:51
Actually, maybe we'll keep that print,
6:55
and see if we can find it on Heroku.
6:57
So let's print out a bunch of stars,
6:59
try and make it easier to find.
7:02
And I think I'll do this actually
7:04
as a separate line
7:07
Like that.
7:08
And then I'll duplicate it a couple of times.
7:10
Let's see if we can find that secret key
7:12
in our server output.
7:14
So I'm going to go to my terminal,
7:15
take a look at get status.
7:17
We changed app dot PY.
7:18
So get add app dot PY get commit.
7:22
We'll just say, add OS for environ variables.
7:29
Okay.
7:30
Then we need to push to our remote, get remote dash V.
7:34
We still have Heroku get push Heroku master,
7:37
assuming that I'm working on the master branch
7:40
and it's going to rebuild our application, hopefully.
7:45
We'll open up the logs, Heroku logs, dash dash tail.
7:50
And there we go.
7:52
We've got our configured environment variable.
7:55
And it's different on Heroku.
7:57
So you still probably want to put
7:59
something stronger than this.
8:00
Read the docs on Flask for their recommendations.
8:03
But we are able to access that environment variable
8:07
we set up on Heroku,
8:08
and then have some different value locally
8:11
in development, or just defaulting to hello secret one.
8:15
Alright, so we'll want to do the same thing
8:17
for our database.
8:18
Once we get a Heroku database set up with Postgres,
8:21
we'll have our local URL,
8:23
and then we'll have a different version
8:25
for production on Heroku.
8:27
That's coming up next.
8:30
(upbeat music)
