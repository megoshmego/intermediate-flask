Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Keeping a User Logged in", the subsection title "Hashing and Loggin In", and the section title "Intermediate Flask"?
(upbeat music)
0:04







- [Narrator] So once we have our basic forms
0:06
for registration and authentication set up,
0:09
as well as the logic implemented
0:11
that we just discussed.
0:13
We have our routes configured,
0:15
a user can now sign up.
0:17
So this would be done, or this is not registration
0:20
but this right here, and they can log in
0:24
but there's also this other piece that's crucial
0:26
we need to be able to remember
0:28
that someone is logged in,
0:29
or we need to know if someone is not logged in.
0:32
If you notice with this application,
0:34
I'm not logged in right now
0:36
so I see two links on the homepage on the route
0:40
local host, 5,000
0:41
register or login.
0:43
But once I log in
0:46
redirect to slash secret,
0:48
okay, I can see this
0:50
I couldn't see this previously.
0:52
I now have two different links log out and secret.
0:56
So we're showing different content
0:58
depending on if somebody is logged in or not,
1:01
we have access, or we know if somebody
1:02
is registered and authenticated,
1:05
if they're currently logged in
1:07
so we're displaying content
1:09
that depends on
1:10
whether a user is currently logged in or not.
1:13
We also have this route slash secret
1:15
I can only visit if I'm logged in
1:18
and it's not just about hiding and showing this link
1:20
but even if I log out, yes, the link is gone
1:23
and if I tried to go to slash secret
1:25
the app knows I'm not logged in
1:27
it keeps redirecting you back to slash
1:29
I can't go to slash secret.
1:31
So how do we do that?
1:32
How do we know that somebody has logged in
1:33
or know that they're not logged in?
1:35
And how do we keep knowing that
1:36
as long as it hasn't hit, log out?
1:39
It all has to do with our good friend flask sessions.
1:43
So to remember if somebody is logged in,
1:46
usually what we do is store their user ID
1:48
in the session.
1:50
So the same old session we've used before
1:52
which is based off of cookies in the browser
1:55
it's just a way of persisting information
1:58
of adding States on top of HTTP
2:00
which is a stateless protocol
2:02
is a way of remembering who's logged in.
2:05
So when somebody does log in, in our slash login route
2:09
as a post, if the form is validated,
2:13
this code only runs
2:14
if somebody has actually filled out the fields
2:17
if it's a post request
2:18
that should be reviewed from what the forms,
2:21
we take their name and password,
2:22
we authenticate them
2:23
using user.authenticate the class method that we set up
2:26
and then either returns the user that matches
2:29
just to refresh your memory like we have here,
2:32
or it returns false.
2:34
And if it returns the user
2:36
we add to the session, a user ID key
2:39
and the value is that user's ID
2:42
user ID of three, which is what we have right here.
2:45
And then we can redirect them to slash secret for example.
2:49
Otherwise if they didn't authenticate,
2:52
we'll add an error to the form
2:53
and then re-render the template.
2:55
So when they log in, we add the user ID to the session.
2:58
Then anywhere in our application
3:00
we can check to see if user ID is in the session.
3:03
So in our actual templates
3:06
I can display something different depending on whether
3:09
user ID is in session.
3:11
It doesn't matter what the user ID is
3:13
if all I want to do is display a log out link
3:16
and a secret link.
3:17
If there's a user in the session or user ID,
3:20
I'll show that if not,
3:21
I'll show something else
3:23
and we can see that if I go to my index, HTML
3:27
if user not in session,
3:29
we show them register and login
3:30
if user ID is in session,
3:32
we show them log out and secret.
3:35
So that's hiding the links
3:36
but somebody could still go to slash secret
3:39
even if they don't see the link
3:40
but fortunately, we can also ensure
3:42
that somebody is logged in,
3:44
in our view functions.
3:45
We can add some simple logic
3:47
instead of a route like slash secret,
3:50
where we check for user ID.
3:52
If user ID not in session, we will flash a message
3:56
you must be logged in and we'll redirect them somewhere.
4:00
And then otherwise we'll show them the secret template.
4:04
So we can check in our views
4:05
and we can check in our routes
4:06
if there is not a user ID in the session
4:09
you gotta get out of here, you can't view this page.
4:12
But we can have other routes like the route route of course,
4:16
here, we're not looking for any sort of user ID
4:18
in the session, in the router itself
4:20
we just render the same template no matter what,
4:23
but the template has a little bit of logic
4:25
that will show something different
4:27
depending on whether a user is logged in or not.
4:30
So session is very important here
4:33
and hopefully you're pretty comfortable working with it
4:35
if there's not much to it
4:37
assuming that you understand how it works
4:39
and this idea of cookies
4:40
and adding state on top of HTTP,
4:43
all that we need to do is set
4:44
session of user ID equals something.
4:47
You might also see people use current user, current user ID
4:50
you just need something that you're consistent with
4:53
and then you can check for that
4:54
inside of your view functions
4:56
to show or hide or redirect people
4:58
to prevent them from coming to a routes
5:00
and instead of your actual templates
5:03
to alter what a user sees
5:04
depending on if they're authenticated or not
5:07
and of course you could get even more intense with this
5:10
if you had different levels of,
5:12
you know, what a user was allowed to see
5:14
and not allowed to see you could have different roles.
5:17
So this is just checking if there is
5:18
any user user ID in the session,
5:21
but you could also add onto that
5:23
you know, if in the session
5:25
there is something called I don't know, admin
5:28
or is admin is true
5:31
versus is moderator is true versus just regular old user.
5:35
You could have these different things
5:36
that you're keeping track of
5:37
so it's not just a matter of showing
5:40
one thing or the other.
5:41
If someone's logged in,
5:43
we can also have, you know a tool bar up top
5:46
that only shows two administrators.
5:48
So you can use the session
5:50
and store information that will persist
5:52
and that can include information about the current user,
5:55
like the ID
5:57
and this is also
5:58
how we would associate something
6:00
with the currently logged in user.
6:02
Let's say that we had a to-do list
6:04
or a, let's say a Reddit clone
6:05
where someone could comment.
6:07
A comment is going to have a relationship with a user
6:10
who owns it
6:11
in order to associate that comment
6:13
with a user who created it,
6:15
you could look in session,
6:17
look for user ID
6:18
and use that user ID to create that new comment.
6:22
And I'll show you an example of that
6:23
once we create this whole thing from scratch
6:26
we're gonna go through and write our routes
6:28
we'll write our forms and all of that after this.
6:31
And then to log someone out, it's very simple
6:33
we just remove the user ID from the session
6:36
that's it, session.pop user ID.
6:39
Now, if they try and go to
6:40
one of our protected routes like slash secret
6:43
user ID is not in the session anymore
6:45
if they go to the homepage, user ID is not in session
6:49
so they'll see this they won't see this.
6:52
Logging out is really, really easy
6:55
and if we look at the route for it here, right here
6:59
app.route, log out, session.pop
7:02
redirect, that's it.
7:04
Pretty straight forward.
7:05
Okay. So I definitely recommend that you
7:08
download this code
7:09
you probably already have
7:10
step through it, play around with it
7:12
see if you can add in your own method or your own route
7:16
that is protected
7:17
add in a template that displays something different
7:19
depending on if you're logged in or not
7:21
and then next after this,
7:23
I'm gonna go through the process
7:25
of creating our own authentication of implementing this
7:29
in an application from scratch,
7:31
kind of from scratch
7:32
we gonna have the flask app already
7:33
but we'll add the user model,
7:35
We'll add the form so add the B crypt
7:37
and we'll also learn how to associate a user
7:40
with some sort of model that they're creating
7:43
whether it's a to-do or a Dog
7:45
or a post or a comment
7:47
that's something that we want to do all the time
7:49
it's not just about showing and hiding content
7:51
based off of if a user is logged in or not
7:54
we also wanna be able to show
7:56
the correct content to user that they created
7:58
or make sure that only the owner of a particular comment
8:02
can delete that comment.
8:03
So that's also coming up next.
8:05
(upbeat music)
