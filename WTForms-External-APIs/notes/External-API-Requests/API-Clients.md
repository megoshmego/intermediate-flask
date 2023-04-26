0:00
(gentle music)
0:04
- [Instructor] All right, one more thing about APIs
0:06
on the server side.
0:08
A lot of the popular APIs you may wanna work with,
0:11
actually have wrapper libraries
0:12
which makes it easier to use that API,
0:15
where you can use a standalone library
0:17
that has its own documentation specialized just
0:21
for that one API.
0:23
So there's a Python library for Twitter's API,
0:27
it's called Python-Twitter.
0:30
Some of these are official,
0:31
so they're put out by the actual API company.
0:34
Some of them are just created by random people.
0:37
In order to use Python-Twitter,
0:39
we'll just take a look at usage.
0:41
If we go to their docs here
0:45
and we go to, maybe getting started,
0:48
we have to make our app on the Twitter website, of course.
0:51
We have to register as a developer, get our keys.
0:54
And then we have our consumer API key
0:56
that we need to copy from their website,
0:59
from the dashboard.
1:00
Keep scrolling down.
1:02
And then here is
1:03
how we initialize the client, import twitter.
1:07
And then twitter.Api,
1:08
and then we have to pass in our different keys and tokens
1:11
that we get from the Twitter documentation.
1:14
And then we can start doing things like searching,
1:16
where we have particular methods like GetSearch.
1:20
So we don't have to actually reference the full URL ourself.
1:23
We don't have to go on the docs necessarily
1:26
to find the end points and which ones are GETs and POSTs.
1:30
Instead, the client has different methods
1:33
and models built in where we can simply pass data in
1:37
and instantiate a new direct message,
1:40
and it will actually create a request for us
1:43
and send that request.
1:44
So it's just a wrapper.
1:45
Instead of directly dealing with a request,
1:48
we can use a client to help us.
1:50
Similarly, Twilio, which we just talked about,
1:52
has a client for Python.
1:54
And this is an official client.
1:56
So you import the client from twilio.rest.
1:58
You have to download the client using PIP.
2:01
You set up your token and your ID.
2:04
And then we can just call client.messages.create.
2:08
We never have to send the request with a URL.
2:11
We never have to say requests.post
2:15
and then pass in params
2:16
or pass in our data like we've been doing.
2:20
Instead, it's just an object
2:21
with a method called messages.create,
2:24
and we pass in some information,
2:26
it will send the request for us and handle everything.
2:29
So this is nice
2:31
if the API you're trying
2:32
to work with actually has a wrapper, if it has a client.
2:35
Here's one more.
2:36
This is for Spotify.
2:38
So this is not official, just put out by someone.
2:40
It still has a good amount of stars.
2:42
And you just put in your ID, your secrets,
2:45
and then we can do things like sp.search, just a method.
2:50
Anyway, keep your eye out for these different clients,
2:53
for whatever you're using.
2:54
Most of the big popular APIs have an official client.
2:58
And a lot of them,
2:59
if they don't, will have a third party client for Python,
3:02
There's also clients for Ruby.
3:04
There's JavaScript clients and Java and all that stuff.
3:08
And if not, then you'll just have to make your API calls,
3:10
like we've been doing.
3:11
You just make a request.
3:13
The docs will cover everything you need to know
3:14
or they should at least.
3:16
And have a good time playing around with some of these.
3:18
(gentle music)