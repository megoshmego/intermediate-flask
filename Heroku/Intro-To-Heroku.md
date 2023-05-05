Would you please evaluate the transcript I provide for its key terms, ideas, concepts and their defintions. Would you also please include the video title “Intro to Heroku", the subsection title "Heroku", and the section title "Intermediate Flask"?


0:00
(upbeat music)
0:04
- [Speaker] All right, so next up,
0:05
we're gonna talk about deploying our Flask applications.
0:08
Right now, everything's running on local host,
0:11
we are not sharing these with people online,
0:13
we're not deploying them,
0:15
actually hosting them somewhere that anybody can access.
0:18
And that's a really important thing
0:19
that we wanna be able to do.
0:21
So there's lots of ways of deploying lots of services
0:24
that you can use to host your application.
0:26
One that we're gonna use for now is called Heroku.
0:29
Heroku, is a really popular tool.
0:33
It supports all sorts of different languages,
0:35
you can use it to host a Python app like we are,
0:38
you can host a Node app on there,
0:39
you can host a Ruby on Rails app.
0:42
It makes it relatively easy.
0:44
I should warn you, first up front,
0:46
something is going to go wrong,
0:48
on pretty much every application you're trying to deploy.
0:51
It's just part of the,
0:52
that's the nature of deploying.
0:54
What we're trying to do is take an application
0:56
that we have running locally on our machine,
0:58
configure it for production,
1:00
and then install it
1:02
or send it to one of Heroku's servers,
1:05
and have it work on Heroku server
1:08
and respond to requests and do everything we want.
1:11
But it's kind of this difficult process
1:13
because we are installing it
1:14
or sending it to a different server,
1:17
we need to be able to make sure,
1:18
our database is correctly configured on Heroku.
1:22
We need to make sure all the dependencies are installed
1:25
and available in the correct versions on Heroku.
1:28
There are other things we need to configure,
1:29
like the secret key for our Flask application
1:32
that we want to configure on Heroku.
1:35
So it is somewhat involved.
1:37
However, Heroku still makes it a lot easier
1:39
than trying to do this with some other tools.
1:42
Just be prepared for something to go wrong
1:44
and don't panic.
1:46
We'll talk about how we can try and fix things,
1:48
and common things that may go wrong.
1:50
Okay, so what I'm going to do is deploy this application
1:54
that we've made,
1:55
it's very simple, it really doesn't have much going on.
1:58
You can log in and out.
2:00
We're using a database,
2:01
we have SQLAlchemy,
2:03
we've got WTForms,
2:04
I've got bcrypt, so that we can log in.
2:07
I can create Tweets,
2:08
and they're associated with my user.
2:10
So I think I was DogFan3.
2:12
I can delete them if I created them,
2:14
and I can log out and sign up and all that stuff.
2:18
Alright, so I have it running on localhost, of course,
2:21
what we need to do next is figure out
2:23
how we get this on Heroku.
2:25
All right, so let's talk a little bit more about Heroku.
2:27
It is a platform as a service.
2:30
It's a company
2:31
where basically their whole product,
2:34
is offering a platform for you to host your applications.
2:37
And they try and make it as easy as possible
2:39
for you to get your applications up on there.
2:41
Now it is a paid product
2:43
that a lot of companies do use.
2:46
And Heroku charges pretty significant amount of money,
2:50
as you scale up and you get a lot more users
2:52
and requests and data and storage.
2:54
But they have a free tier,
2:56
and that's what we'll be working with.
2:57
All you need to do is set up an account.
2:59
And you won't even have to add a credit card.
3:02
So let's start with installing Heroku.
3:06
The first thing we need to do is make sure
3:07
that we have Homebrew installed on your computer.
3:10
So if you don't,
3:12
follow the instructions to install Homebrew.
3:15
You can also just check if it's installed.
3:17
If you go to our terminal here,
3:18
I'll stop my server.
3:20
If you type brew -v,
3:24
if you see something rather than command not found,
3:27
we know we've got Homebrew installed.
3:29
Then the next step, is to sign up for an account on Heroku.
3:33
So click this link, it will take you to Heroku,
3:36
we'll click Sign up.
3:37
I've already done this,
3:38
but you'll need to register with an email and a password.
3:41
I think you need to verify it, the email that is,
3:44
so don't don't register with a fake email.
3:47
And then when that finishes,
3:48
we have one more step
3:49
just to get Heroku installed on our machine.
3:52
The Heroku command line interface.
3:54
So this is why we need Homebrew,
3:56
run this command brew install heroku/brew/heroku.
4:01
This will give us a tool that we can use in our terminal
4:05
to deploy code using special commands.
4:07
We'll get a command called Heroku push.
4:10
We'll get a command that allows us
4:11
to update things on Heroku, on their servers,
4:15
but it's all through the command line.
4:17
So install this, run this command,
4:19
it may take a while just a heads up.
4:22
Last time I did this was a couple months ago,
4:25
on a new machine, it took probably five-ish minutes.
4:29
Maybe it'll be faster for you.
4:30
But don't freak out if it does take a little while.
4:32
And the same goes for installing Homebrew,
4:34
if you don't have it installed already.
4:36
So go through these steps,
4:38
between this video and the next video
4:40
and then we'll talk about
4:41
what we actually need to do to deploy an app.
4:43
Also, I recommend that you keep the handouts open
4:47
when you're deploying.
4:48
You may not want to deploy right along with me,
4:50
at the moment as I'm typing this
4:52
and as you're watching the videos.
4:54
I think it will be easier if you just watch this,
4:56
see how it goes, see what goes wrong
4:58
or what doesn't go wrong.
4:59
And then when you're ready to deploy your own app,
5:02
pull up the handouts, just reference step by step,
5:05
what you need to do.
5:06
Because there are quite a few important steps,
5:08
and there's some syntax we haven't seen before.
5:11
So don't feel like you gotta do it right now
5:13
and memorize it all.
5:14
Ready, run these commands
5:15
and I'll see you in the next video.
5:17
(upbeat music)
