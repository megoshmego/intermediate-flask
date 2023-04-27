Title: Intro to Hash Functions
Section Title: Intermediate Flask
Subsection Title: Hashing and Logging In

Key Terms, Ideas, and Concepts:

Hash functions: Functions that take some input of any size and map it to an output of a fixed size. They are deterministic, meaning the same input will always produce the same output.
Cryptographic Hash functions: A special subset of hash functions used in cryptography. They have additional requirements, such as being one-way functions, meaning you cannot reverse the output to get the original input.
One-way functions: Functions that only allow you to go from input to output, but not from output to input. Examples include absolute value and cryptographic hash functions.
Storing passwords: Instead of storing passwords in plain text, they are hashed using a cryptographic hash function, and the hash is stored in the database. This way, the stored data is more secure and difficult to reverse-engineer.
Logging in: When a user logs in, their entered password is hashed using the same cryptographic hash function, and the resulting hash is compared to the stored hash in the database. If the hashes match, the password is considered correct.
Definitions:

Hash function: A function that takes some input of any size and maps it to an output of a fixed size.
Deterministic: A property of a function that always produces the same output for the same input.
Cryptographic Hash function: A special type of hash function used in cryptography, with additional requirements such as being one-way functions.
One-way function: A function that only allows you to go from input to output, but not from output to input.
Hashing: The process of transforming data using a hash function, often used for passwords in the context of authentication.

I'll provide you with a simple example in Python using the hashlib library, which provides various hash functions, such as SHA-256, which is commonly used in practice. This example demonstrates how to hash a password and verify it against a stored hash.

python
Copy code
import hashlib

def hash_password(password):
    """Hash a password using the SHA-256 algorithm."""
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

def verify_password(stored_hash, password_attempt):
    """Verify if the provided password_attempt matches the stored_hash."""
    password_attempt_hash = hash_password(password_attempt)
    return stored_hash == password_attempt_hash

# Example usage:
password = "MySecretPassword123"
password_hash = hash_password(password)

# Store 'password_hash' in the database instead of the plain-text password

# Later, when a user attempts to log in:
password_attempt = "MySecretPassword123"  # Assume this comes from a user input form

if verify_password(password_hash, password_attempt):
    print("Password is correct!")
else:
    print("Password is incorrect!")
This example demonstrates how to hash a password using the SHA-256 algorithm and how to verify a password attempt against a stored hash. In practice, you would store the hashed password in a database and retrieve it when needed for comparison. Note that for real-world applications, it's recommended to use a more advanced password hashing library such as bcrypt, which adds additional security features like salting and key stretching.
