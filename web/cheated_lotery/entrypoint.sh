FLAG=`cat /app/flag.txt`

echo "mysql_user=btsUs3r" > /app/.env
echo "mysql_pwd=seCR3T_p@ssw0rD" >> /app/.env
echo "mysql_host=127.0.0.1" >> /app/.env
echo "mysql_db=ff86e476b1344851f095759d1eeccda72d9363ad" >> /app/.env

sed -i -e "s/bts{tmpflg}/$FLAG/g" /app/db.sql

mysqld_safe &

echo "Wait for a while"

while ! mysql -e "select NOW(); " 2>/dev/null; do
	sleep 1
done

echo "MYSQL server created. Waiting for databases"

mysql < /app/db.sql
while ! mysql -e "use ff86e476b1344851f095759d1eeccda72d9363ad; select NOW() from coupons;" 2>/dev/null; do
	sleep 1
done

echo "Databases created"

cd /app && gunicorn --bind 0.0.0.0:7331 --workers=2 wsgi:app

