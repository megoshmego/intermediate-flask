
would you please evaluate for any important timestamps during the demonstration from the previous transcript? 



will you please evaluate the following script for the key terms, concepts, and any other relevant information and definitions and include the title of the video "Post Requests", and the section of the course "Intermediate Python", and subsection "External API requests", as well as any demos you think would helpful to me?: 

 

 


0:03
we can also send a post request using
0:06
the request library it is just requests
0:10
dot post and then a URL and then we have
0:13
two options if we want to send data with
0:15
our post request usually we're sending a
0:18
post request let's say we're using the
0:20
Twitter API we've gone through
0:22
authenticating and registering we've got
0:24
an API key we put our credit card in
0:27
we've confirmed our email and we still
0:30
have some will left in our in our brain
0:32
to keep going if we had some end point
0:35
I'm just making this up but it's called
0:37
slash new tweet on Twitter's API we
0:41
would send a post request to slash new
0:43
tweet and then send some information
0:44
like the user name of this new tweet the
0:48
tweet content the hashtags I think
0:51
that's pretty much it right but I don't
0:53
know whatever data needs to be sent we
0:55
actually have two different options for
0:57
passing that data in to request dot post
1:00
so I'll show you that in just a moment
1:02
but first for testing purposes and
1:04
demonstrating post requests I'm going to
1:07
be using a website called request bin it
1:09
just allows me to make a little endpoint
1:12
that I can send a request to and it will
1:13
just show me the request and what it
1:16
included the different headers any data
1:18
if it was a get or a post or something
1:20
else and the reason I'm doing that is
1:22
there aren't many api's that we can use
1:24
where you don't have to register you
1:26
don't need an API key that allow you to
1:28
send a post request the iTunes API is
1:30
all get requests it's all searching so
1:32
this will be the closest we gets at
1:34
least for now but the code I show you as
1:37
far as making the request is exactly the
1:39
same you'll just need to actually
1:41
substitute in an API and put your API
1:44
key in there and that's something we'll
1:45
cover after this all right so to send a
1:48
post request I'm just gonna copy this
1:50
endpoint and then I'm an eye Python I
1:54
have requests still just make sure it's
1:57
here yes requests top post and then I'll
2:00
pass that URL in and I could just do
2:03
this and not include any data with my
2:05
request we get a 200 status code and if
2:09
i refresh oh I guess I don't even need
2:11
to refresh my page anymore
2:13
it does it live here we see that we got
2:15
a post request and it just looks like
2:17
this not too much there's no data
2:19
included just a couple headers
2:22
user-agent its Python requests so it's
2:25
coming from Python requests and that's
2:27
kind of it and if we want to pass data
2:30
in we have two options data and JSON
2:34
these are two different keyword
2:35
arguments that we can use when we send a
2:37
post request we can include data as
2:40
we've already seen and there are
2:42
different formats that that data can be
2:43
included as so there is the traditional
2:46
webform format it's called what does it
2:49
form encoded and there's also JSON which
2:53
we know and hopefully love we can send
2:55
data as JSON
2:56
now most api's these days will support
2:59
both and in general you'll probably want
3:02
to use JSON and most of the modern api's
3:05
are expecting to receive JSON but
3:07
requests dot post this method supports
3:09
two different ways so let's start with
3:12
data if I want to send some data along
3:15
with this request I can add data and
3:18
then pass in a dictionary a Python
3:21
dictionary let's say our data is
3:23
username is chickens and what else I
3:29
guess tweet text just tweets will be
3:37
bok-bok all right so that's our data
3:40
that we're sending okay we get a 200
3:44
status code refresh not keep saying
3:46
refresh we don't have to refresh click
3:48
here and because I sent that with the
3:51
data keyword arguments the information
3:54
that was sent along with the post
3:56
request the body of the post request
3:57
looks like this it's not JSON this is
4:01
what's known as WW form URL encoded this
4:07
is the format of the data that we just
4:10
sent now we can also send data as JSON
4:13
and as the slides mentioned this is
4:16
going to be more common most likely for
4:18
you so if I change this to instead be
4:21
the JSON keyword arguments
4:25
same data same endpoint come back over
4:29
here here we go this is the raw text of
4:34
the response or the request body and if
4:37
we look at the headers for this one
4:39
content type is set to application slash
4:42
JSON versus the other one that I made
4:45
using the data keyword argument where
4:48
the post request body looked like this
4:50
content type was set to application
4:52
slash xww form URL encoded form encoded
4:57
is the format that forms are going to
5:00
submit from in the browser if you make a
5:02
post request from a form but JSON is the
5:05
standard most of the time these days
5:07
especially if you're working with
5:08
complex hierarchical data I'll show you
5:13
an example if I do this from a file
5:15
instead so I can just write my code and
5:19
have a bit more room we'll do a requests
5:22
dot post hopefully I still have that URL
5:25
my clipboard and I'm really so we need
5:29
this URL here get rid of all of that
5:31
let's say I had some dictionary called
5:34
data and it included a username like we
5:38
had before which will be chickens again
5:40
but it also includes how about a list of
5:45
tweets and this will be a list an actual
5:48
list and in here we'll do something like
5:52
hello and then we'll also have goodbye
5:56
and a third tweet will be I guess bok
6:01
bok again alright and maybe we have one
6:05
more tweets that is a dictionary where
6:08
it has an ID of one I'm just trying to
6:11
come up with some structure that's a
6:13
little more complicated so ID is one and
6:15
text is my first tweet okay so here is
6:24
our dictionary has some nested data
6:27
structures in here and if I send this as
6:30
JSON just JSON equals data I'll just run
6:35
this file quit ipython python i
6:39
toons dot dy we get a new post request
6:43
that came in and it looks pretty much
6:46
the same it has been turned into JSON
6:48
which sometimes means that things will
6:50
be slightly different because JSON and
6:53
Python are not the same thing even
6:56
though it's pretty close however if I
6:59
instead had sent this as data and not
7:02
JSON but data which is that other
7:05
keyword argument and I try sending it
7:07
again it still works but if we look at
7:10
the raw body of our request the array or
7:14
the list that we had is broken up into
7:17
this weird thing where we have and
7:19
tweets equals and tweets equals and
7:22
tweets equals and it breaks up the
7:25
content of our data structures into this
7:28
weird format so this can be recompiled
7:31
and and reformed on the API side of
7:36
things but most of the time if we have
7:37
complex data we'll want to send it as
7:39
JSON when we make a post request so we
7:42
have two different options I would just
7:44
stick to our default to always doing
7:46
JSON when we do send our data as JSON
7:50
it's going to automatically be turned
7:52
into JSON so we don't even have to take
7:55
something that is not JSON like we did
7:57
here and turn it into JSON just by
8:00
passing it in under that keyword
8:01
argument requests outpost will convert
8:05
this to valid JSON and send it and it
8:08
also makes sure that the content type is
8:11
set to application JSON I think I lost
8:14
it where are you there we go application
8:18
JSON already so this is a fake API it's
8:22
just a way for us to see the information
8:25
that's sent from each request but you
8:27
would follow this exact same process if
8:29
you were working with a real API the
8:32
only distinction is that most api is
8:34
that you'll actually be able to send a
8:36
post request to and send data to like
8:38
the spotify api you can send a post
8:40
request to add a new song to a playlist
8:42
and that playlist will actually be
8:44
updated we're not searching we're
8:46
actually changing someone's account in
8:48
order to do that we have to have some
8:51
form of API key and
8:52
occasion and it does get a little more
8:54
complicated but the request itself is
8:56
still just a request dot post
9:02
you
