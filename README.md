# Networking_Assignment
Assignment Solution<br>
Download the repo or all the files and keep them inside the same folder.
<br>
## HTTP Server
This server will be running on port 8000 (Value is hardcoded in the code). Next, simply run
```Bash
python3 http_webserver.py
```
And pass GET/POST requests using curl
```Bash
curl http://localhost:8000/add/1/2
```
#### OUTPUT
GET Request
```Bash
python3 http_webserver.py 
Thu Dec  9 12:07:48 2021 Server UP - localhost:8000
127.0.0.1 - - [09/Dec/2021 12:08:01] "GET /div/1/10 HTTP/1.1" 200 -
^C

Thu Dec  9 12:12:06 2021 Server DOWN - localhost:8000
```
```Bash
curl http://localhost:8000/div/1/10
Result of Division: 0.1                                                                                           
```
POST Request
```Bash
python3 http_webserver.py
Thu Dec  9 12:14:20 2021 Server UP - localhost:8000
127.0.0.1 - - [09/Dec/2021 12:14:22] "POST / HTTP/1.1" 200 -
^C

Thu Dec  9 12:15:08 2021 Server DOWN - localhost:8000
```
```Bash
curl --data '{"operations":"add","arguments":[1,2]}' --header "Content-Type: application/json" http://localhost:8000    
{
  "Result": 3
}                                                                                                                     
```
## HTTPS Version
This version of web server will be running on standard port 443. Make sure to include -k flag with curl command while sending requests because as the certificate is self-signed, curl will throw SSL certificate problem.<br>
GET Request
```Bash
python3 https_webserver.py 
Thu Dec  9 12:17:35 2021 Server UP - localhost:443
127.0.0.1 - - [09/Dec/2021 12:17:42] "GET /add/1/2 HTTP/1.1" 200 -
^C

Thu Dec  9 12:17:50 2021 Server DOWN - localhost:443

```
```Bash
curl -k https://localhost/add/1/2
Result of Addition: 3                                                                                                 
```
POST Request
```Bash
python3 https_webserver.py
Thu Dec  9 12:51:25 2021 Server UP - localhost:443
127.0.0.1 - - [09/Dec/2021 12:51:49] "POST / HTTP/1.1" 200 -
^C

Thu Dec  9 12:52:11 2021 Server DOWN - localhost:443

```
```Bash
curl -k --data '{"operations":"add","arguments":[1,2]}' --header "Content-Type: application/json" https://localhost    60 ⨯
{
  "Result": 3
}                                                                                                                               
```
Any bad url sent or requested, appropriated error message will be shown. Division by zero has been also taken care of. 
