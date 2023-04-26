Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Intro to Hash Functions", the subsection title "Hashing and Loggin In", and the section title "Intermediate Flask"?



0:00
(logo music)
0:04
- Already,
0:05
So if we're not going to store passwords in plain text,
0:08
which once again, embarrassed repeating, it's a horrible,
0:11
horrible, no good and terrible horrendous, disgusting,
0:13
upsetting, bad idea.
0:17
If we're not going to store passwords in plain text,
0:19
how do we store them? Or what do we store?
0:22
We need a way of having a username
0:25
and some something that has to do with the password,
0:28
some scrambled up version of the password
0:31
that we can then check against what the user enters
0:34
into our form, and we can verify if they match or not.
0:38
So if we're not gonna compare password to password,
0:40
CharlieBitMe in the database,
0:42
to CharlieBitMe from the login form,
0:45
what are we going to compare?
0:47
Well, we need to talk about Hashing and Hash functions,
0:50
a Hash function,
0:51
or a Hashing function is a function that takes some input
0:55
and it maps it into some output.
0:58
Let me just read the definition here of a fixed size,
1:02
so we can take some data of any size.
1:05
It could be something small,
1:05
it could be something large.
1:07
So let's just go with an example of a string,
1:09
a one character string, a 20 character string,
1:11
or a hundred or a thousand characters string,
1:14
a Hash function will take that input
1:16
and spit out something that is of a fixed size.
1:20
So let's say it will spit out a number
1:23
between one and one million
1:26
or that's maybe not a great example
1:27
because numbers may not seem like they are fixed size.
1:31
So let's say it will spit out a 10 character string.
1:35
So that input could be one character, it could be 10,
1:38
or it could be a thousand characters.
1:40
A Hash function will spit out a 10 character string,
1:42
at least in our example.
1:45
So that's one requirement of a Hash function.
1:47
It needs to take some input
1:48
and spit out something of a fixed size.
1:51
And here's a simple example, a diagram from Wikipedia,
1:54
it takes in some string like John Smith, Sam Doe,
1:59
how do I get rid of that down there?
2:01
I don't know if I can, there we go.
2:03
Sandra D, these are similar in length,
2:06
but they're not the same.
2:07
And we put them through a Hash function, and in this case,
2:10
it will spit out a number or a memory address.
2:13
It spits something out of a fixed size.
2:15
Let's just say two digit numbers.
2:17
As a quick side note here,
2:18
Hash functions are used all over the place in Python,
2:22
or in JavaScript hash maps.
2:25
We just call it a map, but it's a hash map.
2:27
Or in Python, we have dictionaries a key that we pass in.
2:32
Whatever that key is to our dictionary
2:33
is going to be hashed and that determines how it is stored.
2:37
But anyway, that's just a bit of an aside.
2:39
So a Hash function takes some input and it spits something
2:41
out of a fixed size.
2:44
Then there are a couple other requirements.
2:46
One of the most important
2:48
is that a Hash function is deterministic.
2:50
What this means is that for one input value,
2:53
whatever it is, you must always get the exact same output.
2:57
That's very important.
2:59
So that's a Hash function in general.
3:01
It's a function that takes some input of an arbitrary size,
3:04
small or large,
3:05
and it will spit out something of a fixed size.
3:09
And it will always give you the same output
3:11
for the same input.
3:13
Then within Hash functions,
3:15
there is a special subset called
3:18
Cryptographic Hash functions.
3:20
Now these are used in cryptography
3:21
and they have a couple other requirements.
3:24
One of which is that a cryptographic Hash function
3:27
needs to be a one way function.
3:30
Now, a one way function is a function where
3:32
you go from the input, you stick it through the function.
3:36
I don't know why I said, stick it through the function,
3:38
but you, you pass it to the function and you get an output.
3:41
You can not take that output
3:43
and figure out what the input is.
3:45
A simple example of a one-way function in math,
3:49
in JavaScript is absolute value.
3:51
So we have math dot absolutes or abs,
3:56
which takes some number like three,
3:58
and it will always return the positive version
4:01
of that input.
4:03
So negative three and three,
4:06
both give us the same output of three.
4:08
So if I call math dot absolute value
4:10
on this mystery variable that you don't know, mystery input,
4:12
you don't know the value of it.
4:15
I made it, and then I cleared my screen.
4:17
I cleared the console.
4:19
Can you tell me what the input was?
4:21
We're getting 78.
4:23
What was the input?
4:25
We can't, we can't figure it out.
4:26
It's either negative 78 or positive 78.
4:29
So we've narrowed it down to two things,
4:32
but we can actually figure out exactly what the input was.
4:35
It happens that it was positive 78.
4:38
So absolute value is a simple example of a one-way function,
4:42
but cryptographic Hash functions
4:44
have some other requirements.
4:45
One of which is that they must be one way.
4:48
So hint, hint, we're going to take a password,
4:51
pass it into a cryptographic Hash function,
4:54
which will screw it up in a whole bunch of ways
4:56
to make it unrecognizable, but most importantly,
4:59
it's not a reversible procedure.
5:01
If you have the hashed version, you have the output,
5:04
something that looks like this.
5:06
Maybe you're not going to be able to just reverse that
5:08
and figure out what the input was.
5:11
Unlike. Let's say square roots or squaring something.
5:15
If we have a square function, you pass in seven,
5:18
we'll get 49 out.
5:20
Now, if somebody finds a number like 81,
5:24
and they know that it went through a squaring function,
5:26
they can reverse that they can square root 81
5:28
and figure out the input was nine.
5:30
That is not the case with a cryptographic Hash function.
5:33
So we're going to return to cryptographic Hash functions
5:36
in a bit, but let's just talk in general terms.
5:40
And we'll try and implement our own basic Hash functions,
5:43
which for the record,
5:44
is not something that we'll actually use
5:46
in our own authentication.
5:48
There are a couple of standard algorithms set.
5:50
Almost every company, every website will use.
5:54
So hashing in general is this process we've already covered,
5:58
but in our context, we will be hashing a password.
6:02
So whatever a user types in Charlie bit, me or buck buck 98,
6:06
or I love Dhabi,
6:08
we'll take that password and we're going to transform it
6:11
using a Hash function,
6:12
which will spit out something that looks nothing
6:15
like the password and is not reversible.
6:17
And we store that in our database.
6:20
So that is the key innovation. If you will,
6:23
upon what we have so far,
6:25
we'll store the output of a hashing function
6:28
to our database.
6:29
And then when a user logs in with their password,
6:32
we will also hash that same password
6:35
through the hashing function
6:36
and compare what we have in our database,
6:38
because one of the requirements of a hashing function
6:40
is that we always get the same output.
6:43
It's deterministic for one input.
6:46
So if a user types or password incorrectly,
6:49
it is guaranteed to give us the same output.
6:52
If we're using the same hashing function,
6:54
but you can't reverse engineer it,
6:55
you can't take that hash version
6:57
and figure out what the password was.
6:59
So it's safe to store in our database in the next video,
7:01
we'll try our hand at writing some simple Hash functions
7:04
on our own and see how it goes.
7:06
(logo music)
