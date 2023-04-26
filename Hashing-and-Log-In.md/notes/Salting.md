0:05
- All right, so it's important to note
0:06
this built-in Python hash function
0:08
is not at all acceptable to use to hash and store passwords.
0:12
We'll never write our own password hashing function.
0:15
In fact, there's really just a handful, less than a handful.
0:19
There's just a couple of recommended password
0:22
hashing algorithms.
0:23
They have names, there's dissertations
0:25
and papers written about them and here they are.
0:29
The one we'll be using is called Bcrypt
0:31
we'll talk more about this group in just a bit,
0:34
but Bcrypt is a very popular algorithm
0:36
used for password hashing.
0:38
And you might be thinking, well, it's not a problem
0:41
if everybody knows the exact algorithm that we're using,
0:45
if everyone knows we're using Bcrypt.
0:47
Yes if they had a single password hash,
0:50
like if somebody had this password hash and from scratch,
0:54
they were trying to figure it out what the password was
0:57
they would have to brute force and just try millions
1:00
or potentially billions of potential passwords
1:02
until we get a match.
1:03
But what about if we just went through a dictionary
1:08
or we ran some code for a couple of days or weeks even
1:12
generating just as many passwords as we could think of
1:15
and we hash them, and instead of using Bcrypt
1:19
we'll substitute the built-in Python hash
1:21
just as a simple demonstration.
1:23
So what if we hashed all the common passwords
1:26
everything we could think of
1:27
and then we created a reverse lookup table,
1:31
meaning that we create, let's say just a dictionary
1:33
where we map something like this to the input password
1:37
which in our case was just password.
1:40
So if I save that to a variable,
1:42
we'll call this reverse or maybe just hash table,
1:47
and then I try another password,
1:49
how about password123 another common password.
1:54
And then we put this as a key
1:57
and say that equal to password123.
2:01
And if we repeated this process obviously through code
2:04
we wasn't do this manually, but billions of times
2:07
or at least millions of times,
2:09
we would have a table or a dictionary in this case
2:12
where if we ever had access to somebody's database
2:16
and we could just see the hashed passwords that were stored
2:20
I could take this hash password like this right here
2:24
and call hash table of that results.
2:30
And I could figure out the password.
2:31
So if everybody knows that we're using Bcrypt,
2:34
what is stopping us or at some bad actor
2:37
from spending a little bit of time
2:39
generating a massive dictionary
2:42
that contains all of the possible hashes
2:44
that they could come up with through their code as a key
2:48
and then a value set to that actual password
2:51
that generated this hash.
2:52
I've actually gone through
2:53
and done a very simple version of this
2:56
I downloaded a file that includes
2:58
the hundred thousand most common passwords.
3:01
I actually have a couple of versions
3:02
there's one that has 10 million,
3:05
but it takes a little while to run.
3:06
And it's just annoying to try and record a video
3:09
at the same time.
3:10
So I have a file with the a hundred thousand
3:13
most common passwords and I'm reading it in,
3:16
for each line,
3:17
I am hashing just using the built-in Python hash
3:20
but imagine this was a Bcrypt
3:22
which is what we're about to see.
3:24
And then I store that in a dictionary as the key
3:28
and the value is the password from that file.
3:31
So I'm gonna run this file %run app.py
3:35
And it creates a variable for me called hash table
3:39
where I have stored a hundred thousand...
3:41
they're not all gonna show up here, it gets truncated,
3:43
but there are a hundred thousand items in there.
3:46
Some of them are slightly inappropriate
3:48
if you happen to see them.
3:49
But if we go to the top
3:51
we'll see some of the most common ones
3:52
like password, 12345, qwerty, 1234111111,
3:58
dragon, baseball, football.
4:00
So this could be a little bit of work upfront
4:02
to generate something like this
4:04
especially on a much larger scale
4:06
we're talking about millions and millions
4:09
or maybe even billions of passwords
4:11
that we would run through the hash function,
4:14
whether it's Bcrypt or something else
4:16
and then store the result as a key
4:18
and the password as a value.
4:20
If I were to have hacked into somebody's database
4:22
and I got some hashed passwords
4:25
so things that look like this, again,
4:27
what we get back from Bcrypt actually is a bit different
4:30
it's longer, it will include letters and numbers.
4:33
And anyway, this is a much shorter,
4:37
less memory intensive hash
4:39
it's just the built in Python hash.
4:40
But the concept is the same.
4:42
If I got this from a database,
4:44
if I had this and I don't know what password it is,
4:47
but if I say save this to a variable
4:49
we'll call this mystery.
4:51
And then I have this hash table I've created
4:54
a while ago I generated it.
4:56
And it's just based off of the fact that I know
4:59
the algorithm that's being used
5:00
I could just pass this hash in
5:03
and I can see the password is lucky1.
5:06
And because these hashing algorithms are deterministic,
5:09
I could always get the exact same result, right.
5:11
Lucky when it's hashed or lucky1
5:14
is always going to give me that same...
5:17
Let's just verify that same output,
5:20
which is what I have here.
5:22
So this is potentially a really big issue, right.
5:26
If everyone knows we're using Bcrypt
5:28
why not just spend some time
5:29
going through every single password
5:31
you could ever come up with,
5:32
run it through Bcrypt and then store the password
5:35
and the hash that we get as a result
5:38
in a way that we can easily figure out the password
5:40
based off of a hash, if we have the hash.
5:43
Well, fortunately this will not be an issue
5:46
because of something called salting or password salts.
5:50
When we are working with these hashing functions,
5:52
things like Bcrypt,
5:53
we will include something called a a salt.
5:56
And a salt is just a random string that is introduced
5:59
before the hash actually happens.
6:01
So this is not a Bcrypt hash or the output
6:05
this is a simple hash that we've built a hashing function
6:09
it's called salting hash.
6:10
It just uses a slightly better hash function
6:13
from last video, two videos ago.
6:15
So it is not at all secure, but it demonstrates the concept.
6:20
We have a password like penguin1,
6:22
and instead of just hashing penguin1 directly,
6:24
we generate a random salt, just some other characters,
6:28
and we can catenate the two together, and we hash that
6:32
and then we get something else as a result.
6:35
And the point of doing this
6:37
is to make it much, much harder
6:39
for somebody to do what I just showed you here,
6:42
because now when we're hashing the password,
6:45
if this is my application
6:47
I'm the one who was trying to prevent attacks,
6:49
I'm not just gonna hash lucky1
6:51
I'm going to hash that password,
6:53
plus some other random stuff, and then store that.
6:58
And then when a user logs in,
7:00
they'll give me their password
7:02
and I'm going to add that same password salt back in
7:05
and hash that and compare the results
7:08
from what I have stored in my database.
7:10
So the hashing of the salt really just serves the purpose
7:13
of preventing me from doing something like this,
7:17
where I have a table with all the common (chuckles)
7:22
with all the common passwords
7:24
with the hash that was generated from them
7:28
because we are not going to store hashes like this
7:32
we will store a hash that is a password
7:34
plus a bunch of random other characters.
7:37
And then when we go to retrieve that password,
7:39
or use that same string of random characters,
7:41
hash it alongside the user's password and compare.
7:45
So we introduced this element of additional randomness
7:48
and just odd few station that makes it a lot harder
7:51
to do this sort of an attack.
7:54
There's also something called a rainbow table
7:55
which I won't go into,
7:56
but it's a more sophisticated version
7:59
of this sort of approach.
8:02
So salting helps prevent those issues.
8:05
So here's a demonstration.
8:07
All that we do is pick a random string of characters
8:11
and then we hash that in with the actual phrase
8:15
with the actual password,
8:16
this is just our silly implementation,
8:18
but it does give us a different result
8:20
if you notice here,
8:22
penguin1 is the password each time,
8:24
the same exact password we add in that salt,
8:27
and we get back something relatively different
8:31
it's not radically different.
8:32
Obviously they both start with qovo,
8:35
but still slightly different.
8:37
Now, the other use case for including a password salt
8:40
is that, or just salt in general,
8:43
I guess it's not technically called a password salt,
8:45
but the other reason to do it
8:47
is that a lot of people have the exact same password
8:51
and that could be very problematic.
8:53
I mean, if we go by this list here, let's go to the top
8:58
I mean, there's gotta be millions of people
8:59
or at least tens of thousands of people
9:01
who have 123456 or password or qwerty as their password.
9:07
So if we were just directly hashing this and that was it,
9:10
that could be a big problem
9:11
and those people go to sign in
9:13
or if they go to create an account or whatever it is,
9:16
we'll be hashing the same password
9:18
and storing the same result.
9:20
But when we introduce a salt,
9:22
a random string of characters into that string
9:24
and then hash the results,
9:26
it's incredibly unlikely that we'll ever have a collision
9:30
based off of that initial password.
9:32
So this is exactly what Bcrypt does
9:35
when we work with Bcrypt we'll pass in a password
9:38
or a string or whatever it is that we're trying to hash,
9:41
but it does not just hash that exact string.
9:44
It generates a salt, some random characters,
9:47
it puts them together, it hashes that
9:49
and then it tells you exactly what it did.
9:51
So it gives you the result, the hash result
9:53
and it tells you here's the salt that I used.
9:56
And a lot of people get confused by that
9:58
they think why would it tell you the salt
10:00
isn't it supposed to be secret?
10:02
Shouldn't you hide that salt?
10:05
We'll talk more about that.
10:06
But remember the point is just to make it harder
10:09
for somebody to do this sort of an attack.
10:11
It is not a secret that you're salting passwords.
10:15
It's just the element of randomness
10:17
that makes things a lot more difficult.
10:19
All right,
10:20
so next we're actually going to see Bcrypt in action
10:22
and we'll talk more about cryptographic hash functions.
