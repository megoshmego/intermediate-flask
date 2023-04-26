0:00
(upbeat music)
0:04
- [Instructor] Next step,
0:05
let's add in a Registration Form
0:07
as well as a Login Form.
0:09
and connect them so we're gonna use What The Forms
0:12
and then combine that with our user model,
0:15
the register method, the class method
0:17
and the authenticate class method.
0:19
And we'll add our first basic routes
0:21
and hopefully connect things and get it working.
0:24
So I have a new forms.py file
0:27
and I've already imported
0:28
the things I know I need.
0:29
I need flask_wtf,
0:31
I want a PasswordField and StringField.
0:34
So instead of doing two StringFields,
0:36
PasswordField will allow us
0:38
to just create a password input on the client side
0:41
so that we get those little dots
0:42
when you're typing
0:43
instead of the actual password showing up,
0:46
and I'm going to use the InputRequired validator
0:48
because I want username and password
0:50
to both be required.
0:52
So I'm gonna define my class for the form
0:55
and I'm just gonna go
0:57
with one form called UserForm.
0:59
Usually we would have
1:01
or often you have a separate register form
1:03
from a login form.
1:04
When someone registers
1:05
you may wanna capture other information
1:07
like their first and last name,
1:09
there a security question.
1:12
I don't know their birthday,
1:14
whatever, their address
1:15
depending on the needs of your website.
1:18
And then when they log in,
1:19
it's just simply username and password.
1:21
So we could easily have a separate register form
1:24
and a login form.
1:25
But in our case, I'm gonna keep it simple.
1:28
Our User Model doesn't have anything else to store on it.
1:30
We don't have email,
1:31
we don't have address or any of that.
1:34
So just UserForm,
1:35
which just inherits from FlaskForm.
1:40
And then we're going to have
1:41
a couple of different fields, really just two
1:44
we need a username field and a password field.
1:48
Already, So username equals,
1:51
and that will be a StringField
1:52
and the label will be Username.
1:55
And then we'll add in our validators,
1:57
which will be equal to InputsRequired.
2:00
And then I'm just gonna duplicate this
2:03
but change that to be password.
2:06
Uppercase it just to match
2:09
both of them InputRequired.
2:10
And this one should be a PasswordField.
2:14
There we go.
2:15
So username equals StringField
2:16
password equals PasswordField two labels,
2:20
and both have one validator
2:21
which is they are both required.
2:25
And in our app.py let's import user form.
2:29
So from forms import UserForm,
2:33
now let's implement our routes.
2:35
So I'm gonna start by defining
2:37
the register routes
2:40
@app.route('/register', methods=['GET', 'POST'])
2:44
And I'm gonna make this both a Get
2:46
and Post route,
2:47
just like we saw with the, during the
2:50
what the forms content.
2:51
We talked about how we can have one route
2:53
that handles the form
2:55
as well as the same route or the same URL path
2:58
but as it get request,
2:59
which will serve the form itself.
3:02
So we'll go with def register_user():
3:07
And in here, we're going to initialize our form,
3:11
form= UserForm()
3:15
And then we'll just begin with the get version
3:18
where we'll just make sure
3:19
we see a form showing up.
3:21
So form equals UserForm
3:22
and then return render_template('register.html')
3:32
All right, next, let's go into our templates folder
3:36
and make that file
3:38
register.html
3:40
And before I forget
3:41
we should absolutely pass it in the form
3:44
form equals form.
3:45
Hopefully this is all review
3:47
from the what the Form Section
3:49
and then in register,
3:51
just gonna copy what I have in my index to save some time
3:54
we extend base.html
3:56
and then we'll put our
3:59
sign up or register or something.
4:01
Probably give this a bootstrap class.
4:04
How about display one?
4:06
And then we want to add our form
4:08
but let's first make sure that
4:09
so I guess my server's not running it?
4:12
let me get out of here.
4:14
Flask run.
4:16
Let's make sure if I go to slash register
4:21
I see Sign Up and I do.
4:23
Alright,
4:24
so now we need to render our form.
4:27
So I've added the basic form in
4:29
it is a form with method of Post.
4:32
It will submit to the same URL that we're currently on
4:35
which is /register as a GET request.
4:37
It served this as template in the form.
4:40
So it now just submits a POST request.
4:41
We've got our CSRF token here
4:44
the hidden tag that generates that.
4:46
And then for each field in the form,
4:48
we're going to ignore the hidden ones.
4:50
We'll make a paragraph
4:52
field.label put the field there.
4:54
And then if there's any errors,
4:56
we'll display the error as well.
4:58
Now I'm gonna change a couple of things.
4:59
So we have our button, typical submits.
5:02
We may give it a class equals to btn, btn success.
5:08
Let's just take a look at the form first.
5:09
That's showing up here.
5:11
Okay.
5:12
And it looks okay.
5:14
Not very bootstrapy except for the button.
5:18
Let's also add in a class on our fields.
5:23
So we can do that by passing in, what is it?
5:27
Class underscore set to form control.
5:32
There we go, we're getting our bootstrap form now
5:34
we can worry about styling it later.
5:37
Maybe we'll add a tiny bit of text up here, a paragraph
5:41
the class of lead, which is a bootstrap class.
5:44
And how about, Register below to join our application!
5:53
I guess that's kind of self-explanatory.
5:56
There we go.
5:57
Okay. So we have our form now.
6:00
And if we submit it at the moment
6:02
if we just get the exact same template rendered
6:05
it is actually hitting our routes right here
6:07
but it's supposed to request, which is fine.
6:10
We're not discerning between them.
6:10
We're not doing any validation.
6:13
We simply render the same template, no matter what.
6:15
And you can see it as a Post request.
6:17
If I try and refresh the page,
6:18
it tells me that little warning
6:19
are you sure you want to resend that request?
6:22
So it definitely is a post request that's working.
6:25
Now we run our,
6:26
if form.validate on submit():
6:32
if that's the case
6:34
then we want to get the username from the form.
6:38
Username=form.username.data
6:41
and the password from the form
6:46
password=form.password.data
6:50
And then we wanna call
6:52
user.register
6:54
We'll save this to a variable
6:57
maybe we'll call it something a little more explicit.
6:59
How about new_user= user.register( username, password)
7:07
Then we will db.session.add(new_user)
7:13
And then db.session.commit()
7:17
We don't need to pass anything in.
7:20
Technically there is a scenario where this would fail.
7:23
There's at least one I can think of,
7:25
which is if the username is already taken
7:27
and you're trying to register.
7:29
Right now we're not handling that
7:30
we we'll get an error.
7:32
So that's something I definitely would implement
7:35
if I were you, but to save time
7:36
I'm not gonna do it now
7:38
but just keep that in mind.
7:39
you could have an issue.
7:41
And so you probably would want to do some error handling
7:44
and re-render the form with an error that you could add in.
7:49
Okay,so db.session.add(new user)
7:51
db.session.commit()
7:52
And then this is a Post request for making it to this point.
7:56
We usually wanna redirect somewhere
7:58
and especially if we're creating a new user,
8:00
it makes sense to redirect
8:02
to some page that we wanna show a new user
8:05
we'll do a /tweets,
8:07
which does not exist yet.
8:09
So I'll make that template,
8:12
tweets.html
8:14
And so let's see, what do we have here?
8:17
Let's just copy maybe from index.html
8:23
and just change this to be viewing tweets.
8:29
We'll just see if that shows up when we try and register.
8:33
And also what's nice to do is to send a flash message.
8:37
So flash, how about,
8:39
('Welcome! Successfully Created Your Account').
8:42
Also, I need to return that redirect.
8:45
If I don't, we won't be redirected
8:48
and I don't have the tweets route yet.
8:51
So let's just set that up just to get route
8:54
@app.route('/tweets')
8:59
And then def show_tweets(): or something.
9:07
return render_templates("tweets.html")
9:13
Already, let's see what happens.
9:15
I'm gonna try,
9:18
so we'll register.
9:20
How about, blue the cat
9:24
and her password will be,
9:27
Iamcat123.
9:31
Already,
9:32
Pray with me.
9:34
Ah, it worked!
9:36
so Chrome is asking me if I wanna save
9:38
for sure that will just make it easier.
9:41
I guess our flash message is a little hostile looking.
9:44
It looks a bit scary
9:45
because it's currently, I think every flash
9:48
that we do in the base template has an alert danger.
9:53
So we can worry about that when we style things
9:55
and make it look better but it worked.
9:57
We got to this page
9:59
let's go to our database,
10:01
select star from users, blue the cat is there
10:04
and we've got our B crypt hash stored for the password
10:07
and an ID for blue
10:09
So next step we'll work on login.
10:11
(upbeat music)
