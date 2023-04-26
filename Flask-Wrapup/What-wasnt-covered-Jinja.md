Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "What wasn't covered Jinja", the subsection title "Flask-Wrapup", and the section title "Intermediate Flask"?

Transcript


0:00
(upbeat music)
0:05
- [Instructor] So we've been using Jinja quite a bit
0:07
for our templates.
0:09
Just to set the stage here,
0:10
there are tons of different templating languages,
0:12
different tools you can use for writing templates
0:15
within Python, but then also within pretty much
0:18
every language, there are different variations
0:20
for writing templates in Node.js.
0:22
There are tools to write templates in Ruby,
0:24
and they all kind of do the same thing at their core,
0:28
like a bare minimum.
0:30
We need the ability to loop, to have conditionals,
0:33
and to render some sort of variable like a tweet.
0:38
We can loop over all the tweets and make an H1
0:40
with each tweet text, or we can display a username
0:44
dynamically in the navbar.
0:45
But Jinja actually does a lot more
0:47
than the average templating language.
0:50
Or maybe a better way of putting it
0:52
is that there are lighter weight languages,
0:54
or templating languages than Jinja.
0:57
Jinja provides a ton of features.
0:59
We covered some of them.
1:00
We saw things like how we can inherit from another template.
1:05
We can create a base.html or some other main template
1:08
that we inherit from so we can share functionality,
1:11
but there's actually quite a bit more.
1:13
So if you go to the Jinja docs, Jinja's API overview,
1:18
and you just start scrolling,
1:20
you'll see there are a ton of different methods.
1:22
Some of these actually pertain to creating
1:25
or rendering the template itself, flask.
1:29
It takes care of that for us.
1:30
We never actually initialize our template.
1:32
We don't do anything other than call render template,
1:35
but behind the scenes, flask is doing some work for us.
1:38
But then within templates,
1:40
there's quite a few things we didn't talk about.
1:42
First of all, there are things called filters within Jinja.
1:46
So if we scroll down here,
1:48
these are just different operators
1:49
and things that we already know about in Python
1:52
that happened to exist in Jinja.
1:54
But if we keep going down, keep going, here we go.
1:57
Built-in filters.
1:59
These are filters that we can use directly in a template.
2:02
So let's find a simple example.
2:05
Things like max or min,
2:07
so we can have a list or some iterable of numbers.
2:10
It doesn't even have to be just integers,
2:13
but some iterable, and the syntax to use
2:16
one of these filters is to put a pipe,
2:18
and then the name of the filter like max.
2:20
And this is only going to render the max from this iterable,
2:24
which is three, we have min, there's other ones,
2:28
let's see, we've got replace, reverse, round.
2:32
So these aren't exactly the same as just calling a method
2:35
in Python, but it's very similar.
2:37
There are similar methods like around method
2:40
or a replace method in Python.
2:42
We have some other ones, let's see what's another example,
2:45
sort is one that definitely is worth thinking about,
2:48
or at least reading about to sort some sort of iterable
2:52
and change how it's displayed when you are looping.
2:55
So for city in cities and then the filter pipe sort,
3:01
and then you can specify reverse, descending, ascending,
3:05
and you can also specify an attribute.
3:07
So sort based off of the name on each user or reverse.
3:12
Sum, there's another one you can sum different pieces
3:16
like the price on a list of items.
3:19
So we don't have to actually call the correct Python code
3:23
to do this, it's a filter thanks to Jinja.
3:26
So there's quite a few of them, they're worth checking out.
3:28
Another feature I would check out
3:29
that we have not considered are macros.
3:33
Macros are a way of wrapping up Jinja logic and HTML.
3:38
So pieces of a template into almost a reusable function
3:42
that you could call.
3:44
So let's say that we made a lot of NavLinks in a template.
3:48
This is from a tutorial.
3:49
The docs unfortunately, don't do a great job
3:51
of describing macros in my opinion,
3:54
but here's the definition of a macro called NavLink,
3:57
and it creates an ally and it potentially
4:01
has a class of active.
4:02
It may not, it might just be a regular old ally
4:05
with an anchor tag.
4:06
So these would be links for a navbar,
4:09
and it dynamically decides
4:10
which one should have the active class.
4:13
Let's see.
4:13
For example up here, the active class is on Libros.
4:17
I guess this is in Spanish, versus if I was on this webpage,
4:22
the active class is assigned to this one link
4:25
in the navbar.
4:27
So this is something we used a lot on our website
4:29
and we wanted to just easily set up a NavLink,
4:32
which is really just a conditional with an ally
4:36
with active class or the else clause
4:39
is just an ally without that.
4:42
And to use it in our code,
4:44
we can reference NavLink and run it like a function.
4:48
But this is not a function we've defined
4:50
in a separate Python file,
4:51
it's a macro that we've defined in Jinja.
4:55
So that's pretty much it for macros.
4:58
You can define reusable pieces of templates that have logic.
5:01
You can pass argument in, as you can see here,
5:04
you pass values to those macros and you can use them.
5:08
And then another thing that we haven't covered
5:10
is caching with Jinja.
5:12
You can specify that portions
5:15
of a template should be cached.
5:17
They're not going to change often.
5:19
That is more of an advanced feature
5:22
within template inheritance, which we did cover.
5:25
We talked about setting up blocks
5:26
in a parent template like base.htlm,
5:29
and then creating a child template
5:32
that would reuse functionality from base.htlm.
5:35
But we did not talk about super blocks.
5:38
Super is actually pretty simple.
5:40
It's very similar to the idea of super in Python in a class
5:43
where super references the superclass, the parent class,
5:47
that you're inheriting from.
5:48
But in a template, a Jinja template,
5:50
super references the contents of the parent block.
5:54
So if we had a block sidebar in a parent,
5:58
and we wanted to modify it or add something on
6:01
at the beginning, from a child component,
6:04
and then add in the rest of the sidebar block
6:06
from the parent, we can use super.
6:09
You can read more on the docks for this.
6:11
There's actually quite a bit to sharing functionality
6:13
between templates, setting up inheritance
6:15
and base templates, child templates, super templates,
6:18
nested extensions, scoping, template objects.
6:23
There's quite a bit to know about Jinja,
6:25
but we've gotten by just fine with the basics
6:28
that we've absolutely needed, looping conditionals
6:31
and rendering things into HTML.
6:34
So overall, I definitely recommend you take a closer look
6:37
at Jinja, read the docs, in particular,
6:40
this page of the documentation, which is the synopsis
6:44
or the template designer documentation, rather.
6:46
There are other pages on the docs around high level APIs,
6:51
low-level methods, things that you probably don't need
6:53
to care about as much, Mehta APIs,
6:56
but I would focus on this template designer documentation.
6:59
It talks about all the stuff we've already seen,
7:01
the delimiters to have statements in there, expressions,
7:05
to print into your template outputs.
7:07
It talks about variables and controlling white spaces,
7:11
filters that we just barely touched on
7:13
and inheriting and sharing templates.
7:16
This is definitely a page I would check out.
7:18
All righty.
7:19
(upbeat music)
