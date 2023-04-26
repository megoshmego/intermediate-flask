0:00
(upbeat music)
0:04
- [Narrator] So lastly,
0:05
I'll make a couple small styling tweaks.
0:08
Also I guess it's not pure styling.
0:10
Right now one of the first things I wanna address
0:13
is the fact that all of our flash messages are in red
0:16
they look like warnings or danger flashes
0:20
which we probably don't want, at least not in every case.
0:23
So if you can recall back when we covered flashing,
0:26
we talked about including a category
0:29
when we actually call flash,
0:31
you can add a second argument like error or danger,
0:34
warning info success I mean,
0:36
you can add whatever you want.
0:37
But if we're using bootstrap, the bootstrap alerts
0:40
have different varieties based off of those class names
0:44
like primary secondary success, danger.
0:48
So let's do that.
0:50
Let's add a category when we flash so let's see,
0:53
please login first, I think it makes sense
0:55
for that to be danger.
0:59
When we created tweets, we'll probably flash success,
1:06
make that all lowercase for our class names.
1:09
When you need to login once again,
1:12
that will probably be danger.
1:15
When a tweet has been deleted, we could do success.
1:20
I might just do info for some variety here.
1:23
When you don't have permission, we'll do danger.
1:28
When you have created an account, we'll do success.
1:34
And do we have other flashes?
1:36
Yeah, welcome back.
1:38
When we're welcoming someone back,
1:40
maybe we'll do primary just to see what that looks like.
1:43
And is that it?
1:45
Here we have goodbye when you sign out,
1:49
info maybe are primary, let's see how those look.
1:52
So in our flash messages on the base template
1:56
where we're actually looping over every flash message,
1:58
all we need to do is add a second parameter here,
2:02
we are going to unpack the tuple
2:05
that we're already getting from get flash messages,
2:07
or just ignoring the second argument
2:09
or the second value in that tuple.
2:11
If you ever have concerns or questions about it,
2:14
I would have just screwed it up
2:15
because I thought messages first and then category.
2:17
It's very confusing but category is first,
2:20
even though we pass category and second
2:22
when we actually call flash.
2:24
It's weird to me, category comma message in messages.
2:28
So category, comma message, or you can name this whatever.
2:35
And then here, instead of doing alert danger every time
2:38
we'll do alert, dash, and then category.
2:44
Now, this will require us to specify
2:46
the category every single time we flash,
2:49
we may want to set up a default,
2:51
you could easily do that just in here.
2:54
You could just say if not category, category equals,
3:01
I don't know, info primary, but let's check it out now.
3:07
All right, so I'm gonna refresh, and let's log out.
3:12
Oh, too many values to unpack expected to,
3:15
I'm forgetting this parameter we need to pass in
3:17
with categories equals true.
3:20
With categories equals true, we'll try that again.
3:27
And we get goodbye.
3:29
Let's login, okay?
3:33
That's our primary, I'm not crazy about that color
3:37
maybe success makes more sense,
3:39
but let's create a new user we'll sign up.
3:44
How about I guess Dogfan one,
3:50
and password will be wolfwolf23.
3:55
We'll save that.
3:56
Alright, we're getting success now,
3:58
and I think that's pretty much it.
4:01
We've now seen all of them right, primary info.
4:03
If I log out, and I try and go to slash tweets.
4:08
Don't have permission, we're getting our danger,
4:10
that looks good.
4:12
Alright, so that was one thing I wanted to handle.
4:14
Next, let's log in again.
4:17
Let's display the tweets in a slightly nicer way.
4:21
We don't really have much to display,
4:23
we're not saving a date when a tweet is created,
4:26
we don't have user avatar photos,
4:28
it's really just a username and the tweet text.
4:30
We don't have anything else.
4:32
Normally, we would probably add a column
4:34
to the tweet table or the tweets table
4:37
that includes a date when something was created,
4:40
and we could display that an avatar
4:44
is pretty common on Twitter for the username,
4:47
hashtags, the number of likes,
4:49
number of retweets, all that stuff,
4:52
but we just have the text and the username.
4:55
So I'm gonna just make a simple card from bootstrap,
4:59
it's really not for exciting,
5:00
just gives us a little border.
5:02
So it's a div with the class of card,
5:04
div with a class of card body.
5:06
So in the tweets, HTML template,
5:09
instead of making an LI with a bold tag,
5:14
where do we wanna put them all in?
5:15
Probably put a div first,
5:18
and then another div inside with card,
5:23
and then card text or is it body,
5:25
I already forgot, card body.
5:28
And then we'll just move this stuff,
5:31
this bold tag down to the form with the if
5:34
all of that into the card body.
5:38
No idea how this will look.
5:39
Let's cross our fingers and take a look.
5:42
All right, we could definitely use a bit more spacing there.
5:45
Also, I think we should add the card title as the username.
5:51
So card title, H5 or it doesn't have to be an H5
5:55
but something with a card title
5:58
instead of a bold tag for the username,
6:01
so we'll get the username out of here,
6:05
we'll put our tweet text in card body
6:07
but we'll make an H5 or something with card dash title
6:11
and put the username there.
6:13
How does that look?
6:15
Hmm, I don't know about that.
6:19
Let's see, card title is supposed to go in the card body
6:21
so that's part of why it's a little screwed up,
6:25
and then we have a card text class,
6:28
so we're missing that.
6:30
So let's add card text around our tweets,
6:33
so paragraph with card text
6:35
and we'll put the tweet text right in here.
6:40
Alright, looks basically the same, and is this an H5?
6:45
It's not very bolded at all,
6:48
that card title class doesn't seem to be doing
6:51
a whole lot for us, is it?
6:53
Interesting well, we could make it bolded,
6:57
we could give it a different color
6:58
maybe text info, we'll make it look better.
7:01
All right, that looks okay.
7:03
And we could just put a fake subtitle down there.
7:07
We don't have a subtitle to actually display,
7:10
but down below each title, we could put something like
7:15
how about date goes here.
7:22
Alright, so there is a single tweets,
7:25
we might wanna make the text a little bit larger,
7:28
but we won't mess with that.
7:30
Let's add a little bit more spacing between the cards,
7:34
so on each card, we can add a margin Y
7:38
so we could do margin top,
7:40
this is a bootstrap helper class.
7:42
Margin y will be top and bottom,
7:44
let's see what two looks like.
7:47
Maybe a bit more four,
7:51
yeah, I think that looks alright
7:53
and right now I don't have any tweets I've created
7:56
so I'm not seeing the delete button, let's now create one.
8:01
Just do some gibberish, post the tweets.
8:05
Alright, well I think that's okay,
8:08
maybe we can get some inspiration from bootstrap.
8:12
So they do a card link at the bottom, what about a button?
8:17
I know there's some examples with buttons,
8:20
and that's just a button in the card body.
8:23
Well, that's not very helpful.
8:25
Is there anything else that we could do?
8:28
Yeah, I guess we'll just add what we have already,
8:31
it looks okay.
8:33
Maybe we could make this a delete icon,
8:38
so I think we're gonna need to import Font Awesome,
8:40
I don't think we get any icons anymore
8:42
with bootstrap, do we?
8:43
So I'm gonna include Font Awesome
8:46
in my base HTML templates.
8:48
It's just a CSS style sheet so I'll do a link tag
8:52
with that as the href,
8:54
and let's find one that we like
8:56
an icon that we like on Font Awesome that's free,
9:00
we don't have access to the paid ones.
9:02
So let's look at delete.
9:07
Yeah, I guess a trash cans fine maybe this,
9:11
which is, what is it?
9:14
FASFA dash trash.
9:17
So we'll go to the icon or to the button here
9:20
where are you, on tweets.
9:23
Here's our button instead of an X,
9:25
we'll put an icon tag in there,
9:26
the class of FASFA dash trash.
9:30
And there we go, we're getting the delete button,
9:33
we may wanna just put it up with the title
9:37
or the username or next to the tweets,
9:41
who knows where that would go best.
9:43
We could try moving this, put this entire if
9:47
up in the tweets, card title, that could be okay.
9:54
I don't know, we're just playing around at this point.
9:57
Let's see how that looks.
9:59
Yeah alright, that's get enough.
10:01
So we can delete the tweet and there we go.
10:04
And that's kind of it,
10:06
we could style the form of course make this look nicer.
10:09
Right now the cards aren't exactly centered,
10:13
and nothing is responsive.
10:15
If we look at the cards,
10:16
they're in this container right here,
10:19
they're in a UL, I thought I change that to a div honestly.
10:23
So there's still a UL, yes there is.
10:24
So we don't need this extra div.
10:28
Let's get rid of that right there,
10:30
and then we'll put a div around all of them
10:34
and then we'll end that div right there,
10:38
and they should be yeah all right,
10:40
now everything's centered.
10:42
I guess now we really could play around
10:44
with the sizing if we wanted to
10:46
but I think this has gone on long enough to be honest.
10:49
So this is good enough yeah,
10:51
we've got our simple Twitter there's no real homepage,
10:53
but that's fine.
10:54
One issue that we do have with signup
10:57
is at the moment if I use a username that already exists,
11:01
and try and register, whoa boy, we get an error.
11:05
This is coming from our duplicate username,
11:08
we can't have that in our database,
11:10
we have our uniqueness constraint
11:12
that says a username must be or cannot be duplicated,
11:16
it must be unique.
11:18
There's a couple of options for how we could fix this,
11:20
you could add in a custom validator for the form
11:24
where we could actually check if a user name was unique
11:27
before we even tried to create a user.
11:29
However, if we have tons and tons of users
11:32
in our database that could be a little slow.
11:35
What we could also do, just as a simple fix for now
11:39
is except this error except with an E not accept
11:43
but except and we could try to commit this new user.
11:48
And if we get an integrity error,
11:50
then we can add to the form error saying
11:52
username must be unique, and render the form again.
11:56
So in order to except this particular error,
11:58
if you notice it's SQL alchemy dot exc dot integrity error,
12:03
we need to import it.
12:04
So from SQL alchemy dot exc for exceptions,
12:09
import integrity error.
12:12
Then when we have our register route here,
12:16
before or when we try and commit,
12:18
this is where the error is generated,
12:20
that's when we're actually trying to save it,
12:22
insert it into our database
12:24
and we get an error coming from SQL
12:26
from Postgres saying, hey you can't do that.
12:28
Then SQL alchemy, wraps up that error
12:31
and shows it to us here,
12:32
duplicate key value, blah, blah, blah.
12:34
So we can try that, and then we can except
12:39
that error that we just grabbed integrity error,
12:43
we don't wanna just accept everything,
12:45
it's better to be more specific.
12:47
So we could have some other except
12:49
or another exception that we're looking for like,
12:52
I don't know a connection issue with the database
12:55
or who knows what, there's other things that could go wrong
12:58
especially if we have other specific data,
13:01
like we have right now it's just username
13:03
that you're submitting and a password,
13:06
but if we're asking for an email,
13:07
maybe email needs to be unique,
13:09
maybe it has to be a valid email
13:11
like an actual email that we're testing,
13:14
so there are different things that we might wanna accept.
13:17
But if that's the case, we will add to the form,
13:20
dots and then it is, what's the field?
13:23
To username dot errors and we can append to that
13:27
so list and something like username taken,
13:32
please pick another.
13:37
And then we will render that form.
13:40
So return render templates and it's register dot HTML,
13:46
I do need to pass in my form here as well.
13:48
Alright, one more attempt.
13:51
Register user name taken, please pick another,
13:55
keep trying that username taken,
13:57
lets pick some other username Dogfan three,
14:00
and that does work, awesome.
14:04
So there's a lot of other edge cases and things
14:06
you would need to protect against
14:07
and honestly, our view function is getting quite long.
14:10
So I would definitely recommend moving
14:12
some of this logic out,
14:13
but just to make it easier for you to follow,
14:15
I'll just keep it all contained here.
14:17
But as you do make larger apps,
14:18
you absolutely wanna think about keeping
14:20
your view functions as logic free as possible,
14:24
and move most of the functionality out
14:26
into separate methods, whether it's a class method
14:28
or just a standalone function somewhere,
14:31
just keep them clean and brief whenever possible.
14:34
And I think I'm gonna end it here.
14:35
So there's still a lot we could add and again,
14:37
you do have a Twitter clone project coming up,
14:40
but hopefully this was an informative demo.
14:43
I know it's been long but we had a lot of moving pieces
14:45
to put together already, goodbye.
14:48
(upbeat music)
