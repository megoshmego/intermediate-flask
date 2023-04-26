Title: Intro to Hashing
Course: Intermediate Python
Section: Hashing and Log In

Key Terms and Concepts:

Hashing: A process of taking some input data and mapping it to a fixed-size output.
Hash function: A function that takes input data of any size and returns a fixed-size output.
Deterministic: A property of hash functions where the same input always produces the same output.
Cryptographic Hash function: A special subset of hash functions used in cryptography with additional requirements, such as being a one-way function.
One-way function: A function where, given the output, it is computationally infeasible to determine the input.
In the video, the speaker explains the concept of hashing and its importance in storing passwords securely. They emphasize that storing passwords in plain text is a terrible idea. Instead, they recommend using a hash function to transform the password into a fixed-size output that cannot be reverse-engineered to obtain the original password. This hashed password is then stored in the database. When a user logs in, the entered password is hashed using the same function, and the output is compared to the stored hashed password to verify if they match.

Demos:

Implementing a simple hash function to understand the concept.
Using cryptographic hash functions for password storage and authentication.
Comparing input and hashed passwords during login.
The video covers the general concept of hash functions, their determinism, and the additional requirements of cryptographic hash functions. It also provides examples to illustrate the properties of one-way functions and their application in secure password storage.

Demo 1: Implementing a simple hash function

In this demo, we'll create a basic hash function for demonstration purposes. Note that this should not be used for actual password hashing, as it is not secure enough for production use.

python
Copy code
def simple_hash(password, fixed_size=10):
    hashed = 0
    for char in password:
        hashed += ord(char)
    hashed = hashed % fixed_size
    return str(hashed).zfill(fixed_size)

password = "CharlieBitMe"
hashed_password = simple_hash(password)
print(f"Original password: {password}")
print(f"Hashed password: {hashed_password}")
Demo 2: Using cryptographic hash functions for password storage and authentication

In this demo, we'll use the hashlib library to securely hash passwords using the SHA-256 cryptographic hash function.

python
Copy code
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = "CharlieBitMe"
hashed_password = hash_password(password)
print(f"Original password: {password}")
print(f"Hashed password: {hashed_password}")

# To verify the password during login:
login_password = "CharlieBitMe"
hashed_login_password = hash_password(login_password)

if hashed_password == hashed_login_password:
    print("Password is correct.")
else:
    print("Password is incorrect.")
These demos should help you understand the basic concept of hashing, how to use a cryptographic hash function for password storage, and how to verify hashed passwords during the login process. Keep in mind that for production use, you should also incorporate password salting and consider using more secure hashing algorithms like bcrypt or Argon2.