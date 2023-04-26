would you please evaluate for any important timestamps during the demonstration from the previous transcript? 



will you please evaluate the following script for the key terms, concepts, and any other relevant information and definitions and include the title of the video "Server Vs Client API's", and the section of the course "Intermediate Python", and subsection "External API requests", as well as any demos you think would helpful to me?: 

0:01 / 8:05

Transcript


0:00
(upbeat music)
0:04
- [Instructor] All right, welcome back.
0:06
Next up.
0:06
We've got a pretty quick sub unit talking about,
0:09
using external APIs from a flask application
0:13
and also just making requests from Python in general.
0:16
Back when we covered Axios and Ajax,
0:18
we saw how we can make a request from the browser,
0:21
but sometimes we also wanna make API requests from Python
0:25
or from whatever our server is written in,
0:27
whether it's Node or Ruby or Python.
0:30
It's pretty common that we have some data
0:31
we want to get on the server side.
0:35
So let's compare the approaches.
0:37
One option to talk with an API is to make a request
0:39
from JavaScript from the browser using Ajax.
0:43
Well, usually a library these days,
0:45
like Axios or at the very least
0:47
a tool like fetch built into the browser.
0:50
But we also have server-side requests
0:52
which are made on the server side,
0:53
so they're not made from the browser.
0:56
Just like I can make a request with curl from my machine.
0:58
I can make a request using Python.
1:00
I can make a request to load iTunes data or Pokemon data
1:04
or recent Tweets.
1:06
And there's a lot of reasons I might wanna do this.
1:09
So here's a diagram of a client side request.
1:12
Let's say here's a simple flask application,
1:14
we have set up our server, we have a database
1:17
and then we have the browser where a user
1:19
is requesting some page from our server.
1:22
And then we probably get some information from our database
1:26
and then we can respond to the browser,
1:28
the client with a HTML CSS and JavaScript.
1:32
And then we can have some JavaScript in that browser
1:35
that makes a request to some API like the Pokémon API
1:38
or the iTunes API.
1:40
And then that API respond to something
1:42
and then JavaScript does something,
1:44
maybe it adds something to the page.
1:46
It removes something from the Dom, it shows the results.
1:50
This is your typical client side request workflow.
1:54
Really the client side request is just happening here.
1:56
Can ignore all of this.
1:58
It's just the browser making a request to an external API
2:01
and getting something back.
2:03
Also, I should note here
2:05
that we can also respond with JavaScript to a browser.
2:08
So to the client side, some HTML and CSS,
2:11
and JavaScript from a flask application
2:14
that then makes Ajax requests back to our server.
2:17
That's something we'll talk a little bit more about
2:19
in the next sub unit.
2:20
When we talk about JSON and RESTful APIs.
2:23
So we can do this very easily from the browser,
2:25
make a request and JavaScript to some external API.
2:28
There's no flask involved at that point.
2:30
It's just Java script, making requests,
2:32
getting something back.
2:34
This can be faster, but there are limitations.
2:37
So why would we do this?
2:39
Why would we make a request from the server side?
2:41
Here's our flask server, here's our database,
2:44
here's the browser and here's an external API
2:47
where through Python, we might request something.
2:50
So let's say we're working with the iTunes
2:52
or the Pokemon API, from my flask server.
2:56
Let's say the user hits some end point
2:58
like Slash list or Pokemon.
3:01
My flask Python code can send a request to Pokemon api.com,
3:06
get results back,
3:08
and then use those results to make a template or even save
3:09
them to the database, just to do something via Python,
3:14
to respond to my browser with.
3:16
So that requests logic is happening
3:17
on the server side of things.
3:19
Right here is a line between client and server
3:22
versus over here,
3:24
the line is kind of a diagonal line right here.
3:28
Purple is server side and blue is client side.
3:31
So why would we do this?
3:33
Well, certain APIs are set up so that you have to do it.
3:36
You don't have a choice.
3:38
If you tried to make a request to an API
3:40
that enforces the same origin policy
3:42
or has strict restrictions,
3:44
you won't be able to actually request that from Ajax.
3:48
But what we can do is set up a route
3:50
in our flask application.
3:53
Let's just say,
3:53
hypothetically Reddit's API
3:56
is not gonna work through Ajax,
3:58
so we can set up a route in our flask server
4:01
that will make a request from the server side
4:03
to read its API.
4:05
And we can request that route from the browser.
4:07
So it's kind of like a game of telephone.
4:09
The browser says, please,
4:11
I want the Reddit information to our foster server.
4:14
The first server says, okay, hang on.
4:15
We gonna go get it.
4:16
It makes the request to read its API that responds back.
4:20
And then the flask server
4:22
doesn't even have to respond with a template.
4:23
It can just respond back to Ajax needed.
4:26
So we could have an Ajax request
4:27
that would not work to go directly to an external API.
4:31
Instead, we could send it to our server.
4:33
The server does the external API
4:35
and then that ping pongs back to our Ajax in the browser.
4:39
But other reasons include
4:41
a lot of the time you want to do something
4:43
that you can only do server side,
4:45
like if we want to involve our database
4:47
and I want to get, I don't know,
4:49
a hundred Pokemon from the API and put them in my database.
4:53
I have a Pokemon model from SQLAlchemy,
4:56
or when we register a user and we ask for their zip code,
4:59
maybe I wanna take that zip code
5:01
and get a Longitude Latitude from an API.
5:04
There are APIs that will do this,
5:06
and I could send that over.
5:08
What's the Longitude Latitude
5:09
for 10003, the API responds
5:13
and then I can save that to my database.
5:16
So that's something I would do on the server side.
5:18
Also a really important one is that a lot of these APIs
5:22
that you probably care about,
5:23
a lot of the fancier, Twitter,
5:27
Facebook, API APIs, LinkedIn's API,
5:30
pretty much any of the API from big companies, Spotify,
5:33
where you can actually do things like
5:36
create a new Twitter post, a Tweet,
5:38
I guess that's what it's called
5:40
or update information about a user
5:43
or get authenticated information.
5:45
Like, somebody's friends that are private.
5:48
Those APIs are now just open for everyone to use.
5:51
They have a lot more restrictions
5:53
and you need a password, an API key.
5:56
You need to be authenticated a lot of the time.
5:59
And we can't really do that from the browser
6:01
because everyone can see every request
6:03
that we send from the browser.
6:04
We've seen that in the dev tools.
6:06
But if we instead make the request from our server,
6:09
anybody who's actually viewing our website is not gonna
6:12
be able to see that request happening.
6:14
They might see an Ajax request to the server that says,
6:16
please make a new tweet/new tweet.
6:20
But then the server actually does that API call
6:23
and sends the password along with the information
6:27
to Twitter's API which requires a password.
6:30
So that is a really common reason also
6:32
to do server-side requests.
6:34
And we'll actually see a simple example of this
6:37
using a geocoding API,
6:39
and just a bit,
6:40
geocoding means taking a human readable address
6:44
or States or location like the golden gate bridge
6:48
and converting it into Longitude Latitude,
6:49
So you can display it on a map
6:51
or store that in your database.
6:53
So we'll be using an API that does require an API key,
6:56
and we don't want everyone to be able to see
6:58
that key in the browser.
7:00
All right, so there are important distinctions here
7:03
between these two approaches,
7:04
but what they have in common
7:06
is just the fact that it's an HTTP request being made,
7:09
whether it's coming from Python or Ruby or Node.js or Java,
7:13
it doesn't matter.
7:14
It's just a request.
7:16
Or if it's coming from the browser, it's just a request,
7:18
but there are these important considerations
7:20
around things like your API keys.
7:24
Does it need to come from the server side
7:25
so that a user can actually see that API key?
7:28
Is there a, an issue,
7:29
a same origin issue where the API
7:31
is not going to allow us to make an Ajax request?
7:34
These are all things to ask yourself.
7:36
And often, especially with same origin,
7:39
I just try and use Ajax a lot of the time to start
7:42
and then realized it's not gonna work.
7:43
So then I make a route in my server where I can relay
7:46
that requests and make a server-side API call
7:49
and then send that back to the browser.
7:51
Anyway, we'll see some examples of this and just a bit,
7:55
we're gonna start by learning
7:56
how we make a simple request using Python.
7:59
(upbeat music)