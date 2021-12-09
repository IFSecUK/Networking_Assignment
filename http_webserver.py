#!/usr/bin/python3
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


HOST_NAME = 'localhost'
PORT_NUMBER = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
    	url_path = self.path.split("/")
    	if len(url_path) == 4:
    		self.send_response(200)
    		self.end_headers()
    		try:
    			if url_path[1] == 'add':
    				result = int(url_path[2]) + int(url_path[3])
    				self.wfile.write(b'Result of Addition: ' + str(result).encode())
    			elif url_path[1] == 'sub':
    				result = int(url_path[2]) - int(url_path[3])
    				self.wfile.write(b'Result of Subtraction: ' + str(result).encode())
    			elif url_path[1] == 'mul':
    				result = int(url_path[2]) * int(url_path[3])
    				self.wfile.write(b'Result of Multiplication: ' + str(result).encode())
    			elif url_path[1] == 'div':
    				result = int(url_path[2]) / int(url_path[3])
    				self.wfile.write(b'Result of Division: ' + str(result).encode())
    			else:
    				self.wfile.write(b'Please check your request again...')
    		except ZeroDivisionError:
    			self.wfile.write(b'Sorry, You cannot divide bt Zero...')
    	else:
    		self.send_response(400)
    		self.end_headers()
    		self.wfile.write(b'Please send a request as described below\n\n')
    		self.wfile.write(b'[+]-------Menu----------\n')
    		self.wfile.write(b'1. Addition - Example: http://localhost:8000/add/10/20\n')
    		self.wfile.write(b'2. Subtraction - Example: http://localhost:8000/sub/10/5\n')
    		self.wfile.write(b'3. Multiplication - Example: http://localhost:8000/mul/10/5\n')
    		self.wfile.write(b'4. Division - Example: http://localhost:8000/div/10/5\n')

    def do_POST(self):
    	result_dictionary = {}
    	cType = self.headers['Content-Type']
    	
    	if cType != 'application/json':
    		self.send_response(400)
    		self.end_headers()
    		self.wfile.write(b'Send your operations in JSON format or mention explicitly with --header flag using curl')
    	
    	else:
	    	self.send_response(200)
	    	self.end_headers()

	    	
	    	try:
	    		content_length = int(self.headers['Content-Length'])
	    		message = json.loads(self.rfile.read(content_length))
	    		
	    		if message['operations'] == 'add':
	    			result_dictionary["Result"] = int(message['arguments'][0]) + int(message['arguments'][1])
	    			self.wfile.write(json.dumps(result_dictionary, indent=2).encode())

	    		elif message['operations'] == 'sub':
	    			result_dictionary["Result"] = int(message['arguments'][0]) - int(message['arguments'][1])
	    			self.wfile.write(json.dumps(result_dictionary, indent=2).encode())
	    		
	    		elif message['operations'] == 'mul':
	    			result_dictionary["Result"] = int(message['arguments'][0]) * int(message['arguments'][1])
	    			self.wfile.write(json.dumps(result_dictionary, indent=2).encode())
	    		
	    		elif message['operations'] == 'div':
	    			result_dictionary["Result"] = int(message['arguments'][0]) / int(message['arguments'][1])
	    			self.wfile.write(json.dumps(result_dictionary, indent=2).encode())
	    		else:
	    			raise(KeyError)

	    	except KeyError:
	    		self.wfile.write(b'Please check your json input. It should be in the format of {"operations":"add/sub/mul/div","arguments":[a,b]}')
	    	except ZeroDivisionError:
	    		self.wfile.write(b'Sorry, You cannot divide bt Zero...')
	    	except json.decoder.JSONDecodeError:
	    		self.wfile.write(b'Please check your post data. Its not in proper format. It should be like this: {"operations":"add/sub/mul/div","arguments":[a,b]}')


if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), SimpleHTTPRequestHandler)
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n")
    httpd.server_close()
    print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))

