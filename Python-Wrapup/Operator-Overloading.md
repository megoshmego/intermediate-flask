Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions, as well as your own demonstrations of the code? Would you also please include the video title "Operator Overloading" with the subsection title "Python Wrap-up", and the section title "Intermediate Flask".

Transcript


0:00
(soft upbeat music)
0:04
- [Instructor] Next up,
0:05
we'll briefly talk about Operator Overloading in Python.
0:08
This is actually something we briefly touched upon
0:10
very early on when I introduced Dunder methods.
0:14
Operator overloading allows us to modify
0:17
the way that operators behave in Python.
0:20
So for example, out of the box already,
0:24
some operators are going to behave differently depending
0:26
on what they are acting on, right?
0:28
So three plus five is going to behave differently
0:33
or three plus three, in this case, from the string three,
0:36
plus the string three, it can catenate them in this case.
0:40
So there is some behavior that says,
0:43
how does a string plus a string work?
0:47
It is going to look on this string
0:49
and try and figure out.
0:51
Is there a definition for how plus works versus
0:54
on an integer?
0:55
Is there a definition for how plus works on an integer?
0:59
And there is,
1:00
there are special Dunder methods that Python looks for
1:04
on particular classes like the string class
1:07
or on the inter-class or in the case of SQL alchemy.
1:11
When we are doing a filter,
1:14
we talked about how the double equals, so this won't work.
1:16
I don't have a SQL Alchemy running right now.
1:19
I don't have any models or anything,
1:20
but we did things like how about a pet.query.filter.
1:25
And then we would do where, what'd we have,
1:29
I don't know, pet.name equals
1:32
or pet.id is greater than four.
1:35
It's not going to try and figure out what pet.id
1:38
is like a variable five, let's say,
1:42
and just replace that five grater than four.
1:45
That's not how it works.
1:46
It generates a SQL query for us that is then sent off.
1:50
So SQL Alchemy has changed how the plus operator works
1:55
and that's all done by writing the correct Dunder methods
1:59
in some class.
2:01
So, let's take the example of eq for equality.
2:05
Python looks for double underscore eq on something,
2:09
when you were trying to compare using double equal.
2:12
So one double equals three, we get false.
2:15
It knows how to compare integers, obviously.
2:17
And equality is actually a pretty boring one to start with.
2:20
Let's talk about less than.
2:22
So, lt Dunder lt is a method that Python looks
2:26
for when it's using the less than operator.
2:30
So if I have,
2:31
let's just take this string class.Dunder lt
2:36
and let's do help on that.
2:39
Let's see if it has any instructions here
2:42
or any valid help.
2:44
Not really, It just returns the value.
2:46
Well, that's not very useful.
2:48
But you can see that it does exist.
2:49
Let's just start there.
2:51
What we can do that it's more exciting
2:52
is to find our own versions of these methods.
2:55
We can overload the default behavior
2:58
in some class that we create.
3:00
So I'm only showing only showing equality less than,
3:03
and less than or equal to.
3:04
We could also have greater than gt greater than
3:07
or equal to all of them have their own Dunder method.
3:11
So here I've defined a class called CIString,
3:14
Case-Insensitive String, and it inherits from string.
3:19
So it has all the basic string methods.
3:21
But when we make comparisons between strings,
3:25
let's do equality, it will lowercase both strings,
3:28
it ignores casing, and then compares them
3:31
because of this return Self-doubt lower equals other.lower,
3:35
being defined in the Dunder eq method.
3:39
So we are changing the way that equality works.
3:42
At least for our Case-Insensitive String.
3:45
We're not impacting the built-in string class,
3:48
but we are extending it or inheriting from it in CIString.
3:52
So if I run this file,
3:54
CIString that I have to find percent run.
3:56
CIString and I make some new CIString.
3:59
We'll call this a equal CIString
4:03
of how about hello with an exclamation point.
4:08
And then b equals the same thing,
4:11
but we'll change the casing.
4:12
How about like that?
4:16
There we go, we've got some mixed casing.
4:19
I can now compare them with double equals
4:22
and we get true, even though we know that hello
4:27
is not double equals.
4:30
This casing of hello as a regular string,
4:33
but these aren't regular strings.
4:35
These are instances of CIString,
4:37
which have their own versions of equality less than,
4:41
and less than or equal to.
4:43
So I'm doing the same thing here for less than less than
4:45
or equal to, where we lowercase each string first
4:48
and then compare with less than.
4:50
So we're, this can be very useful
4:51
is when you're defining custom classes
4:53
and you want to be able to compare instances
4:56
of those classes.
4:57
So, if I had a Pokemon class in each Pokemon had a type,
5:00
like a fire or water and a name or a species,
5:05
or I don't know what they're officially called,
5:07
Pikachu versus Charles ARD.
5:09
And we wanted to be able to compare instances
5:12
of Pokemon right now, out of the box,
5:15
how would they be compared?
5:16
How would Python know which of those attributes,
5:18
if we have name and species and what else did we say, type,
5:23
maybe age powers or abilities.
5:27
There's all these different attributes.
5:28
How would Python just automatically know
5:30
how to compare them?
5:31
It doesn't, but by defining those special Dunder methods,
5:34
we can specify how you should compare them
5:36
or how Python should compare instances.
5:39
Or here's an example where we have a color class
5:43
and I'm just gonna do something mildly silly.
5:45
We have a color class that accepts a color name
5:48
and then an rg and b value.
5:51
So I would call this like color,
5:54
let's go with bright red or just red.
5:58
And then are, if we're doing an rgb color, like in CSS,
6:03
red would be 255, green is zero blue is zero.
6:07
So why don't I just run this actually in my I Python here.
6:11
So percent run, I called this file Operator Overloading.
6:15
I'll make my color and I'll save this to a variable.
6:17
We'll call this r, nope.
6:22
Okay, r has a method called to get CSS string,
6:28
which returns a string that we could use in CSS
6:30
or an HTML somewhere that represents an r,g,b color.
6:34
It's a correct format.
6:35
It's a string with the parenthesis and rgb prefixing it.
6:38
Anyway, that doesn't really matter.
6:40
But if I had multiple colors
6:41
and I want it to be able to compare them.
6:42
Let's make one more, how about r,g?
6:45
What else?
6:46
I guess we'll just do blue.
6:47
It was kind of boring,
6:48
but we'll make a color called blue, that's the color name.
6:51
And it has a channel red of zero and then zero for green
6:55
and then 255 for blue, blue.get CSS shows us that.
7:01
And right now, if I try and compare r and b,
7:04
let's say is, are less than b.
7:06
We get an error.
7:07
It says less than it's not supported
7:09
between instances of color and color.
7:11
Python does know what to do.
7:13
There's many things that it could compare,
7:16
and it's not always just about comparing one attribute.
7:19
There could be multiple things.
7:20
So we wanna compare.
7:21
And sometimes we do implement a less than,
7:24
or an equality method where we have a complex object,
7:28
an instance of a class.
7:29
And we may wanna take, let's say
7:31
the average of a whole bunch of different pieces of data.
7:34
Or we may want to combine them in some way and then compare.
7:37
So we can do that by defining our own method.
7:40
So why don't we define the Dunder less than methods?
7:44
So Def. less than with lt and Python
7:50
is going to automatically pass in self,
7:52
which is the instance that is being compared.
7:54
So here, we've got r less than b.
7:57
It's going to call the lesson method on r,
8:00
and then pass in B as the second argument.
8:04
So I'm gonna call this other,
8:06
you could call this anything really.
8:07
It just represents the thing we comparing to.
8:10
Now, I'm not gonna define a very useful comparison.
8:14
I think I'm just gonna base this off of the rainbow.
8:17
So for example, red comes before blue in the rainbow.
8:22
If we go with the traditional rgb rainbow.
8:26
So why don't I define a list for our rainbow?
8:29
We have deaf rainbow red and then orange, there we go.
8:36
Rgb, red, orange, yellow, green, blue, Indigo, violet.
8:39
And then what I wanna do
8:40
is take the color name of our colors.
8:43
So, let's say one of them is red.
8:45
I wanna find the index of red in rainbow.
8:47
And then for another one is blue.
8:49
We'll find the index of blue and compare which one is less.
8:53
So red comes before blue.
8:55
So we'll do rainbow.index of self.color name,
9:01
less than rainbow.index of other.color name.
9:09
Just like that.
9:10
And then we can just return that.
9:13
Now this is not gonna work as well.
9:15
When we have colors that are not listed here,
9:18
but let's just see what happens now.
9:19
So if I rerun this, I can find my file.
9:22
Ooh boy, I always insist on just scrolling up.
9:26
It would have saved me a lot of time just
9:27
to run that by typing it,
9:29
and then we'll make our red, here we go.
9:32
We've got red and then we'll make b for blue.
9:35
Maybe I'll name that blue just to make it clearer.
9:38
So blue.
9:40
Now, if I call red less than blue.
9:45
Hey, we get true.
9:46
If I do blue, less than red, we get false
9:50
before we got an error.
9:53
Now I can also do funkier things.
9:55
Most of the time you do want to return a Boolean
9:57
and pretty much always,
9:58
but there's not a rule that says you cannot.
10:01
So if we had something like, I like purple,
10:05
hopefully by now.
10:05
You probably know that I've mentioned it a couple
10:07
of times in the videos.
10:08
Let's say if self.color name equals purple.
10:14
If that's the case, we're going to return,
10:17
how dare you compare anything to purple?
10:24
Okay, purple suppress, you should never
10:26
compare something to purple.
10:28
So let's rerun our file again
10:32
And let's make a color called purple
10:34
or just p equals color,
10:37
where the name is purple
10:41
and then some values two, five, five for red zero.
10:44
I don't know.
10:45
who knows that will actually be purple.
10:48
Now I've got p and I've got b let's compare is purple,
10:51
less than blue.
10:53
How dare you compare anything to purple?
10:56
So we have overridden in this case, actually,
10:59
we didn't have a method to overwrite
11:01
or to overload for color because it was not able to compare.
11:06
There was no default less than or equal to,
11:09
or less than greater than there were no comparisons
11:13
for colors out of the box,
11:14
but we can now tell Python how it should compare
11:18
by writing these methods.
11:20
So when we compare strings like H is less than A,
11:25
and we get false.
11:26
What Python is doing behind the scenes is calling h.
11:30
I did less than so lt and passing in a,
11:35
and that returns false.
11:36
So when I have my red or my blue or purple,
11:39
it's calling purple, If I did purple, less than blue,
11:44
it's doing purple.Dunder less than, and then blue.
11:50
So that is how we can overload
11:52
these comparison operators in Python.
11:54
It's all through these magic Dunder methods.
11:57
It's pretty cool and actually it can be very useful,
12:00
especially as I've mentioned in complex classes where you do
12:03
need to have some way of comparing things
12:05
and Python has no idea how you should compare them.
12:08
So you just tell it using these Dunder methods.
12:11
(soft upbeat music)
