Video Title: Built in Hash Functions
Section Title: Intermediate Flask
Subsection Title: Hashing and Logging In

Key Terms, Ideas, and Concepts:

Built-in hash function: A function available in Python that accepts an input and generates a hash value without requiring any imports. This function is not suitable for storing passwords due to various reasons.

64-bit space: The built-in hash function in Python maps the input to a 64-bit space, which means it uses 64 bits in memory to store the hash value.

Consistent hash values: The built-in hash function will generate the same hash value for a given input in the same implementation of Python, but the output may differ depending on the architecture, machine, and specific build of Python.

Collisions: Hash functions may generate the same hash value for different inputs. The built-in hash function in Python is relatively prone to collisions compared to other cryptographic hash functions.

Fast vs. slow hash functions: A fast hash function is not suitable for password storage, as it enables attackers to brute force their way through the hash values. Cryptographic hash functions are designed to be slow to provide better security.

Hash maps: A data structure that uses a hash function for implementation. Python dictionaries are an example of hash maps. Hash maps are fast for data retrieval and insertion, regardless of the number of key-value pairs.

Hashable and non-hashable keys: In Python dictionaries, keys must be hashable. Mutable types, such as lists, are non-hashable, while immutable types, such as numbers, strings, and booleans, can be hashed.

The built-in hash function in Python is not suitable for storing passwords due to its smaller output space (64 bits), faster computation, and higher collision probability. However, it is used in Python dictionaries, which are examples of hash maps. Dictionaries are fast and efficient for data retrieval and insertion. The keys in dictionaries must be hashable, which means they must be immutable data types.



Certainly! Here's a demonstration of some key concepts mentioned in the video using Python code:

Using Python's built-in hash function:
python
Copy code
hash_value = hash("penguin")
print("Hash value for 'penguin':", hash_value)
Hashing different strings and checking for collisions:
python
Copy code
hash_value1 = hash("penguin")
hash_value2 = hash("Penguin")
hash_value3 = hash("penguin!")

print("Hash value for 'penguin':", hash_value1)
print("Hash value for 'Penguin':", hash_value2)
print("Hash value for 'penguin!':", hash_value3)
Demonstrating Python dictionaries (hash maps):
python
Copy code
# Creating a dictionary
my_dict = {"name": "Harry", "house": "Gryffindor"}

# Retrieving a value using the key
print("Value for 'house':", my_dict["house"])

# Inserting a new key-value pair
my_dict["age"] = 17
print("Updated dictionary:", my_dict)
Attempting to use a non-hashable key in a dictionary:
python
Copy code
my_list = [1, 2, 3]

try:
    my_dict = {my_list: "This will fail"}
except TypeError as e:
    print(f"Error: {e}")
These code examples should help illustrate the concepts from the video. Remember that the built-in hash function is not suitable for password storage, and you should use dedicated password hashing libraries like bcrypt or Argon2 for that purpose.
