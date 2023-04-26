Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Dynamic Python Code", the subsection title "Python Wrap-up", and the section title "Intermediate Flask"?



Skip navigation
Search




Avatar image


0:01 / 7:36

Transcript


0:00
(soft music)
0:05
- [Instructor] Just like we did for Flask,
0:06
I wanna spend a little bit
0:07
of time talking about Python and focusing
0:10
on the features or some of the important things
0:12
that we didn't actually cover.
0:14
Out of the box, Python is a lot bigger,
0:17
has a lot more methods and a lot more libraries.
0:21
The standard library includes dozens
0:23
of different modules out of the box compared to JavaScript.
0:26
So there are some things
0:27
that we definitely have not covered.
0:29
Now we did cover all of the essentials,
0:31
all the basics that you need to write applications in Flask
0:35
and interact with the database and all of that stuff.
0:39
But there's still a lot of things that we left out.
0:41
So as we move on to Node JS and we return
0:44
to JavaScript syntax,
0:45
even though we'll be writing node
0:47
and it won't be running in the browser,
0:49
it's still very similar.
0:50
It is JavaScript.
0:51
I shouldn't say it's similar.
0:52
It is JavaScript.
0:53
We'll be moving away from Python.
0:55
So this will serve as a little end cap
0:57
on our time with Python, a lovely, lovely language.
1:02
So Python in general is a very high-level language.
1:05
High-level typically refers
1:07
to how close a language is to assembly code or machine code.
1:12
Those are two different things,
1:13
but they're both low, low level languages.
1:16
Whatever language we're working in, at least the majority
1:19
of languages at some point will be turned
1:21
into code that looks like binary,
1:23
that is written in binary
1:25
that our computers actually understand.
1:28
So Python is very far away from that chain.
1:31
Other languages like C are closer to assembly code.
1:35
Python is a very easy to read language as we've seen.
1:39
I think the syntax is very nice, clean, neat,
1:43
understandable, compared to even something like JavaScript
1:46
which is also a high-level language,
1:49
but certainly compared to languages like C,
1:51
reading and writing Python
1:52
in my opinion, at least is a real joy.
1:55
It's a pleasure to work with.
1:57
And then you add in all the different methods
1:59
and standard libraries that it comes with.
2:01
It's just a nice experience.
2:04
So it's also a dynamic language.
2:06
This is what I wanna focus on in this video.
2:08
We haven't seen this before,
2:10
but we can actually write code
2:12
that will create different methods,
2:14
different classes as the code is running.
2:17
So they're not predefined.
2:19
Python is dynamically typed as we've seen.
2:22
We can have a variable just like in JavaScript
2:24
that starts out as an integer or a string
2:27
and it can switch at some point.
2:30
So this is the same as JavaScript.
2:32
I can have some variable x, which will be a number.
2:35
And then later on, it's now a string.
2:38
Some languages that is a big no no,
2:41
but in Python that's allowed
2:44
which is not necessarily a good thing by the way.
2:46
It might seem like that's nice.
2:47
It does give us flexibility, but it's pretty rare
2:50
that you actually want
2:51
to have some variable that changes type.
2:54
It's not unheard of definitely,
2:56
but most of the time, if something's a string
2:58
it's gonna stay a string.
2:59
If something is a number, it will stay a number,
3:01
but it's important to note it is dynamically-typed.
3:05
It's also a strongly-typed language.
3:07
Compare this in JavaScript to what we get in Python.
3:12
If we take a string
3:13
and we add the number three to it.
3:16
In Python, we just do some string plus a number,
3:20
it yells at us.
3:21
We get an error.
3:23
It tells us I can't do that.
3:24
You can't take an integer and add it to a string.
3:27
It's not going to try and coerce them
3:28
to a common type like our friend JavaScript.
3:32
And in the next video, we'll talk about this last bullet.
3:35
Python is a compiled language.
3:37
But let's return to this bullet here, dynamic.
3:40
We can run a script or have a script that runs
3:43
and creates its own functions and classes
3:46
that are not predefined.
3:47
So I have a very simple demo of this.
3:50
I have a class called Animal.
3:52
Animal takes a species and a noise.
3:55
So cat and meow, dog and there is woof.
3:59
And then it just sets those attributes,
4:01
self.species is species, self.noise is noise.
4:04
But then what it does is it creates a method
4:08
on this particular instance. So let's say this is the name
4:11
of my cat blue with the name meow.
4:15
So I have a method called blue.meow.
4:20
And that only exists on blue.
4:22
If I had another animal.
4:24
How about a pig called tammy.
4:27
Animal is a pig.
4:30
Noise is oink.
4:32
I end up with a method on tammy called oink.
4:36
So we easily could just define a method called make noise
4:40
and have that be a standard method on all of our animals.
4:43
We call make noise and it could do the same thing.
4:46
It's just gonna print the species says self.noise.
4:49
So the cat says meow, the pig says oink,
4:52
but the method name
4:53
is dynamically created based off of what we pass in.
4:57
If you wanna look at the code,
4:58
it really hinges on this line here, setattr,
5:02
set attribute on self.
5:04
Inside of init, self refers to the instance blue or tammy.
5:10
The name of the method that we're creating
5:12
is self.noise.
5:14
So meow or oink.
5:16
And then we set it to this method,
5:18
def make_noise, which is created.
5:21
This function is defined inside of init.
5:24
The intricacies here don't really matter,
5:27
but basically this is just a placeholder.
5:30
We're defining a method here or a function
5:32
and then associating it with the individual instance here.
5:36
Anyway, if I try this out, let me just get rid of that.
5:42
I'm gonna run this code in Ipython.
5:45
Clear, %run animal.py.
5:51
And I look at blue, dir blue.
5:55
Blue has noise and species and meow,
5:59
dir tammy, noise, species and oink.
6:04
And if I call tammy.oink,
6:07
the pig says, oink,
6:08
blue.meow, the cat says meow,
6:12
but I can't call blue.oink.
6:15
It doesn't work.
6:16
And if I created some new animal.
6:19
What's another animal noise?
6:22
It's complicated by the fact that things like dogs,
6:26
the name of their noise would be bark,
6:29
but the actual noise they make usually is woof
6:33
or orf or something.
6:35
So our method does not account for that.
6:37
It just uses the name meow and prints that out
6:40
or oink and oink.
6:42
How about a cow?
6:43
Animal is cow, noise is moo.
6:46
We'll save that to a variable.
6:48
A name for a cow.
6:50
How about bessie.
6:54
And bessie now has a method called moo.
6:57
The cow says moo.
7:00
So this may seem like a not super useful thing.
7:03
And in this situation, it's really not.
7:06
It would be easier just
7:07
to have a method called make noise,
7:09
especially you know,
7:10
if I had a loop with a bunch of different animals
7:12
and I wanted to have each animal make a noise,
7:15
this would be really obnoxious
7:17
where each animal has a completely different method name.
7:20
But there are situations where this can be useful.
7:22
And I just wanted to point out that it's a thing,
7:25
it's kind of cool.
7:26
It's not something we've talked about at this point,
7:28
but it is possible in Python.
7:30
(soft music)
