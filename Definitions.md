Nested Routes: A routing technique used in web development when one resource is associated with another resource. For example, if you have subreddits and posts, you may want to have a nested route to show the posts associated with a specific subreddit.

Avoid deep nesting: A rule of thumb to avoid nesting routes more than two resources deep to maintain simplicity and readability of the URLs.

Flexibility: The freedom to structure nested routes according to the requirements of your API. There's no strict rule for structuring nested routes, and depending on your API's needs, you may decide to include or exclude certain resource IDs in the URL.

RESTful routes: A standardized approach to designing networked applications, based on the principles of Representational State Transfer (REST). RESTful routes follow a specific pattern that includes HTTP verbs (GET, POST, PUT, PATCH, DELETE) and specific URL structures, defining how resources should be created, read, updated, and deleted.

WTForms-Alchemy: A Flask add-on that combines WTForms and SQLAlchemy to generate forms directly based on your SQLAlchemy model, automatically creating validators based on model constraints. It speeds up development on larger projects.

Flask-Login: A Flask add-on that provides functionality around authentication, including methods like login_user and logout_user, providing a current_user attribute, and offering decorators like login_required to protect views. It simplifies the process of setting up user authentication in a Flask application.

Flask-Mail: A Flask add-on for sending emails that simplifies the process of sending emails, bulk emails, and adding attachments. It can be used to send reminder emails, notifications, and other types of messages.

Flask-Admin: A Flask add-on that quickly creates an admin interface based on existing models, working well with SQLAlchemy. It allows admins to view, edit, delete, and create new entities, saving time by automatically generating CRUD interfaces for models.

Flask-Restless: A Flask add-on that creates a RESTful CRUD API based on your SQLAlchemy models. It automatically generates API endpoints for your models, making it easy to create a RESTful API without writing all the necessary code.


Bcrypt: A password hashing algorithm that combines the Blowfish cipher with another password algorithm called crypt. It is considered safe, popular, and has implementations in many programming languages.

Salt: A random string used in conjunction with a password when hashing it to create a unique hash output. This prevents the use of precomputed tables, such as rainbow tables, for reversing hashes back into passwords.

Work Factor: A parameter in the Bcrypt algorithm that specifies the number of rounds of hashing to perform. Increasing the work factor makes the hash slower to compute, making it more resistant to brute force attacks.

Binary String: A string representation of binary data used in programming languages, such as Python. In Python, binary strings are indicated by the prefix "b".

Hashing: The process of converting an input, such as a password, into a fixed-size output, which is the hash. This process should be deterministic, meaning that the same input should always generate the same hash.

Authentication: The process of verifying a user's identity by checking if the password they provide matches the stored hash in the database. This is done by hashing the provided password with the stored salt and comparing the output to the stored hash.

JSON API: A JSON API is an application programming interface that uses JSON (JavaScript Object Notation) for exchanging data between a server and a client.

Flask app: Flask is a micro web framework for Python that allows you to build web applications easily.

HTML, JavaScript, and CSS: The core technologies used to build and style websites, with HTML providing the structure, JavaScript providing interactivity, and CSS providing styling.

Axios: A popular JavaScript library used to make HTTP requests from the browser.

jQuery: A popular JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling and animation.

API request and response: The process of sending a request to an API and receiving a response containing the requested data.

Data attribute: A custom attribute that stores data in HTML elements, which can be easily accessed and manipulated with JavaScript and jQuery.

Safe: In the context of HTTP requests, a safe operation is one that does not change the data being requested. Among the HTTP verbs (GET, POST, PATCH, PUT, and DELETE), only the GET request is considered safe.

Idempotent: In the context of HTTP requests, an idempotent operation is one that can be repeated multiple times with the same result. The following HTTP verbs are considered idempotent: GET, PUT, PATCH, and DELETE (although DELETE can be a bit tricky).

GET request: A safe and idempotent operation that retrieves data from a specified resource.

POST request: A non-idempotent operation that submits data to be processed to a specified resource, usually resulting in the creation of a new resource. Each time a POST request is sent, a new resource is created, making it non-idempotent.

PUT request: An idempotent operation that updates an existing resource with new data. Repeating the operation multiple times will have the same effect as performing it once.

PATCH request: An idempotent operation that partially updates an existing resource with new data. Similar to PUT, repeating the operation multiple times will have the same effect as performing it once.

DELETE request: An idempotent operation that deletes a specified resource. Although it is considered idempotent, DELETE can be tricky, as the resource is removed, and further requests for the same resource may result in errors or different responses.

REST (Representational State Transfer): A set of architectural principles and guidelines for designing networked applications. RESTful APIs follow these guidelines and make use of HTTP verbs to indicate the desired action on a resource.

JSONify method: A Flask method used to convert

