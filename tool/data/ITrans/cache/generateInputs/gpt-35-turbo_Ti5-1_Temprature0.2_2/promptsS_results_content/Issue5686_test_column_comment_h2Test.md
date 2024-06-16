## New input1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it creates a valid SQL statement for inserting data into the `TABLE_TEST_1` table by selecting data from the `TABLE_TEST_2` table.

## New input2:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "VALUES ('2021-01-01', '123', 'John');";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it creates a valid SQL statement for inserting a single row of data into the `TABLE_TEST_1` table with specific values for the columns `DATE_ID`, `CUS_NO`, and `CUS_NAME`.

## New input3:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "SELECT DATE_ID, CUS_NO, CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it creates a valid SQL statement for inserting data into the `TABLE_TEST_1` table by selecting data from the `TABLE_TEST_2` table without any column comments.

## New input4:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "VALUES ('2021-01-01', '123', 'John'), ('2021-01-02', '456', 'Jane');";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it creates a valid SQL statement for inserting multiple rows of data into the `TABLE_TEST_1` table with specific values for the columns `DATE_ID`, `CUS_NO`, and `CUS_NAME`.

## New input5:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "SELECT DATE_ID, CUS_NO, CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1'\n" + "LIMIT 10;";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it creates a valid SQL statement for inserting data into the `TABLE_TEST_1` table by selecting data from the `TABLE_TEST_2` table with a limit of 10 rows.