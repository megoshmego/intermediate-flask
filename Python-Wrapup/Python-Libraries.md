Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Python Libraries" with the subsection title "Python Wrap-up", and the section title "Intermediate Flask".

0:00
(upbeat music)
0:04
- [Instructor] All right, so there are other features
0:06
and pieces of syntax in Python that we have not covered.
0:09
There are other Dunder methods you can overload.
0:13
There's more to talk about with iterators for example,
0:15
on defining custom iterator classes.
0:17
But for the most part, we've seen
0:19
pretty much everything you need to know to use Python
0:22
at least day to day.
0:24
But we have not talked about a whole bunch of libraries.
0:27
So I just wanna spend some time covering some
0:29
of the commonly used libraries
0:31
and just pointing out things you may wanna look into.
0:35
First of all, the Python standard library is huge.
0:37
There are so many different modules we get for free.
0:40
We've used some of them,
0:41
but we really barely scratched the surface.
0:44
There are tons of useful data structures
0:46
that you get for free in Python,
0:48
things like stacks and queues, binary search trees.
0:51
So if we go to the Python docs
0:53
and we look at the Python standard library page,
0:56
it details all of the different modules
0:58
that you get for free.
0:59
If you're using Python
1:00
you just have to import them when you want to use them.
1:03
They're grouped by categories.
1:05
So there are some pretty, pretty useful ones
1:08
especially around data structures and some algorithms.
1:12
So, if we find the right category here,
1:15
let's see, here we go.
1:17
Under data types there's heap queues, which you probably,
1:21
I don't know, you may or may not have heard of.
1:23
I wouldn't expect you to know about heap queues,
1:25
but there are some algorithms built in that are just nice
1:28
to use in certain situations,
1:30
rather than defining them yourself
1:31
or finding a library that you then install and download.
1:34
We've got tools right here within Python.
1:37
We've got a lot of tools for strings
1:39
that we haven't talked about.
1:40
We haven't covered regular expressions,
1:42
things like fractions,
1:44
working with some advanced math concepts,
1:47
tools for iteration and efficient looping.
1:51
Let's see what else, data persistence,
1:53
there's something called pickling in Python,
1:55
which is a way of serializing data to save to a file
1:59
that you can then read back out at,
2:01
from texts from this special pickle format
2:04
and turn into Python code that can be run.
2:07
So you can serialize a complex Python object
2:11
and then save it to a file without a database, without json.
2:16
And then turn it back into a complex Python object
2:19
when you read it out.
2:20
There are tools for working with different file types,
2:22
most commonly CSV, Comma Separated Value files,
2:26
other tools for cryptography.
2:29
There's a bunch of stuff here,
2:30
a lot around concurrency and threads, and multiprocessing,
2:35
working with emails, that's pretty much it,
2:38
I guess for the most common stuff, audioop, never use that.
2:42
Conversion between different color systems,
2:44
that one can be useful rather than having to go find
2:47
that code or download it or write your own functions
2:50
to convert between different color spaces.
2:52
So there's a lot of stuff here
2:53
and I definitely recommend spending some time
2:55
getting more familiar with at least some of the pieces
2:58
in the standard library.
2:59
There are some great articles about the most useful,
3:02
the most important, the best modules built into Python.
3:05
I would say it might be worth your time
3:07
to research some of them.
3:08
And moving away from the standard library,
3:10
a tool that I like to use a lot is called Beautiful Soup.
3:14
So it is something you have to install and download and use.
3:17
It's called Beautiful Soup
3:19
and it helps you scrape data from the internet.
3:22
So lots of web pages and websites
3:25
and applications have APIs, like Reddit has an API
3:29
where you can just get data from Reddit.
3:31
There are APIs for pretty much
3:33
most of the commonly used big applications online
3:37
but sometimes there's data that you want where the company
3:40
or the application does not provide an API.
3:43
And the information is still on the HTML.
3:46
It's just not easy to get to, there's no json
3:49
or even XML that you can request.
3:51
So you have to request the HTML.
3:53
Here's an example of something that I've done.
3:56
There are websites to make reservations
3:58
for campsites and camp grounds in California,
4:02
and just the national parks and state parks in the U.S.
4:06
There is no API where you can find out
4:08
which campsites are available on what days,
4:10
if there's any openings or cancellations.
4:13
There's no service or API that you can use to get that data,
4:16
but you can go to the actual web pages
4:19
and look with their calendar that's a bunch of HTML,
4:22
you can look for little blocks,
4:24
they have like green, green boxes
4:27
essentially on the calendar for dates that are available.
4:30
So I used Beautiful Soup to scrape, to download that HTML
4:34
from those web pages and checked for those green boxes.
4:37
There was a particular class and some,
4:39
I think it was a paragraph or maybe it's a table.
4:41
I don't remember what it was, something I was looking for
4:44
and I wanted to extract the content about those campgrounds.
4:48
And then you can automate that.
4:49
You can do things like crawl all of the links
4:53
on a given webpage.
4:54
So I could see it, I get started out on a file, a webpage
4:58
that had all the most popular camp sites in California.
5:02
And then it would go to each one, send a request,
5:04
get the HTML, and then scrape it
5:07
according to the algorithm I wrote, the logic,
5:09
the different method calls from Beautiful Soup,
5:11
where I could isolate the pieces I want
5:13
and store that in a database.
5:14
So it just comes with tools to help you navigate
5:17
the messy world of HTML.
5:19
If you have a massive string
5:21
with like 10,000 different HTML tags
5:24
that might be a bit excessive, but thousands of HTML tags,
5:27
and all you want is a couple pieces of data
5:30
between some tags hidden somewhere on the dock,
5:33
it's really difficult to do that yourself.
5:35
So that's where a tool like Beautiful Soup comes in.
5:38
You can even set it up in a way that it will scrape
5:41
every day or every hour even.
5:43
Now the gray area with scraping is that a lot of websites
5:46
don't want you to do it.
5:47
So, sometimes they try and make it hard.
5:50
If you're scraping content from a webpage
5:52
that has a paid service and you're trying
5:55
to get around that, I would careful,
5:58
I wouldn't do that really, or I'd be very careful about it.
6:02
But if it's just an application that doesn't have an API,
6:05
the data's already online, people can view it,
6:07
then usually I don't think there's an issue with that.
6:10
And like I said, I'm a fan of scraping personally.
6:13
So definitely something you may wanna look into
6:15
for a project.
6:16
If you have some idea, some data that you want access to
6:19
that does not currently provide access through an API
6:23
that shouldn't stop you.
6:24
It might make it a bit more challenging
6:26
but thanks to Beautiful Soup, it's still very possible
6:29
to scrape the data from that website.
6:31
And then lastly, in terms of libraries,
6:33
there are lots of data science libraries
6:35
that are really commonly used in Python.
6:37
Now this is not a data science course,
6:40
so we're not gonna go into these,
6:41
but I figured I'd just highlight some of them.
6:43
These are worth knowing about,
6:45
there's tons of tutorials and documentation,
6:47
I'll show you one of my favorites in just a moment,
6:50
but some of the most commonly used libraries in data science
6:53
with Python include Numpy.
6:56
Numpy includes a lot of methods and helpers
6:59
for linear algebra, more complex math
7:02
that would be a huge pain to implement on your own
7:04
and algorithms in general, this type of math,
7:07
matrix math, linear algebra plays a very significant role
7:10
in data science.
7:12
There's another tool called Pandas
7:13
which is used generally when you have some dataset
7:16
and you want to be able to group it or slice it,
7:18
query it, work with portions of it.
7:21
That's what pandas is for.
7:23
And then SciKit-Learn is a tool that includes a bunch
7:26
of common machine learning algorithms that you won't have
7:29
to implement yourself but you can still use.
7:32
So these are taught quite a bit in data science boot camps,
7:35
online courses that teach data science with Python.
7:38
They're very popular.
7:40
So a good place to start, if you are curious about any
7:42
of this is this link here will take you to Scipy,
7:47
Scipy lecture notes and it's just a document
7:50
that basically walks you through most of these tools.
7:54
So we've got Numpy, those things like Matplotlib,
7:57
which we haven't covered.
7:59
Well, obviously we haven't covered
8:00
but I did mention in that list,
8:03
it's a tool for making charts and graphs
8:05
and plotting information,
8:06
a very important part of data science.
8:09
You can see some of the stuff it generates.
8:11
You can customize it and make things a bit more exciting.
8:14
And there are many other tools to help you generate plots.
8:18
We've got Sympy here,
8:19
there's tools for image processing, 3D plotting.
8:23
So this is a good document that walks you through
8:25
a lot of those tools that I mentioned.
8:27
So I wouldn't drop everything and go enter the world
8:31
of Python data science just yet
8:33
because we have a lot left to learn
8:35
even if it's not all in Python.
8:37
We've got a lot left with Node and React and Redux.
8:40
So hang in there, but definitely bookmark this,
8:43
bookmark this page, consider coming back.
8:46
These are just very popular tools
8:48
and it's not like data science is this completely
8:51
removed separate thing from web development.
8:53
Yes, in general, they are different disciplines.
8:56
You can work with Python as a data scientist
8:58
or as a web developer,
9:00
but also there's quite a bit of overlap.
9:01
You might be a data scientist who wants
9:04
to scrape information from the internet using Beautiful Soup
9:08
and then build a front end after you've run a bunch
9:11
of that data through some algorithms
9:12
and you have some learnings to share
9:15
to create a dashboard where people can view it.
9:17
So there is a pretty significant overlap or there can be.
9:20
So don't feel like you need to stay
9:23
in the web developer lane.
9:24
I definitely encourage you to spend some time,
9:26
maybe after you finish this course,
9:28
learning about some of these tools
9:30
in Python for data science.
9:32
(upbeat music)
