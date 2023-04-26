Would you please evaluate the transcript I provide for it's key terms, ideas, concepts and their defintions. Would you also please include the video title "Flask-Bcrypt", the subsection title "Hashing and Loggin In", and the section title "Intermediate Flask"?



0:00
(bright music)
0:04
- [Instructor] All right, so next,
0:06
I'm going to introduce the flask wrapper for Bcrypt
0:09
that we'll be using.
0:10
We could just use regular old Bcrypt,
0:12
like we've been doing an I Python,
0:14
but there's a flask version that makes it easier
0:16
for us to use because Bcrypt here has applications outside
0:20
of simply are just storing passwords in a flask app
0:24
or in a web application.
0:26
The flask wrapper just makes it easy.
0:29
We don't have to generate assault on our own.
0:31
We simply call generate password hash,
0:33
and we pass in the password from a user.
0:35
So replace that with whatever the user has typed in.
0:39
We're getting it from a form.
0:40
And then that gives us a hash we can store in our database.
0:43
Then we can call, check password hash.
0:47
So when a user is logging in and we pass into hash
0:51
from our database and whatever the user has typed in,
0:54
whatever their attempt at logging in is we take
0:56
that password and this will return true or false.
1:00
So let's try it.
1:01
We need to PIP install flask Bcrypt,
1:04
which I've already done.
1:06
And then we can import Bcrypt from flask underscore Bcrypt.
1:11
Next, we do need to instantiate Bcrypt.
1:14
So we need to call it with parenths, just like that.
1:17
And then we have this method
1:19
on it called Bcrypt dot generate, password hash.
1:26
Then we can have some password from a user,
1:28
which actually, I think I'm going to edit this.
1:32
I'm going to type a password in.
1:33
So we'll never actually see the password.
1:34
I'm going to make a variable and then clear my screen.
1:38
Okay, so I have a password
1:39
in a variable called user password.
1:43
I think I just did PWD, user underscore password.
1:47
So now I can call Bcrypt dots, generate password hash.
1:53
This is a method that we get from the flask Bcrypt version,
1:56
the flask wrapper.
1:57
And then it can pass in that user password.
2:00
And that generates for us the password hash.
2:04
So this is what we would store in the database.
2:07
And if I do it again, we actually get a different results.
2:11
Why is that?
2:12
Well, it's generating a salt each time.
2:15
So it's giving us a new random salt that's generated.
2:18
And it uses that to create the hash.
2:21
It's hashed in with the password, whatever user password is.
2:24
But remember, it also stores the salt in this hash.
2:28
Once we call this other method, check password hash.
2:31
So I'm going to do this and save this to a variable.
2:34
I'll call this...
2:36
Let's see, let's just go with H.
2:40
Okay, so we have H.
2:41
This is what we would store in our database.
2:43
Then if a user is logging in, Bcrypt dot check password hash
2:49
is what we would call.
2:50
And then we pass in the hash, which is H and then,
2:54
whatever the user typed into a form,
2:56
let's say it's user password, they got it right.
2:59
Type the same password in.
3:01
This hash contains information about the salt
3:05
that was generated.
3:06
Bcrypt takes the salts out of this,
3:08
it determines what the salt is.
3:10
Then it combines it with the user password that we pass in.
3:14
It hatches that and it compares the result
3:16
to what we have here.
3:18
And we get true.
3:20
Now, if we look at user password, it's hippobrains1999.
3:27
If I passed in something slightly different,
3:30
we should get false.
3:32
How about Huppobrains1999, like that?
3:37
We get false, it's not a match.
3:39
So here is our first version.
3:42
It's not really authentication at this point,
3:44
but the code, the logic that we'll be using
3:47
will be very straightforward.
3:49
When a user signs up, we'll take their password
3:51
and run generate password hash
3:54
and we'll store whatever that hash is in our database.
3:56
This is what we actually put in the database.
3:59
Then when they go to login,
4:01
they'll type a password and a username in.
4:03
We take that username and we find the correct user
4:06
in our database.
4:07
We find this hash that we've stored.
4:09
No plain text password, we just store this.
4:12
And then we take whatever the user typed
4:13
in as their password and we pass that in
4:16
to check password hash alongside this hash
4:19
from our database.
4:20
And Bcrypt will tell us if it's a match
4:22
or if it's not a match.
4:24
And if it is a match, then we can log them in.
4:26
If it's not a match, we'll show them an error
4:29
or we'll redirect them or do something.
4:31
So that's the basic logic for storing the password
4:34
or not really storing it,
4:35
but generating the password hash and then,
4:38
checking or authenticating that somebody's password matches
4:41
what they signed up with.
4:44
So next, we'll actually see the code in a flask application.
4:48
That's up next.
4:49
(light music)
