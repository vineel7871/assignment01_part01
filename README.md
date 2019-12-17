# assignment01_part01
this github repo is made for completing the given assignment

### step 1
* importing necessary modules
* opening excelfile using pandas.read_excel() returns dictionary of dataframes
* changing column names of dataframe because existing column names are not compatible with mysql

### step 2
* connect() -> creates a connection with mysql database
* create_database_schema() -> creates a database schema from excel sheets
* insert_data() -> insert data from excel sheet into database tables

### database model
```mysql
mysql> use assignment01_part01
Database changed
mysql> show tables
    -> ;
+-------------------------------+
| Tables_in_assignment01_part01 |
+-------------------------------+
| group_listing                 |
| product_listing               |
+-------------------------------+
2 rows in set (0.48 sec)```
```

### group listing sheet

```mysql
mysql> describe group_listing;
+-------------------+--------------+------+-----+---------+----------------+
| Field             | Type         | Null | Key | Default | Extra          |
+-------------------+--------------+------+-----+---------+----------------+
| group_listing_id  | int(11)      | NO   | PRI | NULL    | auto_increment |
| group_name        | varchar(255) | YES  |     | NULL    |                |
| group_description | varchar(255) | YES  |     | NULL    |                |
| isActive          | varchar(255) | YES  |     | NULL    |                |
+-------------------+--------------+------+-----+---------+----------------+
4 rows in set (0.18 sec)
```

```mysql
mysql> select count(*) from group_listing;
+----------+
| count(*) |
+----------+
|       22 |
+----------+
1 row in set (0.05 sec)```
```

```mysql
mysql> select * from group_listing limit 5;
+------------------+------------+-------------------+----------+
| group_listing_id | group_name | group_description | isActive |
+------------------+------------+-------------------+----------+
|                1 | Group 1    | Group Number 1    | yes      |
|                2 | Group 2    | Group Number 2    | yes      |
|                3 | Group 3    | Group Number 3    | yes      |
|                4 | Group 4    | Group Number 4    | yes      |
|                5 | Group 5    | Group Number 5    | yes      |
+------------------+------------+-------------------+----------+
5 rows in set (0.00 sec)```
```

### product listing sheet

```mysql
mysql> describe product_listing;
+--------------------+--------------+------+-----+---------+----------------+
| Field              | Type         | Null | Key | Default | Extra          |
+--------------------+--------------+------+-----+---------+----------------+
| product_listing_id | int(11)      | NO   | PRI | NULL    | auto_increment |
| Product_Name       | varchar(255) | YES  |     | NULL    |                |
| Model_Name         | varchar(255) | YES  |     | NULL    |                |
| Product_Serial_No  | bigint(20)   | YES  |     | NULL    |                |
| Group_Associated   | varchar(255) | YES  |     | NULL    |                |
| product_MRP_rs     | int(11)      | YES  |     | NULL    |                |
+--------------------+--------------+------+-----+---------+----------------+
6 rows in set (0.03 sec)```
```

```mysql
mysql> select count(*) from product_listing;
+----------+
| count(*) |
+----------+
|      110 |
+----------+
1 row in set (0.39 sec)```
```

```mysql
mysql> select * from product_listing limit 5;
+--------------------+----------------+-----------------+-------------------+------------------+----------------+
| product_listing_id | Product_Name   | Model_Name      | Product_Serial_No | Group_Associated | product_MRP_rs |
+--------------------+----------------+-----------------+-------------------+------------------+----------------+
|                  1 | Demo Product 1 | Product Model 1 |    98765987659801 | Group 1          |           1001 |
|                  2 | Demo Product 1 | Product Model 1 |    98765987659802 | Group 2          |           1002 |
|                  3 | Demo Product 1 | Product Model 1 |    98765987659803 | Group 3          |           1003 |
|                  4 | Demo Product 1 | Product Model 1 |    98765987659804 | Group 4          |           1004 |
|                  5 | Demo Product 1 | Product Model 1 |    98765987659805 | Group 5          |           1005 |
+--------------------+----------------+-----------------+-------------------+------------------+----------------+
5 rows in set (0.00 sec)```
```