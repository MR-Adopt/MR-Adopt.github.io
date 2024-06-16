## New input1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(0).addAfterComment("-- New comment for DATE_ID");
```
Explanation: This input adds a new comment to the first column of the SQL statement. The new comment is "-- New comment for DATE_ID". This ensures that the SQL statement remains valid and can be parsed correctly.

## New input2:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(1).addAfterComment("-- New comment for CUS_NO");
```
Explanation: This input adds a new comment to the second column of the SQL statement. The new comment is "-- New comment for CUS_NO". This ensures that the SQL statement remains valid and can be parsed correctly.

## New input3:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(2).addAfterComment("-- New comment for CUS_NAME");
```
Explanation: This input adds a new comment to the third column of the SQL statement. The new comment is "-- New comment for CUS_NAME". This ensures that the SQL statement remains valid and can be parsed correctly.

## New input4:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(0).addAfterComment("-- New comment for DATE_ID");
    sqlStatement.getColumns().get(1).addAfterComment("-- New comment for CUS_NO");
    sqlStatement.getColumns().get(2).addAfterComment("-- New comment for CUS_NAME");
```
Explanation: This input adds new comments to all three columns of the SQL statement. The new comments are "-- New comment for DATE_ID", "-- New comment for CUS_NO", and "-- New comment for CUS_NAME". This ensures that the SQL statement remains valid and can be parsed correctly.

## New input5:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(0).addAfterComment("-- New comment for DATE_ID");
    sqlStatement.getColumns().get(2).addAfterComment("-- New comment for CUS_NAME");
```
Explanation: This input adds new comments to the first and third columns of the SQL statement. The new comments are "-- New comment for DATE_ID" and "-- New comment for CUS_NAME". This ensures that the SQL statement remains valid and can be parsed correctly.
