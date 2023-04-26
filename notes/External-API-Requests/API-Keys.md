







Transcript


0:00
(upbeat music)
0:04
- [Instructor] Next up, let's talk about API keys.
0:07
So far every API we've used has been an open API,
0:10
there's no accounts or registration.
0:12
There's no authentication.
0:13
They're just simple APIs like getting pokemon or movies
0:18
or get help information.
0:20
But a lot of the very useful APIs
0:22
you'll actually wanna integrate into your applications
0:25
are not open APIs, you need to register
0:28
and a lot of them,
0:29
it's not just about registering.
0:30
You also will need to pay
0:32
depending on what you're trying to do.
0:34
So Facebook and Twitter and all of those big companies,
0:37
they do have free tiers of their APIs.
0:40
But then for large companies,
0:41
which are doing things at super high volumes,
0:43
they definitely charge you money.
0:46
So for these APIs that do require keys,
0:48
some of them also require what are known as secrets.
0:51
It's kind of like a username and a password.
0:53
So you have both things that you need to include.
0:56
The first most important thing
0:58
that I can give you as far as advice
1:00
is to read the docs.
1:02
For these large companies,
1:03
these big APIs, these popular,
1:05
let's say you're trying to make an app with Spotify
1:07
or SoundCloud or with what else is out there Flickers API,
1:12
Twitter, Facebook, Reddit, whatever the API is.
1:16
Most of these big ones
1:17
are going to have very, very good documentation.
1:21
Especially if they make money from people using the API.
1:24
They're not just gonna like, half-ass it
1:25
and just put something out there
1:27
like some of the free APIs might where it's not super clear.
1:30
There's great documentation,
1:32
there are usually start to finish tutorials
1:34
about what you need to do.
1:35
They have demo requests.
1:37
They have, a lot of them will have tools
1:39
where you can plug in your API key into the browser
1:42
and you can make your request from the documentation
1:44
to test around or play around.
1:46
It's kind of like a little sandbox with their API
1:49
and a lot of other people probably want to use the same API.
1:53
And if there's any pin points or areas of confusion,
1:56
you are bound to find tutorials, blog posts,
1:59
even YouTube videos, stack overflow posts
2:01
all about using Twitter's API or how do I create
2:06
a new playlist on Spotify using the API?
2:08
How do I view someone's friends from the Facebook API?
2:12
You'll be able to find tons of information about it,
2:15
but overall, the reason that these APIs require this stuff,
2:19
why do they need you to have a key,
2:21
has to do with a couple of things.
2:22
First of all, a lot of these APIs provide access
2:24
to sensitive, confidential, important information.
2:28
They don't want just anybody to be able to access.
2:31
When you sign up for this API,
2:33
a lot of the time you need to include a company name
2:35
or the name of your project, a URL,
2:37
where they can find your project deployed
2:40
a little bit of a bio about yourself
2:43
or a blurb about what you're trying to do.
2:45
How many users do you expect is this for profit?
2:48
Is this an educational application?
2:51
All of that information is tracked
2:53
by these companies that offer the API,
2:56
so that they can figure out if someone is misusing it
2:58
or abusing it.
2:59
If they're getting a bunch of spammy calls
3:01
or somebody is using the API to, I don't know,
3:03
put insensitive stuff on Twitter, for example,
3:07
or to spam people's Facebook messages,
3:10
then they can figure out based off of that key,
3:13
who is responsible for it and shut it off.
3:16
Versus if there was no key involved,
3:18
it would be a lot harder.
3:20
Also these APIs usually will cost money.
3:23
At least some tier will cost money.
3:26
So they need to have that key in there and that secrets
3:29
so that they can authenticate you and charge you money
3:31
and not somebody else.
3:32
They can know how many requests you've sent,
3:35
how many you have left at a given price, all of that stuff.
3:38
They need to know your credit card information.
3:40
So they associate your account
3:43
when you register for the API.
3:44
With that key, that is part of the API call.
3:48
And as I've already mentioned,
3:49
limiting abuse is a really important one.
3:51
So Google maps is actually free.
3:54
You do not have to pay to use it.
3:57
You can use the Google maps, geo coding API,
4:01
which takes some location data like a name,
4:05
a place, Joe's gas station in,
4:08
I don't know, Yuba city, California.
4:11
And it will give you information about the latitude
4:13
and longitude about directions, of how to get there.
4:17
What's near there. There's a places API,
4:19
and these APIs are actually free,
4:21
but you still have to include a credit card
4:24
mainly so they can keep you honest.
4:26
And I guess just keep you from abusing it.
4:29
You used to not have to include a credit card
4:31
to sign up for some of the lower tiers,
4:33
but that has changed.
4:34
So definitely pay attention when you're registering
4:37
for some of these APIs
4:39
that this should not discourage you from using them,
4:41
but just keep in mind that there's good reasons
4:44
why these aren't open APIs.
4:46
You can't just make a random request
4:48
from Curl or from Python
4:50
without first proving that you are able,
4:52
you're allowed to make that request.
4:54
So then the next question
4:56
is where do you get these API keys?
4:58
Well, you go to the website of the API.
5:00
If you're looking for Twitter's API,
5:02
I just searched Twitter API,
5:05
and they have a whole nice webpage,
5:07
a set of documentation for all of their developer tools.
5:11
There's a bunch of different Twitter APIs actually.
5:13
So there's a way of making tweets, sending a new tweets,
5:19
getting timelines, making what else?
5:22
Filtering tweets real-time search.
5:25
We've got direct messages.
5:26
So there's an API on Twitter that allows you to respond
5:30
and send messages through code.
5:33
So the reason you would do this,
5:34
like if you're a big company
5:36
and you're getting a lot of customer service,
5:38
direct messages from people complaining about a product
5:41
or giving you feedback or saying they haven't received
5:43
their order, you might get thousands of those a day.
5:46
You can use the direct message API
5:48
to write some automated responses or write an application
5:52
that will listen for new direct messages
5:55
and then email the appropriate person.
5:57
Or maybe you have a dashboard and there'll be ranked
5:59
and prioritize and who knows
6:01
there's a lot of things you can do.
6:03
So there's APIs for trends, for ads,
6:06
for placing ads on Twitter.
6:08
So for all of them, let's say,
6:09
I just want to go with the tweets API.
6:11
I wanna be able to post or retrieve a tweet.
6:15
They give you all the documentation
6:17
about the different end points,
6:18
but then there are these great guides.
6:20
There's information about how you can post a tweets.
6:23
And all of them are going to require if we go to one
6:27
of these end points, how about, I guess,
6:30
favorites/creates.
6:32
It is a post request to this end point favorites/create.
6:38
It looks like it requires authentication
6:41
response with JSON and if you scroll down,
6:43
they have an example request just done through Curl.
6:47
And if you look closely, there's things like consumer key.
6:51
So there's an auto auto-generated nonce.
6:54
There's different pieces of information you have to provide
6:58
to authenticate, and that's all found on the docs.
7:01
And if you do want to apply to use this,
7:04
you need to click on, Apply,
7:05
apply for a developer account.
7:07
Then you need to log in and they'll ask you some questions.
7:11
So Twitter is actually one of the more complicated ones
7:13
to use as far as getting set up and authenticated.
7:16
Some other websites like YouTube, as an example,
7:19
are pretty straightforward. Once you have a YouTube account,
7:22
you can just go to the API tab or just Google YouTube API,
7:27
and you can create API keys at will,
7:29
so you can have different keys and you can delete them.
7:32
So this one is definitely deleted afterwards.
7:35
It's not tied to a credit card either,
7:37
but yeah, you just create the key
7:39
and then you can toggle them on and off
7:41
and delete them and use those credentials
7:43
when you're making your API calls.
7:45
And then once you have a key,
7:47
the important thing is using it.
7:49
How do we make it work?
7:51
Where do we send it?
7:52
If I'm trying to send a tweet
7:53
or I'm trying to make a new playlist
7:56
through an API on Spotify,
7:59
there isn't just one silver bullet
8:00
for how you actually include that information.
8:03
It's different from one API to the next.
8:06
So some APIs want you to send it as a URL parameter.
8:10
They just want you to include the key in the query string,
8:14
but other APIs actually require some more complex pieces.
8:17
They might want you to send a post request
8:19
and include it as a particular header.
8:22
They might want you to encode things in a particular way.
8:24
It just varies from one to the next.
8:27
The good news is that any, for the most part,
8:29
anything you'd wanna use,
8:30
it's gonna have documentation
8:32
and other people who have done the same thing,
8:34
example apps on GitHub.
8:36
So you just have to do a little bit of digging.
8:38
It's not as simple as just, you know,
8:40
opening up Curl and just pasting a URL
8:43
and going and having it work.
8:45
It requires a bit of effort, but they're worth it.
8:48
These APIs that are protected,
8:50
generally are protected for a reason
8:51
that they do something interesting,
8:53
something powerful that you may wanna utilize
8:55
in your own apps.
8:57
So we're going to do a simple example in the next video,
8:59
using a geo coding API from MapQuest,
9:03
which does require an API key.
9:05
So we need to sign up for that.
9:07
You can do that now, if you wanna follow along
9:10
or at the start of the next video,
9:11
we'll do it together.
9:12
(upbeat music)