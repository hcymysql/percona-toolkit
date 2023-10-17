"sql_helper - Automatically determines whether to add an index to the condition field when inputting SQL."

shell> wget https://github.com/hcymysql/sql_helper/archive/refs/heads/sql_helper_1.1.zip
shell> unzip sql_helper_1.1.zip
shell> cd sql_helper_1.1
shell> chmod 755 sql_helper
shell> chmod 755 sql_helper_args

shell> vim test.yaml
host: 192.168.198.239
port: 3336
user: admin
passwd: hechunyang
database: hcy

shell> ./sql_helper -f test.yaml -q "select * from sbtest1 limit 1;"

or

shell> ./sql_helper_args -H 192.168.198.239 -P 6666 -u admin -p hechunyang -d test -q "select * from t1 where cid=11"