0:04
- So I wanna quickly talk about other things
0:07
that we might make a request for from the server side,
0:10
especially things like adding data from an API
0:13
into our database.
0:15
Right now we're just rendering some information
0:17
back to the user about the latitude
0:19
and longitude with this one API.
0:22
But we could also create a new user model
0:25
and save it to our database.
0:26
If we had a user model,
0:28
we would do something like make the API call,
0:32
get our coordinates,
0:34
and then as we instantiate a new user,
0:36
we would then pass in coordinates
0:38
or we could pass in the lat and long
0:42
or whatever our columns are on the user model,
0:45
and then we could also add in,
0:47
let's say a user specified a username from a form
0:50
and they specified an address,
0:52
but we took their address
0:53
and turned it into a lat
0:54
and long from some function,
0:56
and we can save that,
0:58
and now we have more information about that user.
1:01
We use some of what they gave us
1:02
to make an API call
1:04
and get more data.
1:05
Although if we were doing that,
1:07
we would probably make this a post route,
1:09
not a get routes,
1:11
but otherwise it would be pretty much the exact same flow.
1:14
We get some data from a form
1:16
or from the query string in this case,
1:17
but in a post route, it should be a form data.
1:20
Then we send a request in this case to MapQuest,
1:23
we get results back
1:25
and we save something to our database
1:26
and then we'd probably redirect
1:27
instead of rendering a template here,
1:30
we'd redirect somewhere
1:31
because it's a post route
1:32
or as another example,
1:34
we can do things like use the Twilio API,
1:37
which is a really fun one.
1:39
It's an API that allows you to send text messages.
1:42
You can make phone calls,
1:43
you can even set up
1:45
a phone, a hotline where people call
1:47
and they go through the whole like robotic menus
1:50
where you're supposed to say like, speak to operator
1:53
or check account balance,
1:55
or press two to, you know, end your misery
1:58
or whatever, you have these different responses.
2:01
Anyway, the point is you can use Twilio
2:02
to set all of that up.
2:03
It's an API, of course, if they're sending text messages
2:07
and making calls that is gonna cost money,
2:10
they do have a free level
2:11
where at least they used to where you can make a couple,
2:15
I don't know how many requests it is a month.
2:17
Let's see they limit you.
2:20
If we wanted to look at the SMS messages
2:23
so we can send text messages,
2:25
we can also receive text messages.
2:27
So we can set up an app where, you know,
2:29
we have something like, text hello to this this message
2:34
and I don't know, we'll donate X amount of money
2:36
or we'll do something.
2:38
We'll send you the weather.
2:40
You can set up a server
2:41
that is going to get those text messages all through Twilio.
2:45
So there's other things like an email API phone calls
2:48
where you can have automated voice phone calls,
2:50
but we want SMS.
2:51
We're not gonna actually go through with this right now,
2:54
but I just wanted to show you another example.
2:56
If we look at use cases, I like their docs.
2:58
They use cases like Uber uses Twilio
3:01
to send you a text message.
3:03
When your driver is nearby.
3:06
Coca Cola uses it,
3:08
when let's see technicians are servicing a vending machine,
3:12
and they've been dispatched.
3:13
Appointment reminders for hospitals,
3:15
scheduling shifts from Alaska Airlines,
3:18
order confirmations, Nordstrom sales and support.
3:22
So these are just some use cases,
3:24
but in actually all of these examples,
3:27
there's some event that's happening.
3:29
Whether it's an Uber driver being arriving or being nearby,
3:32
somebody being dispatched, you placing an order, let's say,
3:36
that's what we had.
3:37
You were placing an order, we wanted to send a text.
3:40
Well, if we look at the API
3:43
to send a text message,
3:45
they have a little demo here.
3:47
You need to have an account, SID,
3:49
and an auth token,
3:51
and then you specify a two number
3:54
and a from number some body for the text
3:57
and then you can also include some media like an image here.
4:01
And then you just send that request
4:04
through using a client's for the API.
4:05
We'll talk about that in the next video.
4:07
But my point here is that we can have some server side route
4:12
like slash checkout,
4:14
and we take some information from a user.
4:18
We'd probably use an API to process the payment.
4:20
So there's another use case for server side APIs,
4:23
and then after it's been processed,
4:26
we send them a confirmation text using the Twilio API.
4:29
So we could use requests
4:31
and we can send an API call with our key
4:33
and our auth token and the cell phone number
4:36
that we're texting
4:37
and it will be sent.
4:39
So the point is that we have lots of use cases
4:41
for APIs on the server side.
4:44
Things like sending texts, definitely,
4:47
but also we could do silly little trivial things
4:49
like we have here.
4:51
Although this is something we could easily replicate
4:54
just with a pure JavaScript,
4:56
except for the fact that we wanna hide
4:58
the API key from a user
5:00
and if we were making this API call to the MapQuest API,
5:04
all in Ajax, all JavaScript on the client side,
5:08
a user could see that key,
5:10
but this is still simple.
5:11
It's not the most exciting thing ever,
5:13
but I highly encourage you to check out things like Twilio.
5:17
There's a lot of these lists to see fun APIs.
5:20
So there's what else is on here?
5:22
Well, I haven't heard of any of these,
5:25
so maybe not that fun.
5:27
Let's look at upvotes, sort by up votes.
5:30
So we've got Cat Facts, Square.
5:33
If you wanna accept payments,
5:35
different job APIs, Meme Generators,
5:38
a list of cocktails, sentiment analysis.
5:41
That one's pretty cool.
5:42
This is a fun one, where you can pass in some text
5:46
or a tweet
5:47
or an essay
5:48
and it will tell you using machine learning,
5:51
using natural language processing,
5:54
it will tell you the general sentiment.
5:56
So depending on how they break it down,
5:58
usually there's a couple of different categories.
6:01
They'll tell you if something is positive, okay.
6:03
It looks like they give you a score out of 10,
6:05
how positive something was.
6:07
So they're showing a use case for hotels
6:09
and restaurants to figure out a dynamically using code.
6:13
If reviews are positive or negative.
6:16
Emotions, it will score that for you
6:18
and then return something back
6:20
that tells you an average score
6:22
and then it probably breaks down word by word,
6:24
what are the most negative things?
6:25
What are the most popular things?
6:27
So this is an API.
6:29
It looks like they have some free tier,
6:32
and there's a bunch of other fun APIs you can play with.
6:35
So as you work on your own independent projects,
6:38
and you start to think about some of your capstone projects,
6:41
and if you're running out a fight
6:42
or if you don't have any ideas
6:44
and you need some inspiration,
6:46
it always helps to take a look at cool APIs,
6:48
especially now that we can make requests
6:50
from the server side,
6:51
our possibilities open up quite a bit.
6:54
Now we can use these authenticated APIs.
6:56
We can hide our API keys.
6:58
Generally we can do more impressive, exciting things.
7:01
So take a look online, look through different APIs,
7:05
read different tutorials,
7:06
come up with some ideas and play around.