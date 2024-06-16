# New input pair1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    int ccc = 0;
    for (SQLExpr column : sqlStatement.getColumns()) {
        column.addAfterComment("-- comment注释" + (ccc++));
    }
```

Explanation:
The new input pair1 satisfies the inferred relation by adding comments to the columns of the `sqlStatement` object. The `addAfterComment` method is used to add comments to each column in the `sqlStatement` object. The comments are added in the same order as the columns, and each comment is unique. This ensures that the comments added to the `sqlStatement` object are different from those added to the `sqlStatement2` object. The `assertEquals` method is used to compare the `newSql` and `newSql2` strings, which should be equal if the comments have been added correctly.
