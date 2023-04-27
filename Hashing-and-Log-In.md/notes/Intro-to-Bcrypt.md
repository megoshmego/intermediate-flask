Video Title: Intro-to-Bcrypt

Section Title: Intermediate Flask

Subsection Title: Hashing and Logging In

Key Terms, Ideas, and Concepts:

Cryptographic hashing functions: A subset of hashing functions with specific restrictions, where a small change in input results in a radically different output. There should be no way to gain any information about the inputs by comparing the outputs.

Salt: A random value generated and combined with the password before hashing. It ensures that the same password with different salts will have different hashes, making it more difficult to crack the passwords.

MD5 and SHA family (e.g., SHA-256): Examples of cryptographic hash functions that are fast but not suitable for storing passwords. These are used in various applications like cryptocurrencies.

Password hashes: Hashing algorithms specifically designed for storing passwords, such as Bcrypt, Argon2, and Scrypt. They are slower compared to fast cryptographic hashes like SHA-256, which is a desirable feature for securely storing passwords.

Bcrypt: A password hashing algorithm that has been around since 1999 or 2000. It is a slow hash, which makes it suitable for storing passwords. It is still widely recommended by security experts.

Cost factor or work factor: A variable in Bcrypt that can be increased to make the hashing process slower, compensating for advances in computer hardware and maintaining a high level of security.

Definitions:

Cryptographic hashing functions: Hashing functions that have specific restrictions, such as no association between input and output, and a small change in input results in a radically different output.

Salt: A random value generated and combined with a password before hashing to ensure that the same password with different salts will produce different hashes.

Password hashes: Hashing algorithms specifically designed for storing passwords, which are slower compared to general-purpose cryptographic hash functions.

Bcrypt: A password hashing algorithm that is considered slow and secure, suitable for securely storing passwords. It has been widely recommended by security experts despite its age.


Certainly! Here's a Python example demonstrating how to use Bcrypt for password hashing and verification. This example assumes you have the bcrypt library installed. If not, you can install it using pip:

Copy code
pip install bcrypt
Now, let's see how to hash a password and verify it using Bcrypt:

python
Copy code
import bcrypt

# Hash a password
def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

# Verify a password
def verify_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Example usage
password = "mypassword123"

# Hash the password
hashed_password = hash_password(password)
print(f"Hashed password: {hashed_password}")

# Verify the password
is_correct = verify_password(password, hashed_password)
print(f"Password is correct: {is_correct}")

# Attempt to verify an incorrect password
wrong_password = "wrongpassword"
is_correct = verify_password(wrong_password, hashed_password)
print(f"Password is correct: {is_correct}")
This code demonstrates how to create a hashed password using Bcrypt and how to verify if a given password matches the stored hashed password. You can use these functions to store hashed passwords and authenticate users in your applications.

Remember, never store plain text passwords. Always store hashed passwords and use a reliable hashing algorithm like Bcrypt.


