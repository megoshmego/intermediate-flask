0:00
(soft music)
0:04
- All right.
0:05
So, next let's remember that a user is logged in
0:08
and use that across our application.
0:11
And on the other side of things,
0:13
let's make sure a user is logged in
0:15
before we show them these tweets.
0:17
There's nothing to see except for this h1,
0:19
but let's do it.
0:21
And then we'll add in some content in the next few videos.
0:24
So, in our app.py we have our tweets route.
0:28
Let's add some logic in here to look in the session
0:32
for a key called user ID.
0:37
So, we could just do if user ID not in session,
0:42
which right now nothing will be in session
0:45
because we haven't referenced
0:46
or added anything to session ever,
0:48
but we're doing this preemptively.
0:50
So if user ID is not in session,
0:53
we will flash message.
0:56
Please log-in first
1:01
or something like that,
1:03
and then return or redirect back to slash maybe,
1:08
or we could go to the sign-up form or the login form,
1:11
but we'll just redirect to slash for now
1:14
and then otherwise we'll render our template tweets.
1:18
So, if I try and go to slash tweets at the moment,
1:21
I'll always end up back at my route route.
1:24
I can try again slash tweets, no cigar.
1:28
Please log-in first.
1:31
Then, when we register and when we log in,
1:35
we should make sure that we're adding
1:36
the user ID to the session.
1:39
So, we can just do that right here.
1:41
This is for register session of user_Id equals new user.id.
1:51
And then when we log-in right here,
1:54
we'll do if user return, redirect tweets,
1:58
we could flash a message
2:00
that says something like, welcome back.
2:03
We could even put the user's name in there.
2:07
Welcome back.
2:09
And then user.username.
2:13
And then we'll do a session of user ID equals user,
2:22
which is a variable that we got back
2:24
from user.authenticates.id.
2:28
So, now we should be able to log in.
2:30
We'll have our user ID added to the session
2:33
under user_id.
2:35
And if I try and go to slash tweets,
2:37
it should remember that I'm logged in,
2:40
but we should also add in a log-out route.
2:43
Now, the thing about log-out,
2:44
now, the easiest way to do it is to define a GET route.
2:48
So, just add app.route/logout,
2:54
and then just leave it as a GET request.
2:57
Def log-out user.
3:00
And all we do is remove user ID from the session.
3:04
So, session.pop user_id,
3:09
and then we'll redirect return,
3:12
redirect to slash
3:14
so, we can start with it being a GET request
3:16
and it will work.
3:17
But the problem with it being a GET request is that,
3:19
well, there's a couple.
3:20
One is that it's just not very conventional, right?
3:24
This does have a real side effect.
3:26
We should make it a POST request.
3:27
But second of all, browsers, these days,
3:30
a lot of them will prefetch
3:31
and they get requests that it finds on the page.
3:34
So, if it finds a link to slash log-out,
3:36
some browsers will prefetch meaning send a request
3:39
to that URL.
3:41
And if it's a GET request,
3:42
it will actually just log you out.
3:44
So, a couple of years ago GET requests
3:46
for log-out routes were perfectly fine and common,
3:49
now with prefetching, it's pretty standard to make it
3:52
a POST request, also, somebody could just make a link
3:57
on any old page, not your website,
3:59
but just any website and include the slash log-out link
4:05
to our own application.
4:08
And it would log you out of that website,
4:11
which you probably don't want to happen.
4:13
So, we'll start with it as a slash log-out link.
4:17
Let's just verify that it works.
4:19
So, I'm going to log-in.
4:21
We can verify right now that I cannot visit slash tweets,
4:25
I end up going back here to Stupid Twitter homepage,
4:28
the route route.
4:29
Please log-in first.
4:31
Let's log-in.
4:33
Oh, this link doesn't work.
4:34
I forgot about that.
4:36
Let's log-in with my credentials.
4:39
Welcome back, blue the cat.
4:41
I'm now viewing tweets.
4:43
If I open a new window,
4:44
a new tab,
4:45
and I go to slash tweets,
4:47
I can still visit it.
4:49
My user ID is in the session.
4:51
I am logged in,
4:52
and this is persisting across different requests
4:55
and different windows and tabs, which is great.
4:58
But if I do go to slash log-out.
5:02
Okay, we should probably flash a message that says goodbye.
5:06
And if I try and go to slash tweets again, no cigar.
5:10
If I register,
5:12
well, if, I keep forgetting that link doesn't work,
5:14
I go to slash register.
5:16
We make some new username.
5:17
How about just Bob?
5:19
And the password is Bob, one, two, three.
5:21
We definitely should add some validations
5:23
for the password.
5:25
Just in general.
5:26
That's a good idea.
5:26
You don't want to let users,
5:28
or you don't want to allow users
5:29
to make super short, easy passwords.
5:31
So, I did Bob one, two, three.
5:33
If we register,
5:34
it takes me to tweets
5:35
and it does remember that I'm logged in.
5:38
So, now I am logged in
5:41
the application remembers me from one request to the next,
5:44
because user ID is in the session,
5:46
both from logging in with the log-in routes.
5:49
But also when you register,
5:50
we're not going to make you log-in afterwards,
5:52
which I hate it when websites do that.
5:54
Some really junky ones do.
5:57
You register and then you still have to type in
5:59
your username and password,
6:00
but our super fancy app doesn't.
6:02
Okay, maybe it's not super fancy.
6:05
All ready.
6:06
So, now that we have that done,
6:08
let's go into our nav bar on the index
6:13
or on the base rather.
6:14
And let's just make these links,
6:16
the actual links first, /login/register.
6:23
And now I should be able to click them
6:26
to go to /login/sign up.
6:28
All right, so, that's working.
6:30
But if I'm already signed in,
6:32
let's not show those, let's instead show a log-out link.
6:36
So, we can use our little Jinja magic here, percent.
6:40
And then we'll just do,
6:41
if, remember we have access to the session, directly
6:44
inside of our template.
6:46
Session of user ID.
6:49
If that's the case, we'll do our end,
6:54
and our else.
6:55
So, I'm going to do an else because I know
6:57
if you are logged in,
6:59
we're gonna show a link to log-out.
7:01
If you're not, then we'll show this stuff
7:04
and then we'll end our if down below, right here.
7:09
End if.
7:10
All right, so what do we want to show?
7:12
If you are logged in nav-item, same stuff we have here,
7:17
except if you're going to change this to log-out.
7:20
Log-out.
7:23
All right, so I'm going to refresh.
7:26
I'm currently signed in.
7:27
So, all I see is log-out.
7:29
If I log-out.
7:31
Now, I see log-in or sign up.
7:34
Perfect.
7:35
Let's log-in.
7:37
Now, I only see log-out.
7:40
So, you could also easily display a username up here
7:43
or information about a user.
7:45
If you had a little, let's say
7:46
you have them select an avatar, a photo,
7:49
you could show that up here.
7:51
You could have a drop-down menu where it's a link
7:54
to go edit their profile.
7:55
Of course, you have to implement all of that,
7:57
the routes to the logic and the actual HTML
8:01
for that, the forms.
8:04
While we're here,
8:04
let's go to app.py and flash a message
8:08
when you log-out.
8:10
So, we'll just do a flash, goodbye
8:17
or successfully logged you out or something,
8:19
just show them something.
8:21
So, I'm going to log-in,
8:23
now, log-out and we get goodbye.
8:27
All ready.
8:28
So, that's pretty much it for the basic log-in.
8:31
Of course, as I mentioned,
8:33
it would be nice to make, log-out a POST request.
8:36
That's just better practice.
8:37
I'll add a little comment about that.
8:39
All you would need to do is change your routes
8:42
and then put a form for that log-out button.
8:46
So, if I log-in.
8:48
Put a form here
8:50
and it can just be an empty form that
8:52
just submits a POST request
8:54
and that's pretty much it,
8:55
and just be an empty form with a button to submit the form.
8:58
You can even style a button in bootstrap
9:00
to look like a link.
9:01
If that's what you want.
9:02
There's a class called BTN dash link.
9:06
Anyway, you could also do it with JavaScript.
9:07
If you want to send a POST request when you click here,
9:10
or we'll just keep it as a GET request.
9:12
It's good enough for now,
9:13
but keep in mind that it is best practice
9:15
to create your log-out route as a POST route.
9:18
Not a GET route.
9:19
Anyway, moving on.
9:20
Let's actually show some stuff here.
9:22
So, that will be up next.
9:23
(soft music)
