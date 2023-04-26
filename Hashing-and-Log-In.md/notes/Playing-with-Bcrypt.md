Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Playing with Bcrypt", the subsection title "Hashing and Loggin In", and the section title "Intermediate Flask"?



(upbeat music)
0:04
- [Instructor] Alright, so we've established
0:06
that we'll be working with Bcrypt, 2 hash
0:08
and store our passwords in our applications that we built.
0:12
It is safe, it's very commonly used, it's popular
0:16
and there are implementations of the Bcrypt algorithm
0:19
in pretty much every programming language
0:21
that you could want.
0:22
So there is a Python version of Bcrypt.
0:25
If you're wondering how the algorithm works by the way,
0:28
it's very complicated to explain.
0:30
I wish I knew enough to explain it.
0:32
It's based off of a popular algorithm called
0:35
the Blowfish cipher, hence B
0:37
and then crypt this, it's a different password algorithm
0:42
and in 2000 there was 1999 or 2000
0:45
there was a dissertation where the sky created Bcrypt
0:49
and basically combined the Blowfish cipher
0:52
with this other thing called crypt.
0:53
It really doesn't matter but in order to implement Bcrypt,
0:57
if you wanted to try and write the algorithm
1:00
you have to understand how to work with binary
1:03
just as at a start.
1:04
You need to understand working with bits
1:06
and binary math.
1:08
So we're not going to get into that
1:11
we don't have to,
1:12
and that's the point of using a popular existing algorithm.
1:17
We have implementations all over the place,
1:19
including Python that we can use.
1:21
So we will install Bcrypt.
1:23
You don't have to do this step,
1:25
we're actually going to use a flask wrapper
1:28
just like the SQLAlchemy, and then Flask-SQLAlchemy,
1:30
there's WTForms and then Flask-WTF
1:33
there's Bcrypt and then a Flask version,
1:36
but we'll play around with just plain old Bcrypt
1:38
in I Python for a moment
1:40
so I'm going to install it.
1:41
PIP, install Bcrypt
1:45
and open up
1:46
I guess I already had it here
1:48
open up by Python and we'll import Bcrypt
1:52
and then we have a couple of different things that we can do
1:54
but let's start by just importing it
1:56
import Bcrypt.
1:59
Alright.
2:00
So Bcrypt uses salts, as we've talked about,
2:04
there's a method called bcrypt.gensalt.
2:08
So this will make us a password salt.
2:10
Let's just call it salt = bcrypt.gensalt
2:16
and if we look at salt, this is our password salt.
2:20
Notice this B here.
2:22
This means that this is actually a string of binary.
2:26
It's just being represented here
2:28
in a much more condensed form.
2:30
If it were in binary, it would be very, very long
2:33
to print out.
2:35
So that generates a salt.
2:37
Remember that is just a random string
2:39
that is included alongside our password
2:42
when we actually hash things together.
2:45
So then let's say we have some password,
2:48
password equals
2:51
how about a monkey
2:54
pepper
2:55
78.
2:57
That is our password.
2:59
Now technically Bcrypt wants this to be a binary string
3:03
so if we put a B right there
3:06
look at password it's a binary string now
3:09
that's what that B indicates just like we had here
3:12
Well, we didn't write this
3:13
but we got her back from bcrypt.gensalt.
3:16
So now we have the password
3:17
let's imagine this is coming from a user
3:19
and then we have a salt and we generate a new salt
3:22
every time we're going to hash a password
3:25
then we can call bcrypt.hashpw, hash password.
3:29
We pass in the password and a salt.
3:31
So bcrypt.hashpw we pass in our password and the salt
3:40
and this generates us
3:41
I don't know if you saw, it took a little bit of time there
3:44
it's going to generate the resulting hash
3:47
and it is relatively slow.
3:50
The fact that we can notice it's taking a bit of time,
3:53
maybe a split second is important.
3:55
That is very slow when you compare it
3:58
to everything else we've done so far.
4:00
At least in I Python, we get a result immediately.
4:04
So this is our hash password at least this part is here
4:08
and we're gonna talk more about
4:09
what the individual pieces mean
4:11
so assuming we pass in the same password and the same salt
4:14
we always will get the same output.
4:17
It has to work that way of course
4:19
otherwise we wouldn't be able to authenticate a user
4:21
so we will never store their password
4:23
but we will store this string
4:25
and what's kind of confusing and seems counterintuitive
4:28
is that the string actually includes the salt.
4:30
So we don't have to store the salt separately,
4:33
Bcrypt will be able to figure out the salt from the string
4:36
and then use that,
4:38
and then when we pass in a password from a user,
4:40
let's say somebody types monkey pepper 78 into a form,
4:43
hit submit to login,
4:45
we will look them up by their username
4:47
find what we've stored in the database,
4:49
which will look like this
4:50
and then we'll pass this password to bcrypt
4:53
alongside this
4:55
and bcrypt will figure out the salt
4:57
it will hash monkey pepper 78 with that salt,
5:00
just like we did here
5:02
and then check if we get the same output.
5:04
So we have to get the same output.
5:05
It has to be deterministic, but if we generated a new salt
5:09
let's call this new salt = bcrypt.gensalt
5:17
and then I try to hash password the same exact password
5:20
but with new salt, we get something radically different.
5:25
Now, it might look like it's the same at the beginning
5:27
and it is the same, but we'll talk about what these mean,
5:29
this is just sort of metadata
5:32
it's an indicator that we're using bcrypt
5:34
and this 12 has to do with the work factor
5:37
we'll go over it, don't worry.
5:39
But if you look at the actual hash that we get
5:42
they're completely unrelated.
5:45
There's a different salt
5:46
and you can see the end has changed here
5:48
after that slash this is a portion that indicates the salt.
5:52
So that is very important that we have a salt included
5:55
otherwise, if somebody else had the same password
5:57
monkey pepper 78, we would get the same output.
6:01
So let's talk more about Work Factor.
6:04
Bcrypt is supposed to be slow as we've talked about,
6:07
and it is slow relative to other
6:09
cryptographic hashing functions.
6:11
However, computers speed up over time,
6:14
they get much faster and potentially much better
6:17
at brute forcing their way through a password.
6:20
If it's just a matter of how many operations
6:22
how many times you can hash something per second,
6:24
five years ago, I'm making this up,
6:26
but let's say that it's
6:27
a hundred thousand operations per second with bcrypt
6:30
nowadays, if you had a lot of money
6:32
maybe you could buy something that a computer that could do
6:35
a million per second,
6:36
again, making those numbers up completely
6:39
but that wouldn't be an unheard of,
6:40
to have a 10 times improvement over the years
6:43
and certainly things have gotten much faster
6:45
since the year 2000 when Bcrypt was first implemented.
6:49
But fortunately, we have a solution to address this.
6:52
We can specify how many rounds of hashing of encryption
6:56
that Bcrypt should use.
6:58
So there's a default,
6:59
this is known as the work factor
7:02
and the default right now is 12 in our library
7:05
that we're using,
7:06
however, you can actually change that,
7:09
you just specify rounds equals 14.
7:12
So when we generate a salt
7:14
we can specify the number of rounds
7:15
14 is as far as I could tell in 2020,
7:19
it's very early in 2020,
7:20
but I was trying to do some Googling today
7:22
and this is a recommended number
7:25
and again, this just indicates how many rounds of hashing,
7:28
basically the difficulty level of this hash.
7:31
So it slows it down even more
7:33
and that's how we can keep up with increasing speeds
7:36
in computers and even if you left it at 12,
7:39
it's still going to be extremely difficult
7:42
for somebody to break their way in.
7:45
So when we look at the resulting string that we get back
7:48
there's quite a bit here.
7:50
We have the beginning part
7:52
prefix 2b
7:54
that is always going to be the same.
7:56
That is just identifying the result as a Bcrypt hash.
8:01
Then we have the work factor, which is defaulting to 12
8:04
We can see there.
8:06
If we look at our output, we have 2b
8:08
yes, it's Bcrypt and then a dollar sign
8:11
that's kind of like a space here, or you can take of it
8:14
it's just like a separating character
8:16
and then another dollar sign 12,
8:18
that's a number of the rounds of work.
8:20
So if I generated a new salts and I set rounds to be 14
8:26
and then I do the same thing, bcrypt at hash password
8:29
the same password monkey what'd we call it
8:32
monkey pepper 78 with this new salt
8:35
that takes significantly longer
8:37
I don't know if you can see that
8:39
and we have 2b at the beginning, still bcrypt,
8:43
but now 14 rounds.
8:45
If I set rounds to two,
8:48
Oh, it won't let me go down that low will it?
8:50
Looks like four is the lowest or five, let's see
8:54
and try it again with that new salt
8:57
it's very fast.
8:58
We can see there's basically no delay
9:02
and then if I went higher,
9:03
what's the highest I can go?
9:04
30, I'm not gonna go that high.
9:06
Let's just do maybe like 18.
9:12
It's going to take quite a while.
9:14
So the relationship here, each new, additional round
9:18
it's not just going to add like the same amount of time.
9:21
Things ramp up significantly each time we add a new round
9:24
as you can see there, that was very slow
9:27
and so if a user was doing this,
9:29
or if we're logging in a user
9:31
or registering their account and having to hash something
9:35
that's kind of a long time to wait, but 14 is pretty fast.
9:41
It won't be an issue.
9:42
So also included in our password here or not the password
9:46
the resulting hash is the salt, of course
9:49
and then the hash.
9:50
Remember this salt has to be in there
9:52
we have to store it somewhere
9:54
in order to authenticate a user later
9:56
it's just to make things harder
9:58
to make things more difficult to crack
10:01
so that you couldn't just hash a bunch of common passwords
10:04
and then use that as a reverse lookup
10:06
to figure out what somebody's password is
10:09
based off of the hash that you have from the database.
10:12
We introduced this salt each time
10:14
a different salt each time,
10:16
and that salt needs to be stored so that we can use it
10:19
in order for someone to log in
10:21
they'll give us their password.
10:23
We'll take the salt, Bcrypt does this automatically
10:26
so we don't really have to do much
10:27
and you'll see how this works.
10:29
All we need to do is store this string
10:31
and then we pass this string along with a password
10:35
that a user has typed into a form to bcrypt
10:37
and we tell bcrypt is this a valid password
10:41
that would generate this hash
10:42
while it will look in the hash, find the salt,
10:45
take that salt, hash the password that was passed in
10:47
and then compare the results.
10:49
So the result includes information
10:52
not just the hash result of the password or of the string
10:56
also the version or not even the version
10:58
just the fact that it's bcrypt, the number of rounds
11:01
and then it also includes the salt in here and the hash.
11:05
Anyway, this doesn't really, really matter
11:07
that you understand every single piece of how this works.
11:11
I was having a conversation with a developer
11:13
I won't name him or her earlier today about this
11:17
and we were just at lunch and I was talking about
11:21
teaching Bcrypt and authentication,
11:23
and they made a remark of,
11:26
"wow, I don't think I know any of that."
11:28
They might've used some profanity.
11:30
"I don't know any of that stuff,
11:32
"it just works and it's one of those things
11:34
"that I don't need to worry about."
11:36
We're not writing this algorithm, we're not maintaining it
11:39
so at this point, you may know more
11:41
than the average developer who is not in security,
11:45
who is not focused in this area.
11:48
For a lot of people is just a big mystery
11:50
and they just follow tutorials and they just get it to work
11:53
but hopefully the last few videos
11:55
I know it's been kind of a lot
11:56
talking about hashing functions and salts and all of that
11:59
but hopefully it's helped you understand
12:01
the mechanics of all of this
12:03
because yes, you don't have to understand it
12:05
in order to implement it,
12:06
we're just gonna use a simple library.
12:09
All we do is say hash this password, we store the results
12:13
and then basically we call a method like log in
12:17
or verify password
12:18
and that's it.
12:19
We get true or false and it's super simple
12:22
but I think it's important to understand how it works.
12:25
Otherwise it's just this big mystery,
12:27
it seems like it's all magic.
12:29
There's a part of it that's magic
12:30
because we don't really understand the ins and outs
12:33
of the Blowfish cipher and a Bcrypt,
12:35
but we still have a bit of an edge
12:37
over the average developer here.
12:39
All right.
12:40
So next we will actually implement authentication and flask
12:43
I'm gonna show you some slides first
12:45
here's a little preview
12:46
of how we would set up auth
12:47
and then we'll go through
12:48
and do it actually as a code alone.
12:50
(upbeat music)
