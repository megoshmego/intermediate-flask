ript


0:00
(gentle music)
0:04
- [Narrator] Okay, so now we are going to see the bad way,
0:08
the horrible, do not do this,
0:10
do not repeat what I'm about to show you
0:11
way of implementing authentication,
0:14
it happens to be the easy way out.
0:16
It's simple.
0:17
It doesn't require understanding anything
0:18
about this scary, hashing and salting
0:21
and Bcrypt and SHA and MD5,
0:23
and all these weird things,
0:24
you don't have to care about any of it,
0:25
but also you're leaving yourself
0:27
open to a horrendous security vulnerability.
0:30
So what am I talking about here?
0:32
Well, the simplest way of creating some semblance
0:37
of registration and logging in,
0:39
is to have a form, like I have here,
0:42
where you enter a username and a password.
0:45
And then we take that username and password,
0:48
and we just store it, we just save it in the database.
0:51
So we have a username, we've got an ID, a password
0:54
for this model called bad user.
0:58
And then we have a form, you submit that form,
1:00
this form right here.
1:02
And then we just take that username,
1:04
we take that password as is,
1:06
and we make a new user, we db.session.add,
1:09
db.session.commit.
1:11
So we now have saved that information to our database,
1:14
a username and a password.
1:16
Now, we do need to somehow save something to our database,
1:20
once we see the real way of doing this,
1:22
the safe way of doing it.
1:24
We have to keep track of something
1:25
in order to be able to authenticate year later on,
1:28
years from now or tomorrow, or just a minute later.
1:32
If you've signed up, you need to sign back in.
1:34
But we do not wanna store the password itself,
1:37
like I'm doing right here.
1:39
I am storing the actual password from the form
1:41
in my database.
1:43
This is not good.
1:45
But it does make our logic super easy.
1:47
When somebody tries to login,
1:49
all they have to do is type their username, their password,
1:52
and then we find that user based off of the username
1:55
from the form,
1:57
and then we just check if that password
1:59
is the same password that is stored in the database,
2:02
then they're in, great,
2:04
they are who they say they are.
2:06
That's the simplest way.
2:08
You sign up, let's do it now.
2:10
So I'll make some username.
2:11
How about HarryPotter and then a password?
2:16
I'm not gonna tell you what it is.
2:18
It's going to be hidden here.
2:19
How about,
2:25
okay, so I have a password, I'm going to register.
2:28
I do have the flask debugging toolbar set up
2:31
and I forgot to disable the redirect interception.
2:35
So I will have to click through,
2:37
but without that debugging toolbar,
2:39
it would just redirect me to /secrets.
2:42
Welcome to the Chamber of Secrets.
2:45
And we're seeing some content, whatever this is,
2:47
this is our top secret website, the top secret place
2:50
that we're supposed to be able to access
2:52
after logging in or registering.
2:55
Alright, so now when you go back,
2:57
and this is not, by the way,
2:59
this authentication is only partially
3:01
or the authorization is not actually implemented here.
3:04
I can just go to /secret even if I'm not signed in,
3:08
but if I try and login right now
3:10
with our very bad, bad version of authentication,
3:14
and I put my password and username in.
3:16
I had HarryPotter,
3:18
and then I'll retype my password.
3:21
If I can remember it.
3:25
And login, all right, it works.
3:27
It takes us to secret.
3:29
But what's happening there behind the scenes
3:31
is that there's a literal comparison between strings,
3:35
the password in the form
3:36
versus the password in the database.
3:38
This is not a good idea.
3:41
If we go to my database right now,
3:43
and we select * from bad users,
3:45
we will see usernames and passwords.
3:48
We can do it right now.
3:49
So I have a table here.
3:51
The table that our model corresponds to is, where are you?
3:57
Well, I'm in the wrong file.
3:59
There we go.
4:00
It's called bad users.
4:01
So if we select *
4:04
from bad users,
4:07
there we go.
4:09
I have three users and I can see their passwords.
4:12
WillyWonka123 as a password of CharlieBitMe,
4:15
StevieChicks has a password a bockbock98!!6bock,
4:21
and HarryPotter has a password of IloveDobby.
4:25
Now, this is a disaster.
4:27
in this context of a tiny little app that no one uses,
4:30
okay, whatever, it's not a huge deal.
4:32
But actually, it still is a horrible idea.
4:35
Even if you're just toying around,
4:37
you're making a little thing you're gonna throw up
4:40
to share with friends.
4:41
A little demo just to demonstrate,
4:44
hey, look, I've been learning to code.
4:45
Here's what I've made.
4:46
You never wanna do this.
4:48
You never want people to store
4:49
or you never want to store people's passwords as plain text
4:52
for a couple of reasons.
4:54
First of all, if I have any remotely negative intentions
4:59
or bad intentions as a developer,
5:01
or anybody on my team has access to this database,
5:04
they can see everyone's passwords.
5:07
So they could log in as those people,
5:09
and that might not seem that bad.
5:11
But the second thing that's really important to understand,
5:14
is that a lot of people use the same password
5:16
for multiple sites.
5:18
So yes, in a perfect world,
5:19
people wouldn't, they would create a new password
5:21
for every website, they would use a password manager
5:23
that creates very strong passwords in the first place,
5:26
and it remembers them for them,
5:27
and it allows them to make new passwords
5:30
every single time they register somewhere.
5:32
But it's not a perfect world,
5:34
and the majority of people don't do that.
5:36
So if you did have some bad actor at your own company,
5:39
or if you were a bad actor,
5:40
I guess you probably don't care what I have to say,
5:42
because then you might use this approach.
5:45
But if you're at a company
5:47
and somebody has access to the database,
5:49
yes, they could gain access to Willy Wonka's account,
5:52
on the your application, whatever the application is,
5:56
but if they were able to see Willy Wonka's password,
5:58
they could take that password
6:00
and try it with the same username,
6:02
on a bunch of different websites.
6:03
Or even if the username is different,
6:05
a lot of the time people use the same password,
6:08
and you can buy information
6:09
where you can take someone's username
6:11
and find or attempt to find an email
6:14
that is corresponding with it.
6:16
There's a lot of things that DVS people can do.
6:18
But if you have the password, most of the time,
6:21
people are going to use that password somewhere else.
6:23
And that's where it becomes very dangerous.
6:25
Whether it's a bank account,
6:27
or even just email, stock market trading account,
6:31
or Robin Hood, an application that allows you
6:34
to trade on the stock market,
6:35
I don't know why I'm going to detail about that,
6:36
it really doesn't matter.
6:37
But the point here is that, it's problematic.
6:40
And then you introduce being hacked.
6:43
Somebody gets access to this, who is not at your company.
6:46
It's a huge disaster.
6:48
If you're a company and you're storing passwords
6:50
in plain text,
6:51
and you have thousands or hundreds of thousands
6:54
or millions of users,
6:55
and you're storing each one's password.
6:57
If you're ever hacked, if someone gains access to it,
7:00
who is legitimately full blooded, bad actor,
7:04
they have access to everything about those users.
7:06
They can get into every account,
7:08
they don't have to do any password breaking or,
7:11
you know, real hacking
7:12
after they've just gained access to the database.
7:15
That is like the best pay day on earth
7:17
for a lot of those developers or for those hackers.
7:21
So even if they can't really make money,
7:23
or do something nefarious with your application,
7:26
even if it's just like a blog application,
7:28
or, you know, Reddit, for example,
7:31
where most people don't have credit cards
7:32
associated with their account.
7:34
Still, if somebody were to get your passwords,
7:36
Reddit does not store passwords in plain text,
7:38
but if they did, those hackers, those bad actors
7:42
could sell those passwords,
7:44
or they could attempt to use them on other websites.
7:47
Because of this fact we've talked about,
7:48
people use the same passwords.
7:50
So a password, no matter what it is,
7:53
and what the context is, if it's a Reddit password,
7:56
or I don't know, a Tumblr password,
7:59
it's still valuable to people who have bad intentions.
8:03
So that is why you never wanna store a password
8:05
in plain text.
8:07
One of the remaining justifications
8:10
that you may sometimes come across,
8:13
this stack overflow post that I linked to in the slides
8:15
actually covers this.
8:16
One of the main justifications,
8:18
if a company is asking you to store passwords in plain text,
8:21
is often that they want to be able to
8:24
share that password with the user.
8:26
So you can click, I forgot my password.
8:28
And in the past,
8:30
some websites would just show you the password
8:32
if you you answered a question or something.
8:34
But nowadays, we just reset a password,
8:37
whether it's through email,
8:39
or some other form of, you know,
8:40
two-factor authentication with your phone.
8:43
There are different ways of resetting a password
8:45
if someone can't remember it.
8:46
But historically, that was one of the reasons
8:49
that companies would store passwords in plain text,
8:51
was so that they could actually retrieve them
8:53
and remind you have them.
8:55
But that was kind of a different world.
8:57
And another reason like Verizon,
9:00
apparently used to up until recently,
9:03
they store their passwords in plain text.
9:06
And if you would call in
9:08
and you needed to verify something about your account,
9:11
who you were, they would ask you for the first four digits
9:14
of your password.
9:16
And there's a huge outcry on Twitter and the developer world
9:19
of people saying that that is just absolutely ridiculous,
9:22
and that there's other ways of verifying who somebody is,
9:25
without them reading the first four digits
9:27
of their password out,
9:28
to some, you know, customer service representative.
9:31
So Verizon hopefully has swiftly changed that,
9:34
they said that they did.
9:36
But anyway, you do not wanna do this, right?
9:39
We don't wanna be able to see our users passwords.
9:41
The problem is that this is easy.
9:43
This took I mean, I wrote the code
9:45
and just showed it to you, as it was already running.
9:48
But the logic itself is super straightforward
9:50
to log someone in.
9:52
If we go to app.pi we're simply getting data
9:56
from the form, a name and a password.
9:59
We pull up a user, using that username.
10:01
So baduser.query.filter by username.
10:05
I don't know what I just did there.
10:06
And then we just check if password is the same
10:09
as the stored password.
10:10
The one from the form equals the password in our database.
10:14
If so, great, they're logged in.
10:16
Otherwise, we'll add an error to the form.
10:19
So it's super easy, it's fast to implement,
10:21
but it's a terrible, terrible idea.
10:24
So what we're going to do next,
10:26
now that we've seen the bad idea,
10:28
is talk about what you're supposed to do.
10:30
How do we store something about a user?
10:33
We need to store something resembling
10:35
or based off of or somehow created using their password
10:40
that we can then use when somebody logs in to verify.
10:44
We can't just store a username,
10:46
we have to have some way to verify
10:48
that somebody has the correct password.
10:50
But without storing a password, it's a little bit tricky.
10:53
So we need to talk about hashing and that's up next.
10:58
(gentle music)
