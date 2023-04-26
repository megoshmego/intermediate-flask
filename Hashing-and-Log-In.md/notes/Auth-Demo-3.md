0:00
(cheerful music)
0:04
- All right, so next up, we've got login.
0:07
So, the first thing we'll probably want to do
0:09
is start with a route for login.
0:12
App.route/login is fine.
0:18
And we'll add our methods
0:20
and this'll be a get in post as well.
0:23
Get post.
0:27
And then, def login_user.
0:31
And, we'll begin by just rendering the form.
0:33
And we're using the same form, which is Userform.
0:36
Again, you may want different forms for registration
0:39
versus logging in if you want additional information
0:42
from a user when they register.
0:44
It would be really annoying if you had to type
0:45
your address, and your email, and password, and username,
0:49
and full name, and birth date to login.
0:53
And right now that would happen
0:55
if we added something to our Userform.
0:57
So you may want separate forms.
0:59
But this is fine enough for now.
1:01
And, we can start by just returning render_template again
1:05
and we'll do login.html and we'll pass our form.
1:09
So next up, we need to make that template,
1:12
which will be login.html.
1:16
And, I think I'm just gonna copy the entire register HTML,
1:20
which is a bit lazy,
1:22
because this form logic here, it's not really a logic,
1:25
but the form markup with our Jinja loop
1:28
and the hidden tags is kind of 100% duplicated.
1:32
It's not kind of duplicated, it's entirely duplicated.
1:36
So, if I weren't recording a video
1:38
and trying to keep this brief,
1:40
I would move this into its own template
1:42
and include that template both in register
1:45
and login, assuming that we wanted
1:48
the exact same layout and the exact same form in both cases.
1:51
And then I would just change this up right here
1:55
and just display login.
1:57
I probably don't need a lead.
2:00
Actually, you know what?
2:01
We may include a link here.
2:03
Login below.
2:06
Don't have an account?
2:09
Register here.
2:12
And we'll put a link.
2:14
Let's just put an anchor tag there for now.
2:16
Anchor tag and the route is slash register.
2:21
Alrighty, let's see if we can just view that form.
2:25
So, slash login.
2:27
I haven't actually set up my nav bar links yet.
2:31
Login below.
2:31
Don't have an account?
2:32
Register here.
2:34
All right, so that's taking us to sign up.
2:37
Now, we need to implement the login logic.
2:40
So, in our app.py, very similar pattern,
2:44
just like with any time we use the form,
2:47
we're going to need to validate on submit.
2:49
So, if form.validate_on_submit,
2:54
we'll want to get the username from the form.
2:56
Username equals form.username.data
3:00
and the password.
3:01
Password equals form.password.data.
3:05
But then, instead of creating a new user
3:07
or registering a user with that class method,
3:11
we're going to call user.authenticate
3:15
with that username and with that password from the form.
3:20
And remember, user.authenticate is going to try
3:23
and find a user with that username
3:25
and then call bcrypt.check_password_hash
3:27
with the form username here against the database username.
3:32
And hopefully that returns true.
3:33
In which case we returned the actual user object,
3:37
the model that was found in that table.
3:41
So, we're going to call if user.authenticate,
3:44
so we're gonna save that to a variable,
3:46
let's call it U or user, lowercase user.
3:50
And then, if user,
3:53
we'll start by just returning a redirect
3:57
to slash tweets as well.
4:00
And if it doesn't work,
4:02
I'm going to add to form.username.errors,
4:05
which will automatically be displayed in my templates.
4:08
If we look at it here for error in field.errors,
4:11
we print them out and I'll just add in an error
4:14
like, invalid username/password.
4:22
Great.
4:24
So that will be our feedback.
4:25
And, if we hit this else,
4:27
this code is going to run,
4:29
because we redirected here and if,
4:31
so none of this will run,
4:33
but if you have invalid credentials,
4:35
if there is no user that's returned
4:37
from user.authenticate,
4:38
meaning your username or password is incorrect
4:41
or not found, then we add to the errors
4:44
and then the form is re-rendered.
4:47
So, moment of truth here, let's try it.
4:50
I'm gonna refresh and try logging in
4:52
with the correct credentials that Chrome saved for me.
4:56
And it works!
4:57
If I go back and I try this
4:59
with some incorrect credentials,
5:01
let's change the password.
5:03
I'm just gonna delete a character.
5:06
It's not working, it's refreshing the page
5:09
and telling me invalid username password.
5:12
A quick tweak that I would make to the form.
5:15
And this is what's kind of annoying
5:16
with the way my form is set up right now.
5:18
I'm going to have to duplicate this
5:20
in two different places.
5:22
What I'm going to do is add a paragraph in
5:24
with the class of form-text, and then, text-danger.
5:30
Since it's an error, I'll just make it red.
5:33
And then I'll put that right there.
5:34
Also while I'm here, I should change the submit button
5:37
to say login instead of register.
5:41
And, let's see how that works.
5:43
All right, I'm gonna submit again
5:45
with incorrect credentials
5:47
and now I get invalid username or password in red.
5:51
Okay, that looks pretty good.
5:54
Next, I think actually, I might change this
5:56
to be a span instead of a paragraph.
5:58
Let's see.
6:01
Just gets slightly less spacing there.
6:04
And, I'm just gonna do the same exact thing
6:07
with the errors on our register form.
6:11
So, we have to duplicate it,
6:13
which is kind of obnoxious,
6:17
but it's not too bad.
6:18
So now, we have our login logic working.
6:21
I'm able to register,
6:23
I'm able to login, but the thing is
6:26
I could be viewing this from a private window.
6:28
For example, I can still get to slash tweets.
6:32
Well, I'm logged in right now,
6:33
so I can get there,
6:35
but I could get there from any window,
6:37
any computer with or without an account,
6:40
we are not remembering who is logged in.
6:43
We're not remembering anything about
6:45
really anything at all.
6:46
We don't, we can't differentiate
6:48
if somebody is logged in at all,
6:49
or if they're not logged in.
6:51
So next, what I'd like to do is gate this tweets page,
6:55
so that you have to be logged in
6:56
to view a tweet or view all tweets.
6:58
Otherwise, we'll redirect you.
7:00
So, that's coming up next.
7:01
It involves session.
7:03
(cheerful music)
