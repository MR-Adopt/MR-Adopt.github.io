## New input1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
This input is valid because it is the original test case provided. It demonstrates the usage of the `toString()` method to convert a `MySqlInsertStatement` object back to a SQL string.

## New input2:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(0).addAfterComment("-- new comment");
```
This input is valid because it adds a new comment to the first column of the `MySqlInsertStatement` object. The `addAfterComment()` method is used to add a comment after the specified column.

## New input3:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(1).addAfterComment("-- new comment");
```
This input is valid because it adds a new comment to the second column of the `MySqlInsertStatement` object. The `addAfterComment()` method is used to add a comment after the specified column.

## New input4:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(2).addAfterComment("-- new comment");
```
This input is valid because it adds a new comment to the third column of the `MySqlInsertStatement` object. The `addAfterComment()` method is used to add a comment after the specified column.

## New input5:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement.getColumns().get(0).addAfterComment("-- new comment");
    sqlStatement.getColumns().get(1).addAfterComment("-- new comment");
    sqlStatement.getColumns().get(2).addAfterComment("-- new comment");
```
This input is valid because it adds new comments to all three columns of the `MySqlInsertStatement` object. The `addAfterComment()` method is used to add a comment after each specified column.
