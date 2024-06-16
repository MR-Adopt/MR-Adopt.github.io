## New input1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it constructs a valid SQL statement for inserting data into the `TABLE_TEST_1` table by selecting data from the `TABLE_TEST_2` table.

## New input2:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "VALUES (1, 'John Doe', '1234567890');";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it constructs a valid SQL statement for inserting data into the `TABLE_TEST_1` table by specifying the values directly.

## New input3:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT DATE_ID, CUS_NO, CUS_NAME FROM TABLE_TEST_2 WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it constructs a valid SQL statement for inserting data into the `TABLE_TEST_1` table by selecting data from the `TABLE_TEST_2` table based on a condition.

## New input4:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "VALUES (1, 'John Doe', '1234567890'), (2, 'Jane Smith', '0987654321');";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it constructs a valid SQL statement for inserting multiple rows of data into the `TABLE_TEST_1` table by specifying the values for each row.

## New input5:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "SELECT DATE_ID, CUS_NO, CUS_NAME FROM TABLE_TEST_2 WHERE COL1='1' UNION SELECT DATE_ID, CUS_NO, CUS_NAME FROM TABLE_TEST_3 WHERE COL2='2';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it constructs a valid SQL statement for inserting data into the `TABLE_TEST_1` table by combining the results of two SELECT statements using the UNION operator.