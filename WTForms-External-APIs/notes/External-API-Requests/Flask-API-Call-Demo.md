0:00
(bright music)
0:04
- [Instructor] All right, so next up,
0:05
let's see how to integrate request with Flask.
0:09
A lot of the time,
0:10
we'll be making an application using Flask,
0:12
we have a bunch of templates and routes,
0:14
and we may need to make a request on the server side.
0:18
So we can also respond with a JavaScript file
0:21
that we include with our templates
0:23
and make AJAX calls from the client side.
0:26
But as we've seen, there are certain situations
0:28
where we definitely wanna make the request
0:30
from the server side,
0:31
including things like when we're using an API key
0:34
and we don't want a user to see the API key,
0:37
or commonly, if we need that data on the server side.
0:41
If we're trying to register a user,
0:44
let's say a user enters their address, 123 Chicken Lane,
0:49
okay?
0:50
And then maybe a state or a city, in Nevada City California.
0:55
This is the address they enter in.
0:57
We're gonna make them a new,
0:59
or we'll insert that into our database on the server side.
1:02
So we'll call something like User, if we have a user model,
1:06
we'll have name equal to something they passed in, email,
1:09
and then we'll have address equal to that address.
1:14
But we may also at the same time want to get location data,
1:18
latitude and longitude.
1:20
We could make an API call on the server side
1:23
before we actually insert a user into our database.
1:26
And then we could add in longitude,
1:29
if we had a column in our User's table, and latitude.
1:34
So that's one example of a situation
1:37
where we would want to make an API call in a Flask app,
1:40
where we make a call, we get data back,
1:42
and then we save that to a database.
1:45
So I'm gonna show how we could do something like this.
1:48
To start, we'll use the same API,
1:51
the Geocoding MapQuest API.
1:53
My key is here. Pay attention to that comment.
1:55
You generally do not wanna do this,
1:58
but because I'm an educator and this is not tied to a,
2:01
it sounds a bit pretentious, I'm an educator,
2:03
because I'm just doing a demo video,
2:05
and I want you to be able to download this code,
2:07
I won't put this in a secret file,
2:09
but you should if you're doing anything with an API key.
2:13
So we're gonna make an app that has a simple route.
2:16
Let's just do the root route, the / route,
2:19
that renders a form,
2:21
and we're just gonna ask a user to enter an address.
2:24
And then we'll geocode that and respond back
2:27
with information about latitude and longitude.
2:30
So we'll add our first route, @app.route /,
2:37
and we'll define our view function,
2:41
show_address_form.
2:46
And then in here,
2:48
we'll start by just returning render_templates
2:51
address_form.html,
2:55
which doesn't exist.
2:56
So I'm gonna make a templates folder.
3:01
I'll make my address_form,
3:05
keep it very simple,
3:08
and we'll just go with Address Form,
3:12
Enter Your Address.
3:16
We'll put a form in here.
3:17
And we need to figure out where this form will submit to.
3:21
So let's make a route. How about /geocode?
3:27
And we do need to decide
3:28
if it's gonna be a GET or POST route.
3:31
And it really depends on our intention here.
3:33
All that we're doing right now
3:35
is setting up a form where I can type an address in
3:38
and just view the geocoded latitude and longitude.
3:41
So we're not actually saving anything to a database.
3:44
There's no side effects involved.
3:46
If we were, if we were creating a user or storing anything,
3:49
I would definitely make this a POST form,
3:52
but I think GET is fine for now, the default.
3:55
So we'll add a single input in here.
3:57
We'll give it a name of address.
4:00
And we'll give it, what else, a placeholder
4:05
of Address or Enter Address,
4:10
and then a button to submit.
4:14
And let's see if we're getting that form on my root route.
4:18
Oh, what it's yelling at me about?
4:20
Oh, I've got a colon over here.
4:22
All right, I'm a decorator.
4:25
All right, so now we can enter our address.
4:27
And if we click Go, well, we don't have this route set up.
4:30
We need to define /geocode.
4:34
So when it submits to /geocode,
4:37
we'll make our request using the requests library
4:41
and then hopefully get some information back
4:44
and make a new template to show the user.
4:46
Or we could just add it to the same template.
4:48
We'll figure out what we wanna do.
4:50
So @app.route
4:54
/geocode,
4:56
like that,
4:57
and then def get_location,
5:02
or get_latLng or some name like that.
5:05
And we have a query string that will be included.
5:07
You can already see it here, address equals.
5:10
Right now, it's blank because I didn't enter an address.
5:13
So we definitely wanna get that user's address
5:15
that they entered into the form.
5:16
So address equals request.
5:19
And if it's a GET request, it's in the params,
5:21
request.params of address.
5:25
And then we'll just make a request,
5:27
what we've already done before,
5:29
response equals requests.get.
5:32
We need that BASE_URL and we need our API key.
5:36
And the key that we need to use
5:37
in our dictionary or params is location,
5:40
and this will be a variable address.
5:44
So let's make the request here, requests.get.
5:49
And I have a variable called API_BASE_URL.
5:53
And I would make this a variable,
5:55
and usually, we put it in all caps
5:57
because it's not supposed to change
5:58
if that's the BASE_URL for our API.
6:01
Just make sure that's matching.
6:04
Now, this BASE_URL
6:05
is their entire BASE_URL for the Geocoding API.
6:09
Specifically, we're using /address.
6:12
So we could have a different route
6:14
that was going to get directions
6:16
or they have reverse lookup.
6:18
We could use the same BASE_URL and just append /address
6:22
or /reverselookup or reversegeocode,
6:25
whatever the different routes are, or endpoints,
6:27
on their documentation.
6:29
So we're gonna do API_BASE_URL. We'll do an f string here.
6:35
Because we do need to change this URL ever so slightly,
6:39
we need /address at the end.
6:42
That's our endpoint. And then we have our params.
6:45
So params equals, and we need to pass in the key
6:50
as the parameter name key in the query string.
6:54
Some of the docs will want you to do something like api=key
6:56
or k, although k is not very common, it's usually just key.
7:01
And then the other part of the query string is location,
7:05
and that location will be this address right here.
7:09
So key, I don't know why I said =key, it needs to be :key,
7:14
and that needs to be a string,
7:16
you can see JavaScript bleeding in here, comma location,
7:21
which will be set to that address from the form.
7:26
All right, well,
7:28
then what we can do, just to see if this is working at all,
7:31
is put a raise in here.
7:33
I'll get the Dev Tools installed
7:34
and then we can see what's going on with our, actually,
7:37
we can just do a pdb, I guess, just to keep it shorter.
7:41
So, I think I have a little shortcut here.
7:43
There we go, import pdb; pdb.set_trace.
7:47
Save this to a variable. We'll call this response.
7:50
And before I can try this, I need to make sure
7:52
I'm actually getting the data from the query string
7:54
which is not request.params.
7:57
It's gonna be request.args.
7:59
So that's just a stupid mistake on my part.
8:02
Request.form gives us the POST request data,
8:04
but this is a GET route,
8:06
so it's request.args to get the query string.
8:09
And then we'll make our request with a key,
8:12
the address, and we're gonna set_trace
8:15
so that we can just look at res, hopefully.
8:18
So I'm gonna submit the form, Missoula, Montana.
8:21
All right, so this will spin out here
8:23
because we did hit this pdb.set_trace.
8:26
Let's look at res here.
8:28
All right, response object, res.json,
8:33
and what do we have?
8:35
Let's scroll down, or not scroll,
8:37
but let's visually try and make sense of this mess.
8:40
We've got location, Missoula, Montana,
8:43
admin, Type, Neighborhood, Missoula,
8:46
City is Missoula County, Missoula County, state is Montana.
8:51
City or country is US, postalCode is not included
8:54
because there's multiple for Missoula.
8:57
But we're getting latitude and longitude right here.
9:00
Now, to access that, ah, this is so annoying
9:03
to try and actually parse out visually,
9:06
but I know that we need to do a res.json.
9:09
Let's save that to a variable. We'll just call this data.
9:13
And then within data, we wanna look at, I think, results,
9:18
is that what it's called?
9:19
We've got options.
9:21
Yeah, I think it's, oh boy, here we are, results.
9:25
So, data of results.
9:26
And this is a huge part of working with APIs,
9:29
is working your way through the haystack that you get back,
9:33
finding the needle that is, in our case,
9:36
latitude and longitude.
9:37
So now we get a list,
9:39
and let's see what is inside of results of zero.
9:44
All right, so that's a first result.
9:46
It looks like we only got one result anyway.
9:49
And inside of that,
9:51
can we find latLng directly?
9:53
It's hard to tell here. So let's match that, latLng.
9:57
Okay, that did not, oh, I'm missing a quote.
10:00
No, that did not work. So what are we inside of?
10:03
latLng is right here, and it looks like the data structure,
10:07
this is not really how I would recommend doing this
10:09
by the way.
10:10
I would probably (laughs) play around with it in IPython
10:14
or paste it into a JSON formatter.
10:17
But we've got latLng, is it inside of locations?
10:21
So let's try this, locations.
10:25
That gets us closer.
10:26
Now, can we get latLng or do we still have to? No.
10:31
Let's list. So locations of zero.
10:36
Now we have streets. Okay.
10:39
Here we go.
10:40
Hopefully, this works for us, displayLatLng and latLng.
10:44
What's the difference between display and regular latLng?
10:49
Who knows?
10:51
So we're almost there, latLng.
10:55
Ah, hurrah! It worked.
10:56
And then we can get lat out of there by adding on lat,
11:01
and we can get Lng out of there using lng.
11:06
Whoo!
11:07
All right, so I'm gonna take this, copy it,
11:10
and then get out of here.
11:12
What are you? Quit.
11:15
Is that how it works? There we go.
11:17
All right, so now we'll remove this from our route.
11:21
And instead, we're gonna do a res.json.
11:25
We'll save it to a variable called data.
11:29
And then what we want, to get the latitude, will be this.
11:32
So we'll do lat equals,
11:35
and lng equals the same thing, but lng at the end.
11:40
Whoo, that should give us the two pieces we're after,
11:43
latitude and longitude.
11:44
Now, what do we wanna do with them?
11:46
I guess we could just start by printing lat and lng,
11:49
and just making sure it works.
11:52
And maybe before that,
11:54
I'll print a little line of stars or something
11:57
so we can see that it's easy to identify.
12:01
And we're still not responding with any sort of template,
12:04
so that's fine, but let's just see what happens.
12:06
Okay, moment of truth, gonna go back.
12:10
But instead of Missoula, Montana,
12:11
let's try an address that maybe is a bit different,
12:16
a full address of 1600 Pennsylvania Avenue, Washington, DC.
12:19
It's the address of the White House. Let's see what happens.
12:24
All right, so we get an error here
12:25
because we're not responding with anything from Flask.
12:28
However, we still are printing, hopefully.
12:31
Are we getting anything printed out?
12:33
Here we are. Those are our coordinates.
12:37
Let's see what happens. So, hopefully, I just copied that.
12:40
Let's go to Google Maps and paste that in.
12:43
I don't know if I need a comma or not.
12:45
And where does it take us?
12:47
Right there to, is this where the White House is?
12:50
I think so. Yes, it is. (laughs)
12:52
There we go. There is the White House.
12:54
The official address is right.
12:56
I guess this is the official pin that we got
12:58
based off of that latitude and longitude.
13:01
And that looks pretty good.
13:02
So, all we're doing is geocoding.
13:05
We should probably respond
13:06
with the latitude and longitude for the user.
13:08
Rather than making a separate template,
13:11
I think I'm just gonna reuse that same, exact template,
13:14
so return render_templates,
13:17
and this template will be address_form.html,
13:26
but it's also going to include, what should we do here?
13:30
We'll include a coordinates variable, coords, like that,
13:36
and that will be a dictionary.
13:37
I think I'll make this separately actually.
13:39
So coords
13:41
equals, and then we'll set lat
13:46
to be lat,
13:48
and then lng
13:50
to be lng.
13:52
Okay, so now we'll have that dictionary called coords,
13:56
and I'm just gonna pass it in under the name coords.
14:00
And then at the end, we are rendering that template.
14:03
So right now, if I just went back and submit it again,
14:07
it should just take us back to this template.
14:09
But what we can also do is, from within our address_form,
14:14
we could display the latitude and longitude up top
14:17
if those coordinates are here.
14:19
So we could just do a little if,
14:23
if coords,
14:26
and then end our if.
14:31
If there are coordinates,
14:32
maybe we'll make a, just a, what should we do?
14:34
Paragraph, an h, maybe an h3.
14:36
We'll do Lat,
14:39
which is coords
14:42
late, and I'm missing an extra pair of braces there,
14:47
and then we'll do Long below that,
14:49
I'll just duplicate this entire line,
14:54
lng.
14:56
So that shouldn't show up
14:58
if I just go to the main form here.
15:00
If I refresh right now, it's not there.
15:03
But if I now put in an address and submit the form,
15:06
let me find another address.
15:08
How about, let's try 10 Downing Street, London, UK.
15:14
We'll hit Go.
15:16
And it looks like we're getting longitude.
15:20
What happened to lat?
15:21
Oh, I just spelled it wrong. Typical.
15:24
Okay, well, I can just refresh
15:26
because this is a GET request, the data is just up here,
15:29
the address is part of the query string,
15:31
and we've got latitude and longitude.
15:33
Let's see if that's accurate. Who knows?
15:36
Well, I put it into Google Maps,
15:38
and it looks pretty good.
15:40
There is Downing Street.
15:41
I assume that's 10 Downing Street right there.
15:45
We could, yup, it is 10 Downing Street.
15:48
All right, so one thing
15:49
that we're not taking into account at the moment
15:51
is that we can get multiple matches back from the API,
15:54
and we're just automatically responding
15:56
with the first location that matches,
15:59
but there could be multiple.
16:00
In the case of 10 Downing Street, that was pretty specific,
16:03
but some of the things we've done will give us two or three
16:05
or even more potential matches.
16:08
So if we want, we can just take the first one,
16:10
which is all I'm going to do,
16:11
but we could also have, you know, some logic,
16:14
or display them all to a user, ask them to select.
16:17
You may have seen something like that before
16:18
when you go to add a shipping address,
16:21
and you type your address in and it tells you,
16:23
"We found five matches, can you select one of these?"
16:26
And they're usually more specific addresses.
16:29
The last thing I'll do is move this logic
16:32
to make my request into a standalone function.
16:35
So, usually, we wanna keep our view functions pretty slim.
16:39
Plus, if we ever want to reuse this geocoding logic,
16:42
I'm just gonna move it into a function,
16:44
and I'll just call this def get_lat,
16:47
or maybe just get_coordinates,
16:49
get_coords which accepts an address.
16:53
And then I'll put my logic right there.
16:55
So I'm gonna make my GET request, get the data, lat, lng,
16:59
and then return my coords.
17:04
Great. Now I can call it from in here.
17:08
So I'll go with coords equals
17:10
get_coords of address.
17:13
I've just moved that logic into its own function here.
17:17
Let's just verify it still works.
17:20
Go back to my form, Go,
17:23
and we're still getting our coordinates.
17:26
Now we definitely can break this.
17:28
We don't have any validation
17:29
to see if the address is blank.
17:31
We probably don't wanna do that.
17:33
So if address is blank,
17:35
also, if the address just doesn't have any matches,
17:37
we don't have any logic,
17:39
also, we don't have any logic if the API is not working.
17:42
What happens if we get a 400 status code,
17:44
the API is down, it's moved?
17:47
So we definitely would want to soup this up a bit
17:49
with some exception handling.
17:52
We'd wanna add some validation to see if this was empty.
17:55
And if it is, then we probably could just add
17:57
the required attribute (laughs) on the HTML field.
18:00
That would be best.
18:02
But we could also do some server-side stuff.
18:04
But this is really just more to demonstrate
18:06
that we can make a request, and there's an API key involved,
18:10
but the user can't see it.
18:11
All that the user sees when I send a request here,
18:14
I just go back,
18:16
all that a user can see if they were looking,
18:19
or anyone can see from the client side,
18:21
if I were to look for Homer, Alaska,
18:24
great, little town in Alaska, I click Go,
18:29
this is all that's included in the request.
18:30
It's just a request to my server.
18:33
It has the address there in the query string.
18:36
But the API key, none of the MapQuest stuff is here at all
18:40
because we only made a request to our server.
18:43
And then our server actually makes the request
18:46
from here to MapQuest,
18:49
gets data back, here's where we're getting that information,
18:52
and then we render a new template,
18:54
and that's what we see here.
18:55
It's the same template,
18:55
but now it has coordinates to display.
18:58
So very important nobody can see that key.
19:01
I'm not making that request from the client side.
19:04
Now, the downside, of course,
19:05
is that there is a page-refresh involved.
19:07
And sometimes you want a single-page app
19:09
or at least some single-page functionality.
19:12
So there are ways around this,
19:14
which we'll talk about a bit more the next couple videos
19:17
and specifically the next section after this.
19:19
We'll learn that we can respond with JSON,
19:22
we can make AJAX request to our own server,
19:24
then our server can make a call to some other API,
19:28
respond back with JSON to us.
19:30
So we can still have single-page app functionality.
19:33
But either way, we'll want to make some requests
19:35
from our Flask application.
19:38
All right, I know it's been a lot.
19:40
Hopefully, I didn't lose you.
19:42
We're just making a request,
19:43
but now we're doing it from inside of Flask app
19:45
when we get a request to a particular route.
19:48
(bright music)