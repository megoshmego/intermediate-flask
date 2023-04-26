- [Instructor] Next up, we'll do a demo of an API
0:06
that does require a key.
0:08
So the Google Maps API
0:11
that we can use to get geocoded information,
0:14
I've already mentioned this a couple of times,
0:15
geocoding it's when you take a human string,
0:17
like I don't know, San Francisco, California,
0:21
and then you get a latitude and longitude sent back to you
0:24
as well as often other information.
0:27
It's very important
0:27
because if we wanna plot something on a map,
0:29
we can't just tell a map, plot San Francisco,
0:32
although some of them we can.
0:34
Most of them, we need to say,
0:35
make a pin at 37 point blah, blah, blah, comma,
0:39
29 point blah, blah, blah.
0:42
That's not the correct latitude and longitude,
0:45
but the point remains that geocoding
0:47
is a very important skill or not even a skill,
0:49
an important feature in most map based applications.
0:53
So Google Maps has an API for that,
0:55
but you do need to register with a credit card.
0:57
And I didn't want to enforce that as a requirement
1:00
for these videos so we can use MapQuest API.
1:04
It will do the same thing.
1:05
So I'm gonna click, Get your Free API Key.
1:08
Then all we need to do is fill out
1:10
all of the information here.
1:11
I won't do that on camera.
1:13
I already have an API key that I've generated
1:16
that you can use, because there's no credit card associated.
1:21
Really the only limit, at least on the free tier,
1:23
is that you get 15,000 requests per month.
1:26
So if you go past 15,000,
1:28
they're going to stop making those requests work.
1:31
They'll stop responding to them
1:33
and you can add a credit card.
1:34
if you're building a real large application
1:36
that has users and you think it's worth it,
1:39
and you want more than 15,000 transactions,
1:41
you put your credit card in
1:42
and then you can continue to use the API.
1:45
So go through this process if you'd like to follow along,
1:48
because the API key I'm going to use
1:51
may or may not still work for you,
1:52
depending on how many people try and use it as well.
1:56
So once we have registered, we can go to Documentation
2:00
and there's a couple of different APIs
2:02
on the left-hand side.
2:03
So there are SDKs, Software Development Kits,
2:07
which are for creating apps like iOS apps or Android apps,
2:12
or just native map apps.
2:14
If you wanted to include a MapQuest map or directions
2:18
or a search, or I guess they call it search ahead,
2:21
you can start looking for Denver,
2:23
and it autocompletes with different options.
2:25
What we want are just the simple APIs,
2:28
and there's quite a few of them.
2:29
There's a Directions API.
2:30
So you can send a request to get directions, like a route
2:35
and see here's an example, great documentation.
2:38
So this request is including a key.
2:42
So we have to put that key in there
2:44
and then from some address in Virginia
2:47
to some other place in Arlington, Virginia as well.
2:50
And then the response we get includes a bunch of information
2:53
about the different directions.
2:55
And I assume the different legs, the turns, yeah,
3:00
go south on this, proceed to this,
3:02
start out here, turn, go east, there's directions here.
3:07
There's also a Geocoding API, which is what we'll be using.
3:11
And there's a couple of different routes.
3:13
There is a Forward Geocode and a Reverse Geocode.
3:18
Reverse geocoding is when you have latitude and longitude
3:20
and you want the address, the actual human address.
3:24
Regular geocoding is when you have an address
3:26
and you want a latitude and longitude.
3:29
If we look at the docs here, we see the base URL.
3:32
So we'll need that.
3:34
We need to provide our key.
3:36
And this table tells us the name of that request parameter.
3:40
So the geocoding API for MapQuest just wants us to include
3:44
the key as part of the query string.
3:46
Some APIs are set up this way
3:48
as we saw on the slides in the previous video,
3:51
but not every API works this way.
3:54
Then we'll also include a location.
3:57
So we need to, that's required, those two things.
3:59
Location, something like Denver, Colorado.
4:02
We can get fancier and include a bounding box, what else?
4:07
MaxResults, the number of locations that we can get back.
4:11
There's a bunch of things that we can do,
4:13
but we're just gonna go with the first two,
4:15
the key and location.
4:18
So I have my key already.
4:19
I'm gonna copy this end point.
4:23
And the key I'm using is right here.
4:24
Once again, you can try to use this one,
4:27
but it may or may not work
4:28
by the time you're actually trying to run this.
4:31
So I'm in a new file called mapquest.py.
4:34
I'm gonna start by importing requests.
4:36
We're just gonna make a request
4:37
through this one Python file.
4:40
And I'm gonna call requests.get
4:44
we can see this is a get endpoint, right there.
4:47
Here's my URL, the base URL.
4:50
And then I pass in my params
4:54
and there's a couple of things that it's expecting.
4:56
We need to have a location and we need to have a key.
4:59
So I'm gonna set key to be my key variable from here.
5:04
And then I'm also going to set location to be,
5:09
what should we do?
5:10
I guess we can just start with Denver, Colorado,
5:12
which is our example.
5:14
We'll save that to a variable.
5:16
We'll call this response.
5:19
And then I'm probably just gonna open up IPython
5:22
and run this so we can explore the response.
5:25
The docs also tell you exactly what the response looks like.
5:29
It will come back as JSON,
5:31
unless we specifically ask for CSV or XML.
5:35
So let's try it out.
5:37
We'll go over to my terminal here, IPython
5:43
%run mapquest.py,
5:47
let's look at response.
5:49
We got a 200, that's always good.
5:51
And let's do response.text.
5:54
So here is the raw text.
5:57
And if I call response.json,
6:02
Now I can see the dictionary that's been converted
6:05
or created based off of this actual JSON text
6:09
and we have results.
6:10
So the first few things are,
6:12
let's see copyrights, options.
6:15
And then results is what we are probably interested in.
6:18
So for the location of Denver, Colorado,
6:21
it gives us things like the Country,
6:24
which is the U.S., the State, Colorado,
6:26
County, Denver County, the city is Denver.
6:29
It didn't give us a neighborhood
6:30
because all we said was Denver, Colorado.
6:33
But if we had added a specific address or an intersection,
6:36
we would potentially get the full neighborhood.
6:40
Then we get latitude and longitude,
6:42
as you can see right here,
6:44
now we can get more than one results.
6:46
So this I'm not sure exactly why I would get
6:49
more than one result here for Denver, Colorado.
6:53
But if you pass in something, that's a bit ambiguous,
6:56
like 123 Main Street, we can actually try that.
6:59
I don't know what we'll get.
7:01
Let's try it.
7:02
It might be too ambiguous, 123 Main St.
7:07
And run that again.
7:13
Run our app.
7:13
Or mapquest.py,
7:16
we'll look at response.
7:20
Okay, we got a 200, response.json.
7:24
Well, where did it find 123 Main Street?
7:28
Rancho Cucamonga in San Bernardino County, California.
7:32
Here's the zip code.
7:34
And here is the latitude and longitude.
7:38
All right, so simple example to start.
7:41
Next, we'll talk about how we could integrate this
7:43
into a flask application.
7:45
And we also need to talk about an important topic,
7:47
which is keeping our keys secret.
7:50
Right now, I'm just running this from a Python file.
7:53
It's not going to be visible in a browser
7:55
because there is no browser involved, period.
7:59
But if I were to share this code with students
8:01
like I am right now, and I wanted to keep this a secret,
8:05
I wouldn't be keeping it a secret.
8:06
If I want to share this code on GitHub,
8:08
or I wanted to, I don't know, send this code
8:11
to somebody and I didn't want this API key to be included,
8:15
especially for these APIs where a credit card is required.
8:19
That can be really problematic.
8:21
So we'll talk about a solution where we can hide the API key
8:24
from this file and make sure it doesn't go on GitHub.
8:28
But I'm breaking that on purpose
8:29
because I want you to see this API key for now.
8:32
So we just pass it in as part of the query string.
8:35
This is how MapQuest API works,
8:37
but remember not every single API follows the same format.
8:41
They all differ.
8:42
Just like they all have different end points.
8:44
They all expect different parameters.
8:46
You gotta read the docs and follow tutorials, great guides.
8:49
And hopefully it all works out.
8:51
And if you're ever confused, just google,
8:54
that's what every single other developer
8:56
who's trying to use it, will have to do
8:58
because odds are, if you're confused,
9:00
somebody else has been confused too.
9:02
All right, so we are making some simple API requests
9:05
with a key from Python.