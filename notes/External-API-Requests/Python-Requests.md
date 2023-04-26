0:00
(upbeat music)
0:04
- [Tutor] Next up,
0:05
we'll learn how to make requests via Python.
0:08
So it doesn't have to be in a flask app
0:09
we'll start with a simple .py file.
0:12
No flask , no server
0:14
we're just making a request from Python.
0:16
And the tool we're going to use is just a library
0:19
called requests.
0:20
So we'll install that and use it in just a moment.
0:23
But let's start with the API
0:25
that we're going to play around with.
0:26
So the iTunes API
0:28
is I think it's just called the iTunes Store API,
0:31
It's a way of searching for pretty much anything
0:34
on the iTunes Store.
0:35
We've got books, movies, TV shows,
0:37
podcasts, songs, music videos,
0:40
I think there's quite a few other things.
0:42
You can click on this link.
0:44
It responds in JSON.
0:46
They have some documentation with example searches.
0:50
So you can search for anything put out by Jack Johnson,
0:54
by adding search term equals Jack Johnson.
0:58
That includes movies, podcasts, music, music videos,
1:00
audio books, short films and TV shows.
1:03
But we can also specify a limit of 25.
1:06
We can specify things like only music videos
1:09
using entity or country to set it to Canada.
1:13
We also can look up.
1:15
So there's a Search API and a look up API.
1:17
The look up API gives us information
1:20
about one particular thing based off of an ID,
1:23
an artist ID, UPC , I'm not even sure what that is.
1:27
Universal, I have no idea, AMG artists IDs, video IDs.
1:33
So we've got two different uses I guess.
1:36
We've got search and look up.
1:38
We're just gonna focus on search to start.
1:41
So if we just take one of these
1:44
if we limit to 25, we're gonna get a lot of JSON.
1:47
You'll see that we get quite a bit of stuff.
1:51
So to request the API without Python for a moment,
1:54
I could use curl, so we'll try that.
1:57
Curl and then I'll just paste in this URL
2:00
itunes.apple.com/search? for the query string,
2:04
term is Jack Johnson,
2:05
we do need a plus because, we can't have a space in the URL,
2:09
and limit equals 25.
2:11
Here we go.
2:13
Scroll way up. There's a lot of JSON here.
2:15
It's not gonna be formatted nicely.
2:19
And we'll see that we have 25 result Count.
2:23
And then results is a list.
2:25
And we've got things like a song called what is it?
2:30
The album is In Between Dreams,
2:32
the track name is Better Together,
2:36
yeah, you can see there's a lot of stuffs.
2:38
Music from Curious George,
2:39
I know Jack Johnson did this soundtrack for that.
2:43
Anyway, we won't spend too much time going over this.
2:45
The point is that we can make an API call from curl.
2:49
I can also make it from a GUI tool like insomnia,
2:53
or this tool called rested.
2:54
Just put the URL in here, say GET request.
2:57
And I will send this, if I can find the Send button.
3:01
Am I there we go.
3:04
Here we are, we've got our response body.
3:07
And I think I can specify to format it as JSON.
3:10
I don't know if I can zoom in
3:12
doesn't want me to zoom in.
3:13
But you'll see we get a lot of results.
3:15
So just a different place to make that result.
3:19
So this is an application, this rested GUI.
3:22
I'm not sure what it's written in.
3:24
It could be a Swift app, it could be Objective-C,
3:28
it could be technically a Python app
3:31
that's been wrapped up to work on a Mac.
3:34
It could be a C application.
3:36
But whatever language it is,
3:37
it's making a request behind the scenes
3:40
in some programming language, getting responses back,
3:43
once I hit send request, it sends a request off,
3:46
gets data back and then displays it for me.
3:48
So it's not a browser, but it's still making a request.
3:51
And to do this in Python,
3:52
we'll be using this tool called requests.
3:55
So the first thing we'll do is install
3:57
requests pip install requests.
4:01
So I'm gonna start
4:02
I guess I should just do my venv, -m venv venv.
4:10
Always takes a second,
4:12
and then source venv/bin/activate
4:19
okay, pip install requests.
4:24
So there we go. You could just install this globally,
4:28
but it's always best practice to use a virtual environment,
4:31
but for such a small demo, doesn't really matter.
4:34
And then I guess while I'm trying to do this the right way,
4:38
we'll do a pip freeze into a requirements.txt file.
4:45
Already, so let's just see what's in there.
4:48
And we've got requests, and then it has some dependencies.
4:52
Now let's talk about how we use this tool.
4:54
It's very, very similar to things like axios,
4:57
although it just not JavaScript.
4:59
But axios is a library
5:00
that helps us make requests very easily in JavaScript.
5:04
In Python we have requests.
5:06
Which is a library that helps us make requests
5:08
easily in Python.
5:10
So there's a method called get.
5:11
We will need to import requests of course, request.get url
5:16
so we can specify the URL
5:17
and then optional parameters.
5:20
So here's an example, https:itunes.apple.com/search.
5:25
And instead of putting the entire query string here,
5:28
I can add in params.
5:30
And this is a get request to those params
5:32
are turned into a query string,
5:33
and automatically formatted correctly.
5:35
So a space will be converted into a URL safe space,
5:39
and then we can just print the response we get,
5:42
specifically the .json result.
5:45
So the response we get back is an object,
5:48
and it has a text field
5:49
just to get the text of the response.
5:51
It has a status code attributes,
5:52
and most of what we want will be JSON data.
5:56
And if we call .json,
5:57
it will convert that JSON information
5:59
to a Python dictionary.
6:02
Remember that JSON, JavaScript, Object Notation
6:05
is not just specific to JavaScript,
6:07
it's a very, very common format
6:09
for these API's in today's world.
6:11
So Python is close. It kind of matches with JSON
6:17
but it's not a perfect match.
6:19
So .json will convert that JSON string
6:22
into an actual Python dictionary and we can use that.
6:26
So let's try it.
6:27
We'll start in our file by importing requests.
6:31
And here's a URL that we could request.
6:34
I could just start by requesting that entire thing.
6:36
So requests.gets,
6:39
and then I need a string just like that
6:41
and I'll save this to a variable we'll call it res.
6:45
And why don't I just run this from ipython
6:47
so we can see what res looks like.
6:49
So in my terminal here, ipython,
6:53
%run, I think I called this itunes.py.
6:57
And let's look at res.
6:58
It's a response object.
7:00
If we do a dir on res,
7:03
it has a bunch of methods and attributes.
7:06
We can look at res.status_code.
7:10
It's 200. That's good news.
7:12
res.txt is that entire string
7:16
that we got back from the API, is a lot.
7:19
But it's not an object or it's not a dictionary
7:22
or anything that we can work with in Python.
7:24
It's just I mean, I guess we can work with the string.
7:26
But we're not gonna be able to ask for the third result.
7:30
It's just one big string.
7:31
But if I call res.json,
7:35
now I get a dictionary, one big dictionary.
7:39
And in that dictionary oh, this is a pain.
7:41
I should probably limit the number of results next time.
7:45
Oh boy! Okay, here it is.
7:48
We have a result Count of 25 and then results is a list.
7:53
So I could do something like .json
7:56
and save that to a variable.
7:58
We'll call this data.
8:01
Let's look at data and then do data of results.
8:07
And then let's just take the fourth result index of three.
8:11
And this is the fourth result, right there.
8:14
It's a bit more manageable.
8:15
It's a song by Jack Johnson In Between Dreams,
8:19
Bonus Track Version is the collection,
8:21
the name of the song is Sitting, Waiting, wishing.
8:26
The censored name, it's not any different.
8:28
But for some songs, it definitely would be different here.
8:31
And what else?
8:33
The price if you want to buy the track,
8:35
the price to buy the entire collection.
8:37
The album is 10 dollars, release dates,
8:39
it's not explicit, the album's not explicit,
8:42
that's collection explicitness.
8:44
The track is not explicit.
8:46
Track Count, track number, the time in milliseconds
8:50
is streamable, is true and primary genre is rock.
8:55
I don't know about that for Jack Johnson.
8:56
But we're getting data and we've narrowed it down
8:59
just to look at one of those particular tracks.
9:02
So instead of our Python app,
9:04
if we get an app, it's a bit of a overstatement here.
9:07
But if we wanted to work with this data,
9:09
we would just save a variable.
9:11
We'll call it data, equals res.json.
9:17
And then we could do something.
9:18
How about for, let's go with results in data of results.
9:28
Remember that data includes a couple of things up top,
9:32
I'm not gonna scroll.
9:33
But it's this dictionary that has like number of results,
9:38
set to 25 and then actually has the results as a list.
9:42
This is what we want, results.
9:45
So for results in data results, let's print.
9:49
What should we print?
9:52
Each results? Track name, or kind?
9:58
Yeah, maybe we'll do kind and track name.
10:02
I don't know if everything even has a track name.
10:05
For example, does an audio book have a track name?
10:08
I don't think so.
10:09
So we're getting audio books, movies, music videos.
10:12
So let's just print out collection name,
10:15
and we'll try track name.
10:17
So print results of and then track name,
10:24
and collection name.
10:27
We'll see if this works.
10:29
Again, I'm not positive
10:30
if everything actually has a track name and collection name.
10:33
So let's run this file.
10:35
Get out of here. Quit, clear pythonitunes.py.
10:42
Okay, it looks like it worked.
10:44
It's not very clear what is what
10:45
but we've got the track name first.
10:48
Yeah, Better Together In Between Dreams.
10:51
Banana Pancakes, In Between Dreams,
10:53
Upside Down, Jack Johnson and Friends from Curious George
10:58
Constellations, Situations, In Between Dreams.
11:01
So we're getting our data.
11:02
However, instead of hard coding this string in here,
11:05
if we wanted to change the URL
11:08
or the query string rather,
11:09
so that we could have a dynamic query
11:12
the term or a dynamic limit,
11:15
we can instead pass in params, as we've seen.
11:18
So I'll just leave the base URL like this with a URL.
11:23
And afterwards, we go back to the slides here,
11:27
we can pass in our params.
11:30
So the URL goes first
11:32
and then a keyword argument for params,
11:34
key value pairs in a dictionary.
11:38
So let's do that.
11:39
Params equals and then we just have to match
11:41
what the API wants.
11:43
But what's great about this,
11:45
is that I can do things like jack johnson with a space,
11:49
I could have limits set to a number like five,
11:55
that is not a string.
11:57
This is not a valid string for a URL.
11:59
But requests is going to turn this
12:01
into a valid query string, added on to the end of this
12:04
and then make the request.
12:06
Make sure I have term not terms.
12:09
And now we're getting our five results.
12:13
Of course, this could be a variable here.
12:15
So we could call this term.
12:18
And then pretend this is coming from a user term
12:21
is I don't know, let's say
12:23
somebody is searching for Madonna.
12:29
And now we're getting Like a Prayer,
12:30
Material Girl, Like a Virgin, Virgin wow! Like a Virgin,
12:35
True Blue, Holiday, okay.
12:37
So that's pretty much it for making a get request.
12:39
Obviously, the tricky part of all of this
12:42
is not making the request.
12:43
Usually, that's pretty straightforward.
12:45
It's doing something useful or interesting with the results,
12:49
which we're not doing.
12:50
We're just printing it out.
12:51
So that's where the real skill and creativity comes in.
12:53
What do you do once you have the data back?
12:56
Simply connecting to an API is not that bad.
12:58
(upbeat music)
