Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Python Type Hints" with the subsection title "Python Wrap-up", and the section title "Intermediate Flask".

0:00
(lighthearted music)
0:04
- [Instructor] Next up,
0:05
there's a small feature,
0:06
but nice one in Python that we have not covered
0:08
called Type Hints.
0:10
So in general,
0:11
Python is not going to enforce
0:13
any sort of type restrictions, as we've seen.
0:16
We can define a function like this, add function,
0:18
it takes two parameters x and y, it returns x and y.
0:23
It is not going to yell at me,
0:24
it meaning Python is not going to get angry at me,
0:27
if I pass in two strings or two lists.
0:31
Now I might try and add them
0:32
and then there might be an error.
0:34
But it's not gonna prevent me from calling add
0:37
with two strings, or two boolean or whatever.
0:41
Other programming languages,
0:42
not all of them,
0:43
as you see in JavaScript is similar to Python
0:45
in this regard,
0:46
which is why tools like TypeScript exist.
0:49
But some other languages will enforce
0:52
and actually force you to declare,
0:54
if X and Y have to be integers
0:56
or if they have to be booleans, they have to be strings.
0:59
Python does not have that.
1:01
It's not, just not how it works.
1:03
But we can add in a type hint to these parameters.
1:07
Now, this is different than a type definition,
1:09
it is not going to be restrictive,
1:12
as far as the type,
1:14
we'll still be able to pass in a string
1:15
or something that is not hint.
1:18
But we get better feedback
1:19
and help better auto complete in our editors.
1:22
So I'll just demonstrate this.
1:24
Right now, if I call add, my VS Code hint,
1:28
just says x and y.
1:30
And then it shows me the doc string,
1:31
add x and y and return results.
1:33
So I could pass in an integer
1:35
and I could pass in a string.
1:37
And that's pretty much it and if I instead,
1:40
add in this type hint,
1:43
both of them are ints.
1:44
Just like that.
1:46
And now I try the same thing, add,
1:50
it's now giving me a hint that says x should be an int.
1:55
So I'll type some int, comma,
1:57
and it says y should be an int.
1:59
It also shows me up here x and y are ints.
2:02
But again,
2:03
it's not gonna stop me from running this with strings.
2:06
It's purely a hint,
2:07
which is why it's called a type hint, not a type definition.
2:10
Also, I can set a type hint for the return value.
2:14
So I'll just say this function returns an int,
2:17
this is the syntax here.
2:19
And this can be useful
2:21
in the same situations in your editor in IPython,
2:25
or when you're viewing a function
2:26
and getting documentation on it.
2:29
Like here, if I just look at add,
2:32
I can see it returns an integer.
2:35
But it's also helpful.
2:36
If I wanna figure out what methods I can call
2:39
on the result of add.
2:41
So if I did something like add one, comma four,
2:45
and then dots, the auto complete suggestions here
2:49
are all based off of the fact
2:51
that this returns an integer.
2:54
VS Code is assuming because of this type hint
2:57
that this will be an int.
3:00
Now, it will still give me the same hint here,
3:04
if I pass into strings,
3:07
in which case the return value is not going to be an int,
3:10
but it just makes an assumption
3:11
based off of this value right there.
3:14
So that can be nice.
3:16
It just helps you, you know, write your code faster.
3:18
And we get better documentation
3:21
because when we call help of add,
3:23
we can see those type definitions.
3:26
But if I do run it in IPython,
3:28
just very briefly,
3:31
paste this in and I call add one two, it works.
3:36
I can get the auto complete as well.
3:39
These are all int methods.
3:40
I don't have string methods.
3:42
But I can still do this,
3:43
add true comma, the string too.
3:47
So I'm gonna go well, I get an error,
3:49
but it's not going to stop me.
3:52
Also, if I had changed this definition,
3:56
to, let's say, return a string,
4:00
even though it's not going to return the string.
4:03
Now, if I call add one comma two, I type dot
4:07
and I hit Tab.
4:08
All my auto complete suggestions are string methods.
4:12
So that's pretty much it.
4:13
That's type hints.
4:14
It is not restrictive.
4:15
It's not enforced.
4:16
It's purely to help you as a developer
4:18
and other developers with their tools,
4:21
whether it's a text editor like VS code, or IPython.
4:26
It just makes it clearer and easier to figure out
4:29
how a method or a function is supposed to work.
4:31
(lighthearted music)
