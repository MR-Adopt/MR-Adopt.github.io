## New input1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it is the same as the original test case and represents a valid SQL statement.

## New input2:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "VALUES ('2022-01-01', '123456', 'John Doe');";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it represents a valid SQL statement for inserting values into the `TABLE_TEST_1` table.

## New input3:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "SELECT DATE_ID, CUS_NO, CUS_NAME FROM TABLE_TEST_2 WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it represents a valid SQL statement for inserting values into the `TABLE_TEST_1` table by selecting values from the `TABLE_TEST_2` table.

## New input4:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "VALUES ('2022-01-01', '123456', 'John Doe'), ('2022-01-02', '789012', 'Jane Smith');";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it represents a valid SQL statement for inserting multiple sets of values into the `TABLE_TEST_1` table.

## New input5:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "SELECT DATE_ID, CUS_NO, CUS_NAME FROM TABLE_TEST_2 WHERE COL1='1' UNION SELECT DATE_ID, CUS_NO, CUS_NAME FROM TABLE_TEST_3 WHERE COL2='2';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it represents a valid SQL statement for inserting values into the `TABLE_TEST_1` table by combining the results of two SELECT statements using the UNION operator.