#Title: "Safety and Idempotency" Section: "Intermediate Python" Subsection: "Restful JSON" 

Key terms, concepts, and definitions: 

Safe: In the context of HTTP requests, a safe operation is one that does not change the data being requested. Among the HTTP verbs (GET, POST, PATCH, PUT, and DELETE), only the GET request is considered safe. 

Idempotent: In the context of HTTP requests, an idempotent operation is one that can be repeated multiple times with the same result. The following HTTP verbs are considered idempotent: GET, PUT, PATCH, and DELETE (although DELETE can be a bit tricky). 

GET request: A safe and idempotent operation that retrieves data from a specified resource. 

POST request: A non-idempotent operation that submits data to be processed to a specified resource, usually resulting in the creation of a new resource. Each time a POST request is sent, a new resource is created, making it non-idempotent. 

PUT request: An idempotent operation that updates an existing resource with new data. Repeating the operation multiple times will have the same effect as performing it once. 

PATCH request: An idempotent operation that partially updates an existing resource with new data. Similar to PUT, repeating the operation multiple times will have the same effect as performing it once. 

DELETE request: An idempotent operation that deletes a specified resource. Although it is considered idempotent, DELETE can be tricky, as the resource is removed, and further requests for the same resource may result in errors or different responses. 

REST (Representational State Transfer): A set of architectural principles and guidelines for designing networked applications. RESTful APIs follow these guidelines and make use of HTTP verbs to indicate the desired action on a resource. 

By adhering to these conventions, developers can create more intuitive and standardized APIs, making it easier for others to understand and use them. 

 

Title: "Safety and Idempotency" 

##Here are simple demonstrations of the concepts covered in the video: 

Safety: An operation is considered safe if it doesn't change the data it requests. 

Example: 

 

GET /api/pokemon/1 

This GET request retrieves information about a Pokémon with ID 1. It doesn't change any data on the server, so it's considered safe. 

Idempotency: An operation is idempotent if performing it multiple times produces the same result. 

Examples: 

a) GET /api/pokemon/1 (Idempotent) 

No matter how many times we send this GET request, we should receive the same information about Pokémon with ID 1. 


b) PUT /api/pokemon/1 (Idempotent) 
 

Imagine we want to update a Pokémon with ID 1 with the following data: 

{ "name": "Bulbasaur", "type": "Grass" } 

If we send this PUT request multiple times, the Pokémon with ID 1 will always be updated with the same data, producing the same result. 

c) POST /api/pokemon (Not idempotent) 
 

{ "name": "Charmander", "type": "Fire" } 

Every time we send this POST request, a new Pokémon will be created with the given data. Sending this request multiple times will result in multiple Charmander Pokémon entries in the database, so it's not idempotent. 

d) DELETE /api/pokemon/1 (Idempotent)  

Sending a DELETE request to remove Pokémon with ID 1 should produce the same result regardless of how many times the request is sent. However, after the first request, the Pokémon will be deleted, and subsequent requests might return an error such as 404 Not Found, because the resource is no longer available. 

 

