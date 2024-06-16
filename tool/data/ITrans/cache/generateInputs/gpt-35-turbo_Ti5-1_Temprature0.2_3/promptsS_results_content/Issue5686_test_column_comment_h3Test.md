## New input1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it constructs a valid SQL statement with a table name, column names, and a SELECT statement.

## New input2:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "VALUES ('2022-01-01', '12345', 'John Doe');";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it constructs a valid SQL statement with a table name, column names, and a VALUES clause to insert specific values into the table.

## New input3:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "SELECT DATE_ID, CUS_NO, CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it constructs a valid SQL statement with a table name, column names, and a SELECT statement without any comments.

## New input4:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "VALUES (1, 12345, 'John Doe');";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it constructs a valid SQL statement with a table name, column names, and a VALUES clause to insert specific values into the table.

## New input5:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "SELECT DATE_ID, CUS_NO, CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1' LIMIT 10;";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it constructs a valid SQL statement with a table name, column names, a SELECT statement, and a LIMIT clause to limit the number of rows inserted into the table.