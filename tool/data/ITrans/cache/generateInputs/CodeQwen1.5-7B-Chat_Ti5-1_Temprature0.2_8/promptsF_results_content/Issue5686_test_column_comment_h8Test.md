## New input pair0:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    int ccc = 0;
    for (SQLExpr column : sqlStatement.getColumns()) {
        column.addAfterComment("-- comment注释" + (ccc++));
    }
```
The inferred relation is that the `toString()` method of `MySqlInsertStatement` should produce the same output when called on the same object. The new source input pair satisfies this relation because it adds comments to the columns of the `MySqlInsertStatement` object and then calls the `toString()` method on the modified object. The resulting output should be the same as the output of the original `toString()` method call on the unmodified object.
