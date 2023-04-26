0:00
(gentle music)
0:05
- [Instructor] Hey, welcome back.
0:06
We are onto a very important topic that I'm sure some
0:09
of you have been looking forward to,
0:10
or at least anticipating being able
0:12
to incorporate into your own applications.
0:15
We were talking about authentication,
0:17
hashing and login to be more specific.
0:20
We're gonna focus quite a bit actually
0:22
on how all of this works with the end goal of building
0:27
an application where a user can log in and log out
0:29
and register and all of that.
0:31
But rather than just showing you some code that you can copy
0:33
and paste and use as a template, we're also going to try
0:37
and understand what is actually going on,
0:39
which does take a little bit
0:41
of digging and some explanation.
0:43
So let's start with our basic goals.
0:45
It's really just two.
0:46
We wanna understand hashing, what it is,
0:49
how it works at a high level.
0:51
Talk about some hashing algorithms, what the point is.
0:53
And then we'll end
0:55
by actually implementing authentication and authorization.
0:59
We'll talk about those two terms
1:00
in Flask using an algorithm called Bcrypt.
1:04
Let's start off with a discussion
1:05
around these two terms right here.
1:08
Authentication and authorization.
1:10
These are related usually, but they're not the same thing.
1:14
Authentication is simply being able to verify
1:17
that somebody is who they say they are,
1:20
at least based off of their email and password
1:22
or username and password,
1:24
whatever the actual credentials are.
1:26
It's a way that we can have a gate on our application
1:29
that says, I need you to tell me who you are,
1:32
I need to know that you are the person that you say you are.
1:35
So authentication is just the ability
1:38
to sign up for an account and log in or log out
1:43
to remove that authentication or be unauthenticated.
1:47
Authorization has to do with permissions.
1:49
So once you are verified you are who you say you are,
1:53
that doesn't mean you have free reign in an application.
1:56
As an example, here's a Reddit.
1:59
Once again, I am not signed in,
2:02
I don't have permission to do anything.
2:04
If I try and join a subreddit,
2:06
it's gonna ask me to register.
2:09
I don't even know if it'll let me...
2:10
Yeah, if I try and upvote something,
2:12
it's gonna ask me to register.
2:14
This is Reddit way of telling me, I don't know who you are,
2:17
I need you to sign up.
2:19
Then we have authorization.
2:20
So if I do sign in, once again with the throwaway account,
2:24
that's not my real account, CatDogChickenGuy,
2:26
but it is an account in Reddit or on Reddit.
2:30
I can do things like join the soccer subreddit.
2:33
I can create a comment.
2:36
Right here, I could type a comment.
2:38
I can upvote, but I can't delete this comment.
2:43
I can't delete the entire post.
2:45
I could delete a post if I made it.
2:48
If I created a comment right now,
2:49
I could delete that comment, but I only have authorization
2:53
or permission to do certain things.
2:55
So it's not like I have the run of the application
2:58
as soon I've verified who I am,
3:00
there are still are permissions around this.
3:02
And it's not just users to users, regular users.
3:06
So I can't delete this comment,
3:08
but McWaffel, what is that?
3:11
Waffeleisen can delete that comment.
3:14
But then we have moderators on Reddit
3:16
who have special tiers of permission.
3:19
So they can remove a post, they can remove any comments.
3:22
They have probably a special dashboard.
3:25
I'm not a moderator,
3:26
but they probably have a different URL that they can visit
3:29
for mods that I couldn't visit.
3:31
If I tried to go to that URL,
3:33
let's say r/soccer/mods, that's not, it I'm almost positive,
3:38
but whatever it is, I don't have permission to be there,
3:42
and I would get redirected back somewhere else.
3:44
So authentication is, you are who you say you are.
3:48
Authorization is, do you have permission to do this thing
3:51
or to view this page or to delete that or update that?
3:54
So we will learn how to do both.
3:56
Authentication is definitely the trickier bit.
3:58
It involves having someone sign up and register
4:02
with a username or an email and a password,
4:04
and we have to talk about security
4:06
and how do we store information around passwords?
4:09
We don't store the password itself.
4:11
Definitely, definitely don't do that.
4:13
But we have to talk about it.
4:14
It's a little trickier.
4:16
Then authorization, it comes down
4:19
to the logic of your application.
4:21
It comes down to things like conditionals.
4:23
Like if this person is a moderator,
4:25
show them the mod button.
4:27
If this person is not the owner of this comment,
4:31
hide the delete button.
4:33
So that is definitely easier.
4:35
But in this video, I just wanted
4:36
to introduce the two concepts.
4:38
So next we are going to learn a horrible,
4:41
no good, disgusting, bad way
4:44
of implementing authentication on your own.
4:47
I'm going to say this again at the beginning
4:49
of the next video, but I wanna be very clear now,
4:51
what you're about to see in the next video is
4:54
how you are not supposed to build authentication
4:57
and I'm using it as a demonstration of why it's a bad idea
5:01
and why not to do what I'm about to show you.
5:03
So please do not watch the next video and then just try
5:07
and implement that and skip the rest of this section.
5:09
It is just a preface to the real way of doing auth.
5:12
Okay, that's next.
5:14
(gentle music)
