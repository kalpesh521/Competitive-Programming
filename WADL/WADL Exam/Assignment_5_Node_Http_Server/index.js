
//  https://www.guru99.com/node-js-create-server-get-data.html

 

var http=require('http') // Import Node.js core module

var server=http.createServer((function(request,response) //	Create a server object
{
	response.writeHead(200, 
	{"Content-Type" : "text/plain"});// Send the HTTP header HTTP Status: 200 : OK Content Type: text/plain
	response.end("Hello from kalpesh\n");// Send the response body "Hello World"
}));
server.listen(8000,()=>{ // Bind server to a port
    console.log("Server is running on port 8000"); // Run the server
});


