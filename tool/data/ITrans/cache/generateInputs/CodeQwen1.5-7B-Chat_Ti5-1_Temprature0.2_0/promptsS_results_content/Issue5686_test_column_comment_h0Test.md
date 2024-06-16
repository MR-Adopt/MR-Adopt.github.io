## New input1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(0).addAfterComment("-- new comment for DATE_ID");
```
Explanation: This input adds a new comment after the `DATE_ID` column in the SQL statement. This is a valid input because it does not violate the original SQL syntax and does not change the functionality of the SQL statement.

## New input2:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(1).addAfterComment("-- new comment for CUS_NO");
```
Explanation: This input adds a new comment after the `CUS_NO` column in the SQL statement. This is a valid input because it does not violate the original SQL syntax and does not change the functionality of the SQL statement.

## New input3:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(2).addAfterComment("-- new comment for CUS_NAME");
```
Explanation: This input adds a new comment after the `CUS_NAME` column in the SQL statement. This is a valid input because it does not violate the original SQL syntax and does not change the functionality of the SQL statement.

## New input4:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(0).addAfterComment("-- new comment for DATE_ID");
    sqlStatement.getColumns().get(1).addAfterComment("-- new comment for CUS_NO");
    sqlStatement.getColumns().get(2).addAfterComment("-- new comment for CUS_NAME");
```
Explanation: This input adds new comments after all three columns in the SQL statement. This is a valid input because it does not violate the original SQL syntax and does not change the functionality of the SQL statement.

## New input5:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(0).addAfterComment("-- new comment for DATE_ID");
    sqlStatement.getColumns().get(1).addAfterComment("-- new comment for CUS_NO");
    sqlStatement.getColumns().get(2).addAfterComment("-- new comment for CUS_NAME");
    sqlStatement.getColumns().get(0).addAfterComment("-- duplicate comment for DATE_ID");
    sqlStatement.getColumns().get(1).addAfterComment("-- duplicate comment for CUS_NO");
    sqlStatement.getColumns().get(2).addAfterComment("-- duplicate comment for CUS_NAME");
```
Explanation: This input adds duplicate comments after all three columns in the SQL statement. This is a valid input because it does not violate the original SQL syntax and does not change the functionality of the SQL statement.
