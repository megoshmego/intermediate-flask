Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Registering and Authenticating", the subsection title "Hashing and Loggin In", and the section title "Intermediate Flask"?

0:03
all righty so now that we've seen the
0:06
basics of using flask bcrypt in ipython
0:09
the actual methods that will need to use
0:12
to create the password hash and then
0:14
also authenticate a user using check
0:16
password hash those are the methods we
0:19
need let's talk about how we would
0:20
structure a flask app to actually use
0:23
this stuff so here's a demo app that I'm
0:25
going to use it's also in the slides all
0:28
of the code I'm showing you corresponds
0:30
to this app called good password so you
0:33
can find it in the demo folder under a
0:35
good password I'm not going to create it
0:38
from scratch I'm not going to type all
0:39
of the code I'm just going to walk
0:40
through existing code and then after
0:42
this I will show how we would actually
0:44
create everything and set it up one step
0:46
at a time
0:47
but I want to give you the bird's-eye
0:49
view first of how it all fits together
0:50
so this is a very simple app there's no
0:53
other model aside from a user model
0:56
there is a protected route called slash
0:58
secret if I try and view it right now I
1:01
can't get there I do have the flask
1:02
debug tool bar setup and it's going to
1:06
intercept those redirects but you can
1:08
see there I'm not allowed to go to slash
1:10
secret every time I try it's redirecting
1:13
me to slash it's taking me back here
1:16
it's flashing a message saying you must
1:18
be logged in to view I'll register with
1:20
a username of CB chicks which is my one
1:23
of my chickens if you haven't gathered
1:24
that by now she's spending like every
1:26
other video and then I'll type some
1:28
password my password it will be hippo
1:33
monkey with a capital M 1980 with an
1:38
exclamation point I'm going to register
1:40
sure I'll save it in Chrome and now it's
1:43
redirecting me to slash secret and I'm
1:46
logged in I can go to slash secret I can
1:48
go back home but I can also go to slash
1:50
secret and view it it's not trying to
1:52
redirect me anywhere but as soon as I
1:55
log out it will redirect me back to
1:58
slash again that's just the flask debug
2:01
toolbar and now if I try and go to slash
2:03
secret no luck
2:04
it keeps redirecting me home and saying
2:06
you must be logged in to view if I log
2:09
in my password information has been
2:11
saved thankfully I don't have to type it
2:13
again Stevie chicks and my password
2:15
login it works I end up at slash secret
2:19
and I can continue to go to slash secret
2:21
so it's not just authenticating me for
2:24
one route or one request it's
2:26
remembering that I'm logged in so we'll
2:29
cover both of those pieces so here's the
2:32
app code let's take a look at the model
2:35
first so we have our basic DB stuff with
2:38
sequel alchemy and I have a single model
2:40
called user so there are some methods
2:43
we're going to ignore for a moment at
2:45
the core of the model we just have three
2:47
columns an ID which is an integer auto
2:51
increments primary key we have a user
2:53
name which is not allowed to be null and
2:56
username has to be unique which is very
2:59
important we're going to look somebody
3:00
up based off of their user name when I
3:03
go to login right I just type in a
3:07
username and a password we need to be
3:09
able to find that user based off of this
3:11
username we don't have people enter
3:13
their user ID they use their username so
3:16
that must be unique otherwise it'd be
3:19
very difficult and problematic if we had
3:21
two people with the same username we'd
3:23
only be I don't know how we'd actually
3:25
implement that that would not be good
3:27
and then we have our password which
3:29
cannot be null and it's just text okay
3:33
so if we look at our routes let's go to
3:37
the register route
3:38
it is a get in a post route we're using
3:41
what the forms and when that form is
3:44
submitted and validated hopefully this
3:46
is not new to you we talked about this
3:49
in with the forms then we're getting the
3:51
name and the password from the form and
3:52
we could put the logic right here to
3:55
actually hash the password get the
3:58
hashed password and then create a new
4:00
user model and save that to the database
4:03
DB ad or DB session data DB session
4:06
commit but instead of cluttering our
4:09
view function with the bcrypt logic it's
4:12
better to move our logic out of the
4:15
views and move it into the models so
4:18
we'll create class methods and this is
4:20
pretty standard for registering so
4:23
there's a class method called register
4:24
we call that on user
4:27
I'm calling it right here let me zoom in
4:30
that's quite zoomed the user dot
4:32
register this is going to return a new
4:35
user and that user will have a hashed
4:38
password it will have a user name on it
4:41
and then we can save it add and commit
4:44
and we should get an ID as well so that
4:47
method register is going to take a
4:49
username and a password which I'm
4:51
passing in from the form data and then
4:54
it generates password hash using bcrypt
4:57
then we take that we do have to turn it
5:00
into a normal string to store it in our
5:02
database so we're just turning a byte
5:04
string into a normal string then we take
5:07
that and we create a new user remember
5:11
in a class method the class itself will
5:14
be passed in as the first argument so
5:17
this is user capital u user but we use
5:20
class we're making a new one user name
5:23
equals the username that was passed in
5:25
we haven't done anything with that we're
5:26
just directly passing it here but
5:28
password is not going to be the password
5:31
that was passed in that's very important
5:32
it is the hashed password so if we play
5:36
around with that I'm gonna open up
5:38
ipython over here I'll run my app dot py
5:44
and I have this method user dots
5:48
register and I'll pass in a username
5:52
like Colts sure something simple and
5:56
then a password my chickens 87
6:01
exclamation point ampersands are cool
6:04
all right well let's how I'm gonna do it
6:09
I didn't save that to a variable let's
6:11
save that to a variable we'll call it
6:13
Colts and now if we look at Colts it has
6:19
a username and colt has a password but
6:23
it is not this password it's the bcrypt
6:26
hashed version of this password and it
6:29
looks like this and if I were then to
6:31
save it to the database so DB session
6:34
dot add Colts DB session dot commit
6:40
now I look at Colt there should also be
6:43
an ID of three if I go over to my
6:46
database I need to switch I'm using the
6:49
bad password database what did I call
6:52
this password database or this user
6:54
hashing login okay so I'm going to
6:56
connect to hashing login select star
6:59
from users and here we go
7:05
each user has an ID I made a few
7:07
accounts
7:08
Stevi chicks I just made Colt willy
7:10
wonka was from before I started
7:13
recording and then we have our bcrypt
7:15
hashes that are in the database that's
7:17
all we store okay so that is the
7:20
register method it's a class method and
7:22
it simply returns a new user object a
7:25
new instance of the user model where the
7:28
username is coming directly from the
7:29
form but the password has been hashed so
7:32
you don't have to have a class method to
7:34
do this you could put all of this logic
7:35
right in your routes or in the view
7:37
function but it's just best practice to
7:39
move it into the model because it has to
7:41
do with the user model then we have the
7:45
other side of things which is
7:46
authenticating our user so when they go
7:48
to login we want to make sure that their
7:51
password matches and if it doesn't then
7:53
we'll return something false and if it
7:56
does match if they are authenticated
7:58
they have the correct password then
8:00
we'll return the user object itself so
8:03
let me show you how this works we pass
8:05
in a username and a password
8:07
coming from a form again when a user
8:09
logs in we take that username and we use
8:12
it to find the first user that matches
8:14
we used to find the user basically the
8:17
reason we wouldn't do like dot one is
8:19
that a username could potentially be
8:22
typed incorrectly and we don't want our
8:24
app to break because remember the dot 1
8:26
method in sequel alchemy is only going
8:29
to be happy with us if it finds exactly
8:32
one user not zero so if there's not a
8:35
user found with that username it's going
8:36
to break dot first is more forgiving but
8:39
we're not using dot first because we
8:41
think there might be more than one there
8:43
should only be zero or one users with
8:45
this exact username anyway we find the
8:48
user so whatever it is we find it then
8:50
we check okay is there a user first of
8:53
all
8:53
if not then we know already they're not
8:56
going to be able to login if they're
8:57
trying to use a username we don't know
8:59
about but if there is a user that we
9:01
found then we call bcrypt check password
9:03
hash the same method we saw last video
9:05
and then we pass in the password from
9:08
the user object in our database this
9:11
thing right here and then the password
9:15
that was passed in from the forum and
9:17
then that should return true or false
9:19
we've seen that previously so if we get
9:22
true we've returned the user itself and
9:25
that's useful because when somebody logs
9:27
in maybe we just want to know you know
9:30
do they have the right password or not
9:32
but usually we also want to know who is
9:35
this user because we'll want to store
9:37
something in the session so we can
9:39
remember that they're logged in and
9:41
we'll talk about that more later so
9:43
let's try this authenticate method so we
9:47
have our user here user object I have
9:49
Colts but if I just call user dot
9:52
authenticate and I pass in a username
9:55
and a password let's do one that doesn't
9:57
match it gives us false but if I do one
10:02
that does match which I already forgot
10:04
my password we're west of that line I'm
10:06
not going to type that and I put this
10:11
here imagine it's coming from a form it
10:15
returns the user object that represents
10:18
me in the table user with ID of three
10:22
okay so we have those two methods set up
10:24
and then to use them as I've already
10:27
demonstrated in ipython we call them on
10:29
the class they are class methods and if
10:32
we inspected our database like it just
10:34
showed you we won't have any plaintext
10:36
passwords if somebody got ahold of this
10:38
it doesn't mean a whole lot it would
10:41
take a very long time for anybody to
10:43
figure out or to brute-force their way
10:45
through just one of these passwords so
10:48
we're doing it the safe way this is a
10:51
million trillion kajillion times better
10:53
than directly storing the plaintext
10:55
password which is an awful idea and you
10:57
should never ever do you should always
10:59
use be crypts at a bare minimum and if
11:03
there is some other password hashing
11:05
algorithm that comes out that
11:07
security experts claim and approve of as
11:10
better than bcrypt than shirt we use
11:12
that but you should never try and roll
11:14
your own thing from scratch and make up
11:15
your own hashing algorithm that's a
11:17
recipe for massive disaster ok so that's
11:21
the basics of setting up our class
11:24
methods next we'll talk about how we
11:26
actually keep someone logged in
