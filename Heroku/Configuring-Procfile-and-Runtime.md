Would you please evaluate the transcript I provide for its key terms, ideas, concepts and their defintions. Would you also please include the video title “Configuring Profile and Runtime", the subsection title "Heroku", and the section title "Intermediate Flask"?

0:00
(light music)
0:04
- [Instructor] So next step,
0:05
we're going to install a new server
0:07
that we want to use for our app only in production.
0:10
The server we've been using out of the box with Flask
0:12
is for development, and it's just not as efficient.
0:16
It's not a server that is production ready.
0:19
So we want to configure our app to
0:22
use a production ready server on Heroku.
0:25
The particular server we'll be using
0:26
technically it's called gunicorn
0:30
for however many years, I've been referring it
0:32
referring to it as gunicorn, but I just Googled it.
0:37
It is definitely pronounced gunicorn.
0:39
So I've just learned that today,
0:41
fortunately, that doesn't impact how we use it.
0:44
We do need to install it.
0:45
So pip install gunicorn.
0:48
I'm gonna do that now.
0:50
Pip install.
0:51
I'm using my virtual environment.
0:53
As you can see here, I have a virtual environment
0:56
and then I'll need to freeze my requirements
0:58
or freeze pip and save to my requirements .txt.
1:02
So pip install gunicorn, just like that.
1:08
Okay, so that finished,
1:10
the next step is to make sure my requirements .txt
1:13
is completely up to date.
1:15
I'm going to have to send my code
1:18
over to Heroku, but I'm not going to include any
1:20
of the virtual environment stuff.
1:22
It's actually in my get ignore file.
1:24
My get ignore is completely ignoring venv.
1:27
And we will be using get
1:28
in order to send our code, or push our code to Heroku.
1:32
So that requirements.txt file is very important.
1:35
Pip freeze, and then requirements.txt.
1:39
Let's just look at it
1:41
make sure we see gunicorn and then all other dependencies.
1:43
So I've got B crypt, Flask B crypt.
1:47
We now need to add something called a Procfile
1:50
with a capital P, a Procfile is going to be used
1:53
by Heroku to determine what command will
1:56
be needed to actually start the server.
1:59
So we can have multiple different apps
2:01
in different languages that we want to deploy to Heroku,
2:04
and they will all start in different ways.
2:07
And the way that our server is going to be started
2:09
is with this line right here, gunicorn app, colon app.
2:14
So web colon, I just said, gunicorn,
2:17
gunicorn app colon app.
2:20
This is how you start up the gunicorn server.
2:23
If we were pushing a Ruby app made with rails,
2:25
we would have a different
2:26
command that we want Heroku to run.
2:29
And we put that in the Procfile.
2:31
If we were using node
2:32
and we had an express app, we have a different command here
2:35
but for our Python app, when we're using gunicorn
2:38
as our server, we'll just run this line
2:41
and we need to put it in a file called Procfile capital P.
2:45
There is no extension.
2:46
It's not .txt.
2:48
It's not .py it's just Procfile.
2:51
And we'll put this in the root of our directory.
2:54
So in the same place where our app .py is,
2:57
there we go, make sure it shows up
3:00
and let's take a look at it.
3:02
Cat Procfile.
3:04
Okay, we're in business there.
3:07
Now we have another configuration file called runtime.
3:10
And this one is a .txt file.
3:13
This is how we can tell Heroku exactly
3:15
what version of Python we want to use.
3:17
So we want to figure out exactly what version we're using
3:21
which you could just type Python.
3:23
I am in the virtual environment.
3:25
So I'm not going to do Python three, but just Python.
3:27
I can see I'm using 3.7.2.
3:30
If you're using something different, just take note.
3:32
And then in runtime.txt
3:34
we specify the exact version that we want Heroku to use.
3:38
So if you were writing a Python two app, for some reason
3:41
we need to make sure Heroku knows that
3:43
and it's not going to try and run it with Python three.
3:47
All right.
3:48
So now I've got that file.
3:49
Runtime.txt.
3:51
Let's take a look.
3:53
And it has Python 3.7.2 in there.
3:56
Okay, so I'm gonna stop here.
3:57
We have some basic configuration done.
4:00
These are files that Heroku is going to be looking for.
4:03
We also installed gunicorn.
4:05
We froze our requirements into requirements.txt,
4:09
next we're going to actually create our Heroku app
4:12
and push our code up.
4:13
But that won't be the end of the story.
4:15
We still have more to do, but that's coming up next.
4:17
(light music)
