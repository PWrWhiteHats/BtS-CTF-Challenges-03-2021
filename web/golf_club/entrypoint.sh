FLAG=`cat /tmp/f`
sed -i -e "s/FLAGTOBEREPLACED321/$FLAG/g" /db_init.sql

mysqld_safe &

echo "Wait for a while"

while ! mysql -e "select NOW(); " 2>/dev/null; do
	sleep 1
done

echo "MYSQL server created. Waiting for databases"

mysql < /db_init.sql
while ! mysql -e "use test_db; select NOW() from leaderboard;" 2>/dev/null; do
	sleep 1
done

echo "Databases created"

cd /var/www/html && /usr/sbin/apachectl -D FOREGROUND