Authentication: The process of verifying the identity of a user, device, or system.
Authorization: The process of determining what a user is allowed to do.
Hashing: A cryptographic function that takes an input of any length and produces an output of a fixed length.
Cryptographic hashing functions: Hashing functions that have specific restrictions, such as no association between input and output, and a small change in input results in a radically different output.
Password hashing algorithms: Recommended algorithms for hashing passwords, such as Bcrypt. These algorithms have been extensively researched and are considered secure for password storage.
Bcrypt: A popular password hashing algorithm that is considered secure and widely used in the industry.
MD5 and SHA family (e.g., SHA-256): Examples of cryptographic hash functions that are fast but not suitable for storing passwords. These are used in various applications like cryptocurrencies.
Reverse lookup table: A table or dictionary that maps the hash values to their corresponding passwords. This can be used by attackers to find passwords by looking up the hash values.
Salting or password salts: A random string that is introduced before hashing the password. This adds an extra layer of security by making it much harder for an attacker to generate a reverse lookup table or use precomputed hash tables (rainbow tables) for cracking passwords.
Rainbow table: A more sophisticated version of a reverse lookup table, which is also used by attackers to crack passwords.
Collision: A situation in which two different inputs to a hash function produce the same output. Salting helps to reduce the likelihood of collisions.
Cryptographic hash functions: Hash functions that are designed to be secure for cryptographic purposes, such as password storage. Bcrypt is an example of a cryptographic hash function.
Plain text password storage: Storing users' passwords in an unencrypted format, which is a bad practice and leads to security vulnerabilities.
Password comparison: Comparing the user's input password with the stored password in the database to authenticate the user.
Password reuse: The practice of using the same password for multiple websites or services, which is discouraged for security reasons.
Password manager: A tool that helps users create, store, and manage strong, unique passwords for each website or service they use.
Two-factor authentication: An extra layer of security that requires a user to provide two different types of identification, such as a password and a fingerprint or a one-time code sent to their phone.
Python hash function: A built-in Python function for generating hash values, which is not suitable for hashing and storing passwords.
Cost factor or work factor: A variable in Bcrypt that can be increased to make the hashing process slower, compensating for advances in computer hardware and maintaining a high level of security.
Security vulnerability: A weakness in a system that can be exploited by an attacker to gain unauthorized access or control.
Flask Sessions: Flask sessions are used to persist information and add state on top of the HTTP protocol, which is stateless by default. They are crucial for remembering if a user is logged in or not.
User Authentication: Users are authenticated by checking their submitted credentials against stored user data in the database. The class method user.authenticate is used to achieve this.
Storing User ID in the Session: When a user logs in successfully, their user ID is stored in the session, which can then be used to determine if the user is logged in or not.
Displaying Content Based on User Status: Based on the presence of the user ID in the session, you can show or hide content in your templates or control access to certain routes.
Protecting Routes: You can add logic to your view functions to ensure that only logged-in users can access certain routes. If a user is not logged in, you can redirect them to a different page

Python: A popular, high-level programming language known for its readability and extensive standard library.

Standard Library: A collection of modules that come bundled with Python, providing functionality for a wide range of tasks.

Dynamic Language: A language that allows developers to create, modify or delete constructs like classes, methods, or functions during the execution of a program.

Dynamically Typed: A characteristic of programming languages where variables can change their type during the execution of the program.

Strongly Typed: A characteristic of programming languages that enforce strict rules on mixing data types during operations and do not automatically convert between types.

setattr(): A built-in Python function that allows developers to set the value of a named attribute of an object dynamically. The syntax is: setattr(object, attribute_name, value).

Generators: An easy way to create iterators in Python that allow you to produce one value at a time, rather than generating all values at once.

Generator functions: These are functions that contain the "yield" keyword, which returns a value and pauses the function's execution until the next value is requested.

Yield keyword: A keyword used in generator functions that returns a value and pauses the function's execution until the next value is requested. The function then resumes from where it left off.

Generator object: An iterator that is returned when a generator function is called, allowing you to iterate over a sequence of values.

Laziness: A term used to describe the process of generating values only when they are needed, instead of generating all values at once. Generators implement lazy evaluation, which can save memory and improve performance.

Iterators: Objects that allow you to iterate over a collection of values, such as lists, tuples, or strings. Generators are a type of iterator in Python.

StopIteration exception: This exception is raised when the generator reaches the end of its iteration. It signals to the loop or other iterable construct that there are no more values to be generated.

Jupyter: A popular tool in the world of Python, allowing for the creation of interactive documents that can run code, edit code, display code output, create charts, and add documentation, all within a webpage.

Interactive documents: Documents that contain code, charts, and documentation, which can be edited, run, and shared with others. These documents are often used for reports, tutorials, or teaching materials in fields like data science.

Jupyter Notebook: A web-based interface that allows users to create, edit, and run Jupyter interactive documents. It can be launched from the command line and supports multiple languages, including Python.

Code blocks: Sections of code within a Jupyter Notebook that can be executed independently, allowing users to step through the document, running and tweaking code as needed.

Markdown: A lightweight markup language used in Jupyter Notebooks for formatting text, including headings, lists, and links.

Collaboration: Jupyter Notebooks can be shared and collaborated on in real-time, similar to Google Docs, allowing multiple users to contribute, write notes, and add comments.

Jupyter Lab: A newer product from the Jupyter project, offering an integrated development environment for working with notebooks, code, and data.

Authentication: The process of verifying the identity of a user.

Authorization: The process of determining what a user is allowed to do.

Hashing: A cryptographic function that takes an input of any length and produces an output of a fixed length.

Session: A temporary state associated with a user.

Bcrypt: A password hashing function that is designed to be slow to compute.

Flash messages: Temporary, contextual messages displayed to users to give feedback on the outcome of an action or process.

Bootstrap alerts: A collection of pre-styled elements in the Bootstrap framework for displaying contextual feedback messages to the user



