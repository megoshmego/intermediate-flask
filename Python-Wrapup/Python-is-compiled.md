Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Python Compilation" with the subsection title "Python Wrap-up", and the section title "Intermediate Flask".



Skip navigation
Search




Avatar image


0:00 / 6:55

Transcript


0:00
(exciting music beat)
0:04
- [Instructor] Next up, let's talk about this
0:06
last bullet point here, Python is a compiled language.
0:10
Now this is not something you usually need to think about
0:13
or worry about, but it's worth just talking about
0:15
if we're gonna recap Python and point out some of the,
0:18
the nice to knows this is one of them.
0:21
So when we define some function in Python,
0:23
like this add function right here,
0:26
I'm just gonna paste it into iPython.
0:31
Okay, there we go, we have our add function.
0:34
We can pass in some numbers, three and four, great.
0:38
I can also set double to be true,
0:42
which will then double my output, it defaults to false.
0:46
All right, hopefully nothing too crazy.
0:48
When we write our code whatever it is
0:50
in this case this add function,
0:52
Python actually gets compiled into byte code.
0:56
Now byte code is still,
0:58
it's not the same thing as assembly code,
1:00
it's definitely not the same thing as machine code.
1:02
But it looks like this when it's printed out,
1:06
you never really have to see this or,
1:08
or deal with it but it's good to know.
1:11
When we run our Python files
1:13
or when we import a Python file.
1:16
When we import a module into another Python file,
1:18
that code is compiled down into byte code.
1:22
So if you tried to read this, I mean,
1:24
you definitely can make sense of it, it takes a lot of work.
1:27
If you're not familiar with these terms,
1:29
things like how binary add works or load fast
1:33
or pop jump if false.
1:35
So I wouldn't stress about it, but I'll do a quick demo
1:38
of how we can actually view this code.
1:40
If you wanna see it, there is a standard library
1:44
we can import called DIS.
1:48
We do a help on DIS,
1:51
Dissembler of Python byte code into mnemonics.
1:54
There is a function available on this module
1:57
called DIS disassemble.
2:00
And we pass in some file, a function class, a module.
2:05
It will disassemble classes, methods, functions
2:08
and other compiled objects down into this byte code
2:11
that will be printed out for us.
2:13
So we have this add function
2:15
that we've been playing around with.
2:18
And if I called DIS.DIS and then they pass in add,
2:25
there we go, this is the byte code.
2:28
Let's try it on our animal class.
2:31
Nope, animals not defined, I think I quit iPython.
2:34
So let's run animal.PY.
2:37
Now I have my animal class great.
2:41
Let's try that line again.
2:43
Okay. So it's significantly more,
2:47
it's still pretty short and that's really
2:49
all you need to know about it at this point.
2:52
Most Python developers probably never even looked at this,
2:55
but yes, it is a compiled language and you can view
2:58
the underlying byte code that it gets turned into.
3:02
Now, somewhere this may have come up
3:03
or definitely has come up,
3:04
you may or may not have noticed is when we actually import
3:09
a module into another file and we run that file.
3:13
We end up with this weird
3:15
double underscore Dunder pycache folder.
3:18
I don't know if you've seen it before,
3:20
but this pycache folder is actually going to store
3:23
the underlying byte code that has been compiled
3:27
from some module.
3:28
And this is done just to prevent the process
3:31
from having to be repeated every time you run some code.
3:35
So when Python is compiling this code down to byte code,
3:39
it will be stored as byte code in the pycache.
3:41
And then in the future, if you're trying to use that file
3:44
and it hasn't changed, that's important.
3:46
If it hasn't changed at all,
3:48
then it won't have to recompile it down.
3:50
So I can just quickly demonstrate that here.
3:53
I'll quit out of here.
3:57
Right now if I do an LS, there is no pycache at all.
4:01
I'm going to make a new file.
4:03
I'm gonna delete this afterwards,
4:05
but I'm just going to call this file, how about zoo.PY.
4:12
And in zoo, I'm going to import animal.
4:16
So I'm probably gonna do from animal.PY the file
4:20
import my class animal,
4:23
and then I'll instantiate these two animals over here
4:28
and I'll try doing blue.meow, tammy.meow.
4:35
All right, so I now have zoo.PY where I'm just executing.
4:40
I can't do Tammy.meow, it's tammy.oink.
4:45
There we go.
4:46
I'm importing animal the class from this file.
4:50
And if I run my zoo.PY file, this code will be turned into
4:55
or compiled down into byte code.
4:57
But first we're importing animal from this animal file
5:01
so this needs to be compiled as well.
5:04
And Python is going to compile this
5:06
and store it in the pycache so that in the future,
5:09
if I run this file again,
5:11
it will still compile this file,
5:12
but it won't have to go and compile this module
5:15
over and over and over.
5:17
And this is short and compiling really doesn't take long
5:20
most of the time, but it's just a nice optimization,
5:23
especially in things like a Flask app where we have
5:26
dozens of dependencies and they might,
5:29
they might consist of, you know, thousands.
5:31
Well, I shouldn't say thousands, a hundred files maybe
5:34
with thousands of lines of code that need to be compiled.
5:37
We don't need that to happen every single time
5:39
we run our main app.PY file.
5:42
So right now there is no pycache.
5:44
I'm going to execute this file called zoo.PY.
5:48
Okay, it works.
5:50
Now I type LS and lucky there,
5:54
we've got a Dunder pycache folder.
5:57
If we open it up, there's no cache, there is is.
6:00
In my editor, it's not gonna look like much.
6:02
Notice it ends in a dot PYC and it's named animal,
6:08
which is the file that we compiled and imported.
6:13
So now, assuming I don't change animal,
6:16
this will remain and just be used in the future.
6:19
Anytime I run this file,
6:20
we'll use that cached version from the pycache.
6:23
Now we don't do any of that ourself.
6:25
Python keeps track of whether the files have been changed.
6:28
Python will look in the cache and use that compiled version,
6:31
but that is what the Dunder pycache folder is
6:34
you probably have seen it before,
6:36
and you don't need to include those in Git
6:38
or put them up on GitHub, they can be,
6:41
they will be generated automatically by Python when needed.
6:44
All right, so next we're gonna move on
6:46
to some more specific features
6:47
and syntax in Python that we haven't covered yet.
6:50
(upbeat music)
