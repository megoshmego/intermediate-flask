Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Generators", the subsection title "Python Wrap-up", and the section title "Intermediate Flask". 

0:00
(upbeat music)
0:04
- [Instructor] Next step,
0:05
another topic we did not cover in Python called generators.
0:09
Generators, technically generator functions,
0:11
are an easy way of creating iterators in Python.
0:16
Recently in JavaScript
0:18
we actually have a similar idea, a similar feature.
0:21
It is not standardized across browsers obviously
0:24
like most of the new features in JavaScript,
0:26
but in Python, we don't have to worry about that.
0:29
Generators are a very easy way to create iterators.
0:32
We'll come back to this laziness thing
0:34
and why it has to do with generators in a bit.
0:36
But lemme show you an example.
0:38
Let's say I wanted
0:39
to do something relatively straightforward.
0:41
I wanted to sum the first, I don't know, 100 integers.
0:46
Well, I could use the sum function that's built in
0:50
and I could pass it in a list.
0:51
Let's say I wanna sum the first five.
0:53
I could pass this list in and it sums them all together.
0:57
And that's not too bad,
0:59
but if I wanted to sum the first 1,000 or 100,000 integers,
1:03
this would be pretty obnoxious.
1:06
Even if I didn't have to create the list myself
1:09
like the typing would be brutal,
1:10
but if I wrote a loop or something like I have right here,
1:13
def firstn, which is just going to make an empty list
1:18
and then loop between zero
1:21
and then whatever n will pass in, zero and 1000
1:24
and add that number to my list
1:27
and then return the list at the end.
1:29
So if we look at firstn of 20,
1:33
it makes me a list going from zero to 19.
1:36
So I've made a function that I could then pass into sum.
1:39
If I want to do a firstn,
1:41
let's do the first 1,000 numbers.
1:43
Great, so I could pass that in, sum of firstn 1000
1:50
and it works, no problem.
1:52
The downside of this approach
1:54
is that we are first creating a list
1:57
to hold every single number.
1:59
And then we're passing that in,
2:01
it's taking a while to scroll here,
2:02
then we're passing that into sum.
2:04
So before sum even starts adding the numbers,
2:07
we're generating this list
2:09
and then storing all these numbers in one place.
2:13
And that takes up space and it takes time.
2:15
And in a scenario like I have here
2:17
where I'm simply summing numbers,
2:19
I don't need to have all the numbers at once.
2:21
I could just start at the beginning.
2:23
I mean, if we were a human
2:24
and we were tasked with summing all of the numbers
2:27
between zero and 1,000,
2:30
we wouldn't first write down every number.
2:32
We would just start with zero and add one.
2:34
Then we take that total, which is just one,
2:36
we would add two.
2:38
Then we get to the next number, we add three to that total,
2:40
we add four.
2:41
So in situations where we don't need every number at once,
2:45
and it's not just limited to numbers,
2:46
but we're starting here,
2:48
we can use generators.
2:50
So we could make our own iterator
2:52
that will provide to us one number at a time
2:55
and we could loop over that
2:56
or we can just pass it right into sum
2:58
and sum we'll loop over it just like it loops over a list
3:02
or this massive list here,
3:04
and then sum all of those numbers together.
3:07
And that's what I have right here.
3:10
So this is a generator function.
3:13
It looks like a regular function
3:15
except we've got this weird keyword in here called yield.
3:19
So yield is kind of like the return keyword.
3:22
It's going to return a value
3:24
but it's also going to keep it spot
3:27
and remember where it is.
3:28
It's almost like pressing pause on this loop
3:31
that I have right here.
3:32
So this loop if I didn't have yield,
3:35
if I had nothing here,
3:37
it's basically the same as what I'm doing here
3:39
except I'm appending to a list,
3:41
but we have some end, let's say to 1,000
3:43
and then a start point which is zero.
3:45
While zero is less than 1000, add one to num.
3:49
So num will start at zero, then it will go to one, two three
3:52
until we hit 999 and then get to 1,000,
3:55
at which point this is false.
3:57
And then our function is done.
3:58
But if we put yield in there,
4:00
each time through the loop when yield is encountered,
4:03
it will return a value
4:05
and then pause this loop until we ask for the next value
4:09
or until something in Python asks for the next value,
4:12
at which point it will resume, it will add one to num,
4:16
and then yield the next num.
4:18
And then when we ask for the next value,
4:20
it adds one again and it yields.
4:23
So every time we yield, it stops,
4:25
but it's kind of like if you're reading a long book
4:27
and you're flipping back and forth
4:28
between, I don't know, something at the beginning
4:30
like there's a map or the table of contents
4:33
and something in the middle of the book,
4:34
you might put your finger or a bookmark
4:36
or something to hold your place.
4:38
That's kind of what yield does.
4:40
So here's how it works.
4:41
If I run this function firstngen,
4:45
lemme clear my console here,
4:46
and run the file again,
4:49
I now have this function called firstngen
4:52
and I'll pass in a number.
4:53
Let's start simple, how about 10?
4:57
What it returns to me is not a number,
5:00
it's not returning a zero or whatever.
5:03
Instead it returns this generator object.
5:08
So a generator function
5:09
is going to return a generator object.
5:12
This is the generator function,
5:13
the thing we get back is a generator object.
5:16
Python knows to return that
5:18
simply because we have yield here.
5:20
If we had return and I executed firstngen,
5:23
it's just gonna return one number and be done.
5:26
Here, it actually creates an iterator for me.
5:29
So I can loop over this.
5:31
I could use this.
5:32
I could pass it to sum
5:33
to sum up all of those numbers,
5:35
but all of those functions or a loop, for example,
5:38
are going to take this iterator and ask for the next value.
5:43
So if I save this to a variable,
5:45
we'll call this it for iterator,
5:50
there's a method or a function I can use called next.
5:53
And I can pass in some iterator like it
5:56
and ask for the next value.
5:59
So the code now is running.
6:01
This code here runs and it hits the first yield
6:04
and it returns, say, yields zero.
6:08
And if I ask for next again,
6:09
it's going to unpause and it adds one to num,
6:14
this is still true, so it yields one.
6:17
And this is going to keep going
6:18
until I hit the very end right there.
6:22
And we get a stop iteration exception.
6:25
So I can use this function that I've built,
6:27
the generator function which is about firstngen.
6:31
In loops I could use it in list comprehensions,
6:35
anywhere I would iterate over something
6:37
I can iterate over this.
6:39
So let's do the first 50 numbers
6:42
and let's loop over it, for n in firstngen,
6:48
we will print n, okay?
6:50
I hit Enter and there we go.
6:53
When we have a loop in Python,
6:55
internally behind the scenes whatever the iterator is,
6:58
whether it's something like this or a range or it's a list,
7:03
something that's iterable,
7:04
the Python loop is going to call next over and over and over
7:07
until it gets to that exception that we saw,
7:10
until it hits the end, not that one,
7:12
this one here, stop iteration.
7:14
So it's gonna keep calling next,
7:15
we don't see that but that's what's happening.
7:18
So the very first time it says next please
7:20
of this iterator that we get back.
7:22
This is a function we call
7:24
that returns this generator object.
7:26
It's all very confusing with the terminology,
7:29
but it returns an iterator,
7:31
it doesn't return a number or anything.
7:33
But then when we ask for the next value, we get zero.
7:38
And that's assigned to n, so we can use n.
7:40
Next time through it asks for next again
7:42
and it keeps going until it hits the end.
7:46
So this is a way of producing one value at a time,
7:50
rather than the first approach we started with
7:52
where we generated all values at once
7:55
and put them in a list.
7:56
We have this lazy way of getting a single value
8:00
each time we need it.
8:02
So now I could pass that into sum,
8:04
so if I want to get the first 1,000 numbers,
8:07
I could do sum firstngen of 1,000.
8:17
And there is no list that's created.
8:20
There's no intermediate step
8:21
where all of these numbers are first generated.
8:24
They're not stored at the same time.
8:25
It's just one number, okay?
8:27
I'm gonna add that in.
8:28
Next number, I'll add that in.
8:30
Next number, and it keeps pulling,
8:33
waiting and waiting for the next number when it needs it
8:35
and creating our total sum,
8:38
versus the other approach
8:39
where we generate one large list first
8:41
and pass that in to sum.
8:43
Now the generator function we built here,
8:46
we could easily just replace with range, right?
8:49
Range is a built-in function that will return an iterator.
8:53
And we could write our own range.
8:56
In this case though,
8:57
it probably would just be better to use range.
8:59
Why bother creating this generator function
9:02
that just replicates what we can already do?
9:05
But there are definite situations
9:07
where generators can help you.
9:09
So as a rule of thumb,
9:11
sometimes you might have infinite data.
9:14
You might have all even numbers
9:16
that you're trying to generate.
9:17
You need one at a time.
9:19
If you want to have access to those in an easy way
9:21
without having to predefine
9:23
or precreate all of those numbers,
9:26
you could use a generator function.
9:28
But the most common scenario
9:29
is when you have something
9:30
that is just too big to hold in memory at once.
9:33
So we can hold 1,000 numbers in a list at once.
9:37
But if I was trying to sum the first 1 million numbers,
9:40
I don't think there's actually a restriction
9:43
on the size of a list in Python,
9:45
but in some languages there are,
9:47
the main restriction in Python
9:48
is just whatever your machine can handle
9:50
and what memory is available.
9:52
But there could be some scenario
9:54
where you have something that's really, really large.
9:56
Let's say you have some big file
9:57
with 10,000 or 100,000 lines in it.
10:01
You do not need to have access
10:02
to every line at once at the same time, most of the time.
10:05
So you could define a generator function
10:08
that returns an iterator
10:09
which will yield a portion of that file.
10:12
Five lines at a time or one line or a character,
10:15
some chunk of it at a time that you can then use in a loop
10:19
or you can pass to a function.
10:20
So this stuff tends to come up
10:22
when we're working with big data,
10:24
when we've got really, really huge files
10:27
or a database with tons of information or a large CSV file
10:31
or just a lot of data,
10:33
and it doesn't make sense
10:34
or it's not even physically possible
10:36
to access or work with all of it at once,
10:39
you can create a generator function
10:40
which returns a generator
10:42
which is a type of an iterator, very confusing,
10:45
that will give you one piece at a time.
10:48
So here's one more example.
10:50
I have a function called find_liked_nums.
10:53
It is going to accept some sort of iterator
10:56
or iterable like a list.
10:59
So a list is something we can iterate over.
11:01
And for each number in that list, if it is a list,
11:05
we'll ask the user, do you like this number?
11:08
And if they enter anything but the letter y,
11:11
then we go and repeat the process.
11:13
But as soon as a user enters y, then the loop stops.
11:17
So I can just show you this first.
11:18
I need to run my file.
11:20
And then we'll call find_liked_nums or num.
11:24
We'll pass in some list of nums
11:25
about two, four, six, eight and 10.
11:29
And it's going to go one item at a time using this list.
11:33
Do you like two?
11:34
I'm gonna say no.
11:35
Anything that is not a y and then I'll hit y for eight
11:39
and we're done, it returns eight.
11:41
Now imagine we're doing something more complicated
11:43
not just asking a user if they like something
11:45
but some operation
11:47
where we are going to repeat it over and over and over
11:51
for some element in some sequence or some series.
11:54
We could pass in the entire sequence at once,
11:57
which is what I'm doing right here.
11:59
But what if we wanted to allow a user
12:01
to continue rejecting numbers all the way up
12:06
essentially ad infinitum until they find an even number,
12:09
let's say, that they actually like?
12:12
Well, with a list,
12:13
I would have to create a really large list
12:16
and it would still be finite.
12:17
There would still be some end point.
12:19
Using a generator which I've done here,
12:22
I have a generator function called evens.
12:25
We can pass in a starting value
12:27
and then it will yield an even number
12:29
based off of that start value.
12:31
Technically it could be an odd value
12:33
if you passed in a start of like three or five or seven,
12:36
but if we pass in a start of two,
12:38
it will start by yielding two
12:40
and then each time it is asked for the next value.
12:44
It will add two to that number and yield that number again.
12:47
So it will yield two then four then six then eight.
12:50
So this would allow me to run this code, find_liked_num,
12:55
but instead of creating a list
12:57
where I've defined and stored every number
13:00
that I want to try with a user,
13:03
I can instead do it the lazy way
13:05
where one number at a time
13:06
is all that we're ever working with.
13:08
We're not storing them together.
13:10
We're just accessing each one when needed.
13:13
So we can do that
13:14
by passing in the generator function I defined, start,
13:17
we'll give it a start point like two,
13:20
and now it asks me, do you like two?
13:22
And if I type no or anything that is not y,
13:26
it will then ask for the next value from evens.
13:29
No, and I could just keep going forever here.
13:33
I really could go forever at least in terms of Python,
13:37
there's not going to be a stopping point
13:39
with this generator unless I type y
13:42
or there's some sort of memory issue
13:44
or something goes wrong with my computer,
13:46
but Python is not going to get in the way.
13:49
I can continue to do this,
13:51
I mean, even just to get to this point.
13:53
With a list, I would have
13:54
to generate all of these numbers ahead of time
13:56
and pass that in.
13:58
But now, oh, I didn't even type y, there we go.
14:01
But now this can keep going as long as needed,
14:03
it's doing it the lazy way.
14:05
It's just getting one number.
14:06
Do you like this one?
14:07
Nope, all right, well, lemme get the next one.
14:09
Do you like this one?
14:10
So we can do things like summing them together
14:13
but like I said, most of the real use cases for this
14:16
is when we're working with big data.
14:18
The overhead of storing 1,000 numbers in a list is really,
14:22
it's pretty inconsequential.
14:24
Once you start getting
14:25
into like tens and hundreds of thousands
14:28
of numbers in a list, it's something to consider.
14:30
But in the examples I showed you,
14:32
it was really just to demonstrate
14:34
how you could write a generator function and how they work,
14:36
not to make a case for using a generator
14:39
if you're just trying to ask a user
14:41
if they like two, four, six or eight.
14:44
So there's a lot more to generators
14:46
and iterators in general in Python.
14:49
Generator functions are a shortcut.
14:51
They're an easy way of defining an iterator.
14:53
You can also define them the long way,
14:56
the more complex way using a class.
14:58
It gets a little bit complicated
14:59
and it's not something you'd really need to do very often
15:02
but generator functions are worth knowing about.
15:04
And that's pretty much all I have to say about them.
15:07
This is another topic
15:08
that is definitely worth trying to pursue and understand.
15:11
But most of the time in web development,
15:14
at least with the apps
15:15
that you'll probably be creating right now,
15:17
I wouldn't stress too much about generators,
15:20
but if you continue to build larger apps
15:22
and work with larger sets of data,
15:25
or if you go down the data science route
15:27
and you're trying to follow a tutorial
15:29
or learn more about doing some data analysis in Python,
15:34
you'll probably encounter at some point a generator function
15:37
or tutorial that mentions generators.
15:39
So you'll know when you need it for the most part.
15:42
But that's it, generator is an easy way
15:44
to define an iterator,
15:46
a lazy way of working with one item, one piece,
15:49
It doesn't have to be a number.
15:51
It could be a character in a really long string.
15:53
It could be a part of a file.
15:55
It could be a single byte in a long string of binary.
16:00
It's just one thing at a time that will be yielded
16:03
rather than pre-calculated ahead of time
16:05
like we would do with a list or something, okay.
16:08
(upbeat music)
