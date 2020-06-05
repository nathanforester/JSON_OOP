### JSON and APIs

## JSON: JavaScript object notation
- Object is both dictionary and array/list
- Is the web standard for APIs and front end development
- Front end languages - CSS, HTML, JS
- Netscape created JavaScript and developer SSL, founded by Mozilla
- Utilises simple text files that languages can parse with built in function to interpret and run it


## API: application programming interface

- Multiple software intermediary
- REST APIs most common
- Many APIs request that a user identify/verify themselves
- Allows programmers to access specific features or data of a specific application, operating system or web services
- Google maps API - JSON request back
- Error message: must use and API key to authenticate error request


## GET request

- HTTP GET request: used to request data from a specified source
- One of the most common HTTP methods
- query string example ML
````GET/test/demo_form.php?name1=value1&name2=value2````

- Can be cached, remains in browser history, bookmarked and should not be used when dealing with sensitive data
- has a length restriction
- only used to request data (not modify)

## POST request

- Used to send data over a server to create/update a resource
- The data sent to the server with POST is stored in the request body for the HTTP request:
```POST/test/demo_form.php/HTTP/1.1```
- POST is one of the most common HTTP orders

- POST requests are never cached, do not remain in browser history and cannot be bookmarked
- No restriction on data length
