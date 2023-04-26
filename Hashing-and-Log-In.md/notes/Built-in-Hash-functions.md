anscript


0:00
(gentle music)
0:04
- [Instructor] So, Python comes
0:05
with its own built-in function
0:07
called hash.
0:08
This is not something you would use to store passwords,
0:11
once again, but it is still a step up
0:14
from our very silly examples that
0:17
absolutely suck at hashing.
0:19
This is useful in some context.
0:21
So the built in function hash,
0:23
accepts an input.
0:25
We don't need to import anything.
0:27
Let's try hashing a string like penguin,
0:29
and see what we get here.
0:31
And it maps it in 64-bit space,
0:34
so it uses 64 bits in memory
0:36
to store this number in this case.
0:39
And I'll always get that same result
0:42
at least in this implementation of Python.
0:46
It actually will change depending on your architecture,
0:48
the machine you're on,
0:50
and the specific implementation or build of Python.
0:53
Without going too much into detail,
0:56
you should not use this to store passwords
0:57
for a bunch of reasons.
0:58
But the main reasons that you'll get a different output
1:01
depending on where you're running Python.
1:04
So, in this one implementation of Python
1:06
on my machine, every time I hash penguin,
1:08
I'm gonna get the same number out.
1:10
And if I slightly tweak it,
1:13
if I clear my screen,
1:16
to be penguin with an exclamation point,
1:19
we get a pretty different number.
1:21
So again, this is the built-in hash function,
1:24
and it does meet a lot of the requirements
1:26
we're looking for, but it still is unusable
1:29
in terms of storing passwords.
1:32
We don't wanna use this to hash a password
1:34
and store this in our database.
1:36
It's certainly better than storing a plain text password,
1:38
but it is still not good enough.
1:42
First of all, it is using 64-bit space.
1:45
The algorithms that we'll see, at least
1:47
some of them, use double that at a minimum, 128 bits.
1:51
So, much longer outputs.
1:53
Which means if you were trying to reverse engineer,
1:56
if you were trying to brute force your way through,
1:58
you have a whole lot of work in front of you
2:01
compared to trying to brute force your way through this.
2:03
In addition,
2:05
these are relatively prone to collisions
2:08
compared to this built in hash from Python.
2:10
Is relatively prone to collisions It's built to be fast.
2:15
This function is a fast hash function.
2:18
The other ones we'll see in just a bit are not
2:20
they are slow.
2:22
But that's a good thing when we're working with passwords.
2:24
We don't want a hash function to be very fast,
2:27
otherwise somebody could try and brute force
2:30
their way through, try every single
2:31
combination of every string that they could think of,
2:34
get some fancy hardware and machines
2:37
that can just run through millions of computations
2:39
per second, and just try every combination,
2:42
and if it's a fast hash,
2:43
they could find the answer much faster.
2:45
And again, because this space is smaller, 64-bits,
2:49
it's more prone to collisions,
2:51
it's much more likely that we'll end up
2:53
with a duplicated output for a given
2:55
input, or for multiple inputs,
2:57
compared to some of the algorithms we'll see later on.
3:00
So then, what is this useful for?
3:02
This is a bit of a tangent,
3:04
but I think it's worth discussing.
3:06
It's Something that is just good to know about Python
3:09
and programming in general.
3:11
Early on, a couple videos ago,
3:12
I mentioned this idea that a dictionary in Python,
3:16
like D here.
3:18
Where we have keys and values,
3:20
the key here will be name and the value will be Harry.
3:26
And then, we'll have another key
3:29
which will be...
3:30
How about house.
3:33
Will be Gryffindor which I actually...
3:35
How do you spell Gryffindor? I know there's Gryffindor
3:41
I don't know.
3:42
I'm just gonna guess that.
3:44
Anyways, we have keys and values in a dictionary.
3:46
Dictionaries are an example
3:48
of something called a hash map.
3:50
So a hash map uses a hash function in its implementation.
3:55
So, hash maps are very fast
3:58
when we are retrieving data from them or inserting data.
4:02
It doesn't matter if there's ten items,
4:04
ten key value pairs, or thousands of key value pairs,
4:08
they are very fast.
4:09
It takes the same amount of time
4:11
for me to retrieve Gryffindor if I did D of house,
4:17
in this small dictionary,
4:20
compared to a dictionary with ten thousand elements in it,
4:24
and I ran D of house, it would take the same time,
4:27
roughly at least the same time
4:29
for me to get Gryffindor out.
4:30
Now, if we compare that to an array, or a list,
4:34
in order to find something in a list,
4:35
like the last element in the list.
4:38
Or to search for something in there.
4:40
If we're trying to find where house is in a list,
4:43
if there's ten items in there,
4:45
that's gonna be relatively fast.
4:47
And if there's a million items in there,
4:48
we might have to look in a million places.
4:51
The way that Python dictionaries work,
4:53
is that this key here, is actually going to be
4:56
hashed, using this hash function.
4:59
So this string will be hashed,
5:01
and then the output that we get,
5:03
will always be the same output for that one input.
5:06
Python uses this number,
5:09
which is actually binary behind the scenes,
5:11
and this is kind of fudging it
5:13
but it stores Harry at that address in memory.
5:18
So, if we just replicated that,
5:20
hash of name, the string name,
5:24
gives us this number.
5:26
Python takes this output,
5:27
and it stores the value of Harry
5:30
at this location in memory.
5:32
Again, that's very simplified,
5:34
but now every time I ask for D of house
5:37
or D of name,
5:39
is actually what I did here instead of house,
5:41
we will get that same hash.
5:43
So, when I ask for a key,
5:45
and I want the value or I provide the key
5:47
and I want the corresponding value,
5:49
Python will hash this key,
5:51
and then try and find something at that given address.
5:54
So hashes are used outside of cryptography,
5:57
outside of authentication and storing passwords,
6:00
this is an example of that.
6:01
In other languages,
6:03
they're just called hashes instead of dictionary.
6:06
In Python, or in JavaScript,
6:08
we have object literals, we have maps.
6:10
They all operate on roughly the same principle
6:13
of taking some key, hashing it,
6:16
running it through a quick, very fast, hash function.
6:19
Getting that output,
6:20
which is always the same, it's deterministic
6:22
for that one key, we get the same output.
6:25
We take that, or Python takes it
6:27
and stores the value at that location.
6:30
And this is why, we can't use keys,
6:34
in a dictionary, that are not hashable.
6:37
Things that are mutable, for example,
6:39
like a list.
6:41
I can't do this.
6:42
One, two, three.
6:45
Because, list is unhashable.
6:48
It's trying to hash this.
6:50
And if we tried hash of an empty list, we can't do it.
6:54
And if you think about it,
6:55
this is a mutable structure.
6:57
So, I could have a variable,
6:59
we'll call this L, set to my list,
7:01
and if I was able to hash L which I'm not,
7:05
but just imagine I get some output.
7:07
Whatever it is, if I were to change L
7:10
to now be a list that contains some stuff,
7:13
I would get a different output if I were able to hash this
7:16
because now the input is different.
7:18
So, we can't hash mutable types.
7:20
We only can hash immutable,
7:22
like numbers and strings and booleans.
7:24
So that's a quick explanation of how dictionaries work,
7:28
and where this hash comes into play.
7:31
But again, it's still not good enough for us.
7:33
The output is too small, it is too fast.
7:36
One of the few times that you want something to be slow
7:39
is a cryptographic hashing function.
7:42
And, that's too prone to collisions,
7:44
so we will see a better option shortly.
7:47
(gentle music)
