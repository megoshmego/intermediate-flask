Title: Other HTTP Verbs Course Section: Intermediate Flask Subsection: Restful JSON APIs 

Key terms and concepts covered in this video: 

 The video discusses how to create a RESTful JSON API using Flask and covers the different HTTP verbs, including GET, POST, PUT, PATCH, and DELETE. The instructor also talks about the limitations of HTML forms, which only support GET and POST requests, while JavaScript and server-side languages can use all the HTTP verbs. 


API: An Application Programming Interface allows different software applications to communicate with each other. In this context, it refers to creating an API with Flask that responds with JSON data. 

HTTP Verbs: These are methods used to indicate the desired action to be performed on a given resource. The main HTTP verbs discussed in the video are GET, POST, PUT, PATCH, and DELETE. 

REST (Representational State Transfer): A software architectural style used for designing networked applications. RESTful APIs use HTTP requests to access and manipulate data. 

GET Request: This HTTP verb is used to request data from a specified resource. It is typically used to retrieve data without any side effects on the server. 

POST Request: This HTTP verb is used to submit data to a specified resource, often resulting in a change on the server-side, such as updating or creating new data. 

PUT Request: This HTTP verb is used to update an entire resource with the supplied data. 

PATCH Request: This HTTP verb is used to partially update a resource, meaning only the specified fields will be updated. 

DELETE Request: This HTTP verb is used to delete a specified resource. 

CRUD (Create, Read, Update, Delete): These are the basic operations performed on a resource in an API. 

 
## EXAMPLES 

GET: Retrieves data from a specified resource. Example: 

 

        import requests 

        response = requests.get("https://api.example.com/users") 
        print(response.text) 

 
POST: Submits data to be processed to a specified resource. Example: 

 

        import requests 

        data = {'name': 'John Doe', 'email': 'john.doe@example.com'} 
        response = requests.post("https://api.example.com/users", data=data) 
        print(response.text) 
 

PUT: Updates an existing resource with new data. Example: 

 

        import requests 

        data = {'name': 'John Doe', 'email': 'john.doe@example.com'} 
        response = requests.put("https://api.example.com/users/1", data=data) 
        print(response.text) 

 

 

PATCH: Partially updates an existing resource with new data. Example: 

 
        import requests 

        data = {'email': 'john.doe@example.com'} 
        response = requests.patch("https://api.example.com/users/1", data=data) 
        print(response.text) 

 

 

DELETE: Deletes a specified resource. Example: 

 

        import requests 

        response = requests.delete("https://api.example.com/users/1") 
        print(response.text) 
 
 

 


 