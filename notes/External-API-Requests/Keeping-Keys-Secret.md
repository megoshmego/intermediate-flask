0:00
(bright happy music)
0:04
- So with these API keys,
0:06
one of the most important things to keep in mind
0:08
when you're working with them
0:09
is that you don't want people to know these keys
0:12
especially if your credit card is hooked up to them.
0:15
And that's one of the main reasons
0:16
we make a lot of these requests from the server side
0:19
so that a user who is using our application
0:22
won't be able to see the actual request to the API.
0:26
They'll see a request sent to our server.
0:28
The server then makes a request
0:30
with the correct API keys then gets back data
0:33
and then responds back to the client with that data.
0:37
So our server is an intermediate that is making the request
0:40
with this private API information,
0:42
the key is the secret whatever else.
0:44
But what about if we're putting our code on GitHub,
0:46
if I'm sharing this with you
0:49
or somebody is putting their code on GitHub
0:52
and they're using a fancy API key for Twitter
0:55
or for Spotify or whatever it is,
0:58
where there's a credit card hooked up to it?
1:00
That could be problematic.
1:02
So instead of storing that file in Git,
1:04
and tracking it and putting it on GitHub,
1:07
we do not wanna do that, we can hide it.
1:10
One of the simplest strategies
1:11
is to just make a separate file to store your API keys
1:15
and then import that file into your app.py
1:19
but don't tell Git about that file.
1:21
Make sure that it's part of your Git ignore.
1:24
For example, we could have a secrets.py file,
1:27
put our API secret keys in there,
1:30
whatever it is Twitter, Facebook, Google APIs,
1:33
put the keys in there.
1:35
Then in our Flask app or whatever app
1:38
where we're importing and using at API key,
1:40
we can import it from secrets import API secret key.
1:45
So in Python's world, it doesn't matter,
1:47
it's just coming from a different module.
1:48
The secrets.py file, but it still works.
1:52
Then we can just use this variable.
1:54
But the key part here is to make sure your gitignore file
1:57
includes secrets.py.
2:01
Then when you add to Git, when you commit,
2:04
when you push to GitHub, that file should not be tracked,
2:07
it shouldn't show up if you type git status or git add
2:10
it should not be included.
2:12
So if you push your code to GitHub,
2:14
all a user will see or a developer, is this right here
2:18
from secrets import API secret key.
2:21
And if they try and run your application,
2:23
they're going to get an error
2:25
or 400 or some sort of status code,
2:27
when they try and make an API call,
2:29
because the secret key is not defined.
2:32
It's a variable from this file
2:34
and they'll know they need to make that secrets file.
2:37
And if you are making an application and writing
2:40
and putting it on GitHub and it requires a secret key
2:43
it's usually a good idea to let other developers know.
2:46
Clone this repository make a secrets.py file
2:49
in the root directory and include your Twitter API key.
2:54
Just so they know the steps they need to go through
2:56
to recreate what you have.
2:58
So this is a very important step
2:59
if you do plan on putting your code on GitHub,
3:02
but also if you're working just on something locally
3:04
it's best not to track your API secrets
3:07
or your keys with Git period
3:09
even if you're not pushing up to GitHub.
3:11
And these days GitHub has some features
3:13
where it will actually look at all of the files
3:17
that you're uploading to GitHub
3:18
and it sends you an email.
3:20
I can't guarantee it we'll do this for every API,
3:23
but for some APIs that it knows
3:25
are hooked up to credit cards
3:27
and people might be scouting and searching across GitHub
3:31
trying to find schmucks who have included their secret keys.
3:35
GitHub will actually look for that
3:38
and send you an email saying,
3:39
Hey I noticed you included this API key.
3:42
You really need to get rid of that.
3:45
For some of these APIs like AWS, Amazon Web Services
3:48
that's all hooked up to a credit card.
3:50
And if somebody's got that API key
3:53
and used it, they can rack up a bill.
3:55
Like if they're trying to mine for Bitcoin, for example
3:58
that could be thousands of dollars on your account.
4:01
And Amazon is maybe going to work with you,
4:03
but you're going to have to make a case
4:05
and explain it to them.
4:07
Because at the end of the day, somebody used that key
4:09
and spent a lot of money and resources.
4:12
So definitely, definitely be careful about this.
4:15
It's nothing scary.
4:16
Just make a secrets file
4:18
and import it and make sure Git ignores that file.
4:22
But I'm not going to do this here
4:24
just to keep things simple.
4:25
I'm going to put the direct API key
4:28
in my app.py just so you can see it
4:30
and you could rerun this key or rerun this code rather.
4:33
If you download it
4:35
without having to make your own key
4:37
this is not tied to a credit card
4:38
so it's not the end of the world.
4:39
Worst case we just hit the max
4:41
of 15,000 requests in a month.
4:43
That's not a huge deal.
4:45
But in general, do this trust me.
4:48
You don't want to be on the receiving end of a crazy bill.
4:51
I've seen students who have had this happen to them before,
4:54
who did not follow instructions.
4:57
And it was not a good experience for them.
4:59
Some of them were able to get refunded
5:01
but some of them weren't.
5:03
So just be careful.
5:05
I know that's a little scary sounding
5:07
but it should be, this is important.
5:09
You don't want to spend money you don't need to spend.
5:12
People are looking for keys on GitHub.
5:14
They're looking for it online.
5:16
And if they find them, they're going to use them.
5:18
Okay, enough scare tactics.
5:20
In the next video we're going to integrate
5:22
our MapQuest API with Flask.
5:25
(bright happy music)