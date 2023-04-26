
Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Intro-to-Bcrypt", the subsection title "Hashing and Loggin In", and the section title "Intermediate Flask"?

0:00
(upbeat music)
0:04
- [Instructor] Next up, let's focus in
0:05
on cryptographic hashing functions.
0:08
So there's hashing functions
0:09
and then cryptographic hashing functions are a subset
0:12
where there are a couple other restrictions.
0:14
We've talked a little bit about this early on.
0:16
But one of the most important is that a small change,
0:19
the tiniest possible change in input
0:22
is going to radically alter the output.
0:25
So there is no way that we could figure out something like,
0:29
I'm just gonna use hash here, the built-in hash function.
0:33
Let's say that hash or password gives us this,
0:38
we should not be able to figure out,
0:39
okay, well, we got negative 2749,
0:43
and somehow map that to P or pass
0:46
or figure out that we're close to the password
0:49
that we're trying to crack.
0:51
There's no way that we should be able to look at the output,
0:53
and compare that to another output,
0:56
and use that to get any information about the inputs,
1:00
there should be no association.
1:02
And the tiniest change to the input
1:04
should radically alter the output.
1:07
So as an example here, the output of hashing penguin one
1:11
might look like this and that's using this salt.
1:15
The output of penguin two is completely different.
1:19
So at the end, we have the salt here,
1:21
we'll talk more about that.
1:22
But the actual hash results looks nothing like
1:25
what we had above.
1:27
It's just one character different,
1:28
but there should be nothing similar, no pattern,
1:31
no way that we could reverse engineer it
1:33
and compare these two and figure out,
1:35
oh, these must have come from similar passwords.
1:38
Okay, then, we also have the salts of course,
1:42
which the hashing functions we'll be using, Bcrypt,
1:45
will generate a new salt for us each time a random salt.
1:49
So even if the same salt was used, however,
1:52
which will not be the case, but here we have xab one seven,
1:55
which will be hashed alongside penguin one.
1:57
Same salt with a slightly different password,
2:00
very different output.
2:02
Same password penguin two,
2:04
we give it a completely different salt,
2:06
which is what Bcrypt will do, completely different output.
2:09
So even if people have the same exact password penguin two,
2:13
we could have thousands of users,
2:14
though each have a different salt included,
2:17
and the corresponding, the resulting hash
2:19
will be very different.
2:20
There'll be no connection or correlation,
2:23
no logical conclusion we can come to
2:25
based off of these outputs.
2:27
So if we got a database, and we saw all of these strings,
2:30
all of these hashed passwords,
2:32
there's nothing that we could tell about the input
2:35
based off of these outputs.
2:37
Now, there's just a couple
2:38
very popular cryptographic hashes.
2:41
One is called MD5, there's another family called SHA.
2:45
There's different variations, like SHA 256.
2:49
These are very fast cryptographic hashes,
2:52
they're actually not suitable for storing passwords.
2:55
And we'll talk about why in just a second.
2:56
They are used however, SHA as an example is used in
3:00
a lot of cryptocurrencies, like Bitcoin.
3:03
It plays a very, very important role in the blockchain,
3:08
and mining for Bitcoin, and authenticating and securing
3:12
the transaction history of Bitcoin.
3:15
So those are examples of cryptographic hashes.
3:18
And within cryptographic hashes, we have password hashes
3:21
like Bcrypt with that we'll be working with.
3:24
Argon2,
3:25
Scrypt.
3:26
These are very slow, compared to things like SHA.
3:30
SHA 256, as an example.
3:33
And that seems like a bad thing.
3:35
It seems like you don't want a very inefficient slow
3:38
hashing function.
3:39
But that's actually not true,
3:41
you do want something that is slow.
3:42
And when we talk about slow,
3:44
it's not gonna like slow your application down
3:46
from a user's perspective,
3:48
but when we are thinking of people who are maybe setting up
3:51
a dedicated computer with super fancy hardware,
3:55
with the sole goal of cracking passwords,
3:57
and they're going to brute force their way through,
4:00
I don't know, a couple hundred thousand
4:01
or a million computations a second,
4:04
we want to slow things down as much as possible.
4:07
So a fast hash would be worse in terms of security,
4:12
because it would be faster to try
4:15
and brute force your way through somebody's password
4:17
and figure it out.
4:18
So Bcrypt, Argon2, Scrypt are all slow hashes.
4:22
And that is what makes them suitable for storing passwords.
4:26
Now, the one we'll be using is called Bcrypt.
4:28
It's been around since either 1999 or 2000.
4:32
So 20 years at this point, a very long time.
4:35
And you might also think, well, that sounds like
4:38
I shouldn't be using it if it's been around so long.
4:41
However, actually, over the last 20 years,
4:43
it's only gone on to gain more notoriety
4:47
and security experts still recommend it to this day.
4:51
Here's a nice Stack Overflow post on the security.
4:53
I guess it's not technically Stack Overflow,
4:55
but security dot Stack Exchange.
4:57
So this is for security professionals.
5:00
Now this was in 2014.
5:03
So still a little while ago, but this person was asking,
5:06
if Bcrypt has been around for so long,
5:08
it seems like maybe that's a problem and it's dated.
5:13
However, this person has written a very nice response
5:16
that talks about why Bcrypt is so great.
5:19
Mainly, it is slow and it aims to be slow.
5:23
So it wants to be as slow as possible for the attacker,
5:25
while not being intolerably slow for honest systems.
5:29
Obviously, you could come up with some insanely
5:31
slow hashing function that took seconds or minutes,
5:35
but then logging in would be miserable,
5:37
signing up would be miserable on a website
5:40
from our client perspective.
5:42
But we wanna make something slow enough that it is harder
5:45
for an attacker to just brute force their way through.
5:48
And they talk a little bit about some of the other hashes
5:51
like SHA 256, which is used in Bitcoin, as I mentioned,
5:55
it can be very efficiently implemented on a GPU.
5:59
And that's exactly why people who are into bitcoin mining,
6:04
buy thousands and maybe hundreds of thousands of dollars
6:07
worth of GPUs.
6:09
So Bcrypt is different.
6:11
You cannot buy fancier GPU or a bunch of GPUs
6:16
and have more success at trying passwords,
6:19
because Bcrypt does not rely on GPU usage,
6:23
or it's not as GPU centric,
6:25
which makes it harder for somebody to just,
6:27
set up a little farm and mine their way through
6:31
your password.
6:32
All right, so here's another kind of fun post to talk about.
6:36
Somebody is asking, "Mathematically, how long would it take
6:38
"to crack a Bcrypt password hash?"
6:41
If you set up a machine, and you just had it
6:43
trying every single possible password it could come up with,
6:46
on average, how long would it take to crack a password,
6:49
if you only had the hash, and you're trying to figure out
6:52
how to generate that resulting output hash?
6:55
So this person is talking about some article
6:58
that says an 8X and video setup blah, blah, blah,
7:01
can calculate about 100,000 Bcrypt hashes per second,
7:04
which is very slow compared to
7:07
how many times you could calculate a SHA5 or SHA 256 hash
7:11
as an example.
7:12
In conclusion, I'll just jump to the chase here,
7:14
cut to the chase,
7:15
you need four years of running a computer non stop
7:20
trying to hash over and over and over,
7:23
brute forcing your way through a password to figure out
7:25
what the input was that resulted in the output,
7:28
your target output, on average, four years.
7:32
Now, this was about two years.
7:34
Yeah, this is a post that's two years old.
7:36
And we're gonna to talk about something called cost factor
7:39
or work factor in the next video.
7:43
So you might be thinking, well,
7:44
don't people have fancier computers now?
7:46
Definitely, absolutely things have improved.
7:49
So this number would go down if it weren't for
7:52
the increase in something called the cost factor
7:54
or work factor.
7:55
Anyway, hopefully this has demonstrated to you
7:58
that Bcrypt is, yes, it's old, 20 years old,
8:01
it's still very popular, and it's still safe.
8:04
That doesn't mean it's impossible
8:06
for somebody to figure out a password.
8:08
But it means that it is exceedingly difficult,
8:12
especially if you are using good passwords
8:14
and you're not using password or one, tow, three, four
8:16
as your password.
8:18
Alrighty, so next we're gonna play around
8:20
with Bcrypt in code
8:21
and we'll actually see how we can hash a simple string
8:24
and get some results and we'll go from there.
8:27
(upbeat music)!
