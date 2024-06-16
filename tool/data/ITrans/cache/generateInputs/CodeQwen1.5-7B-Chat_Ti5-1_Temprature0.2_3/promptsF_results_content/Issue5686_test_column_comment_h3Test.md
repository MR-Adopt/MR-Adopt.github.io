## New input pair1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement2.getColumns().get(0).addAfterComment("-- comment注释0");
    sqlStatement2.getColumns().get(1).addAfterComment("-- comment注释1");
    sqlStatement2.getColumns().get(2).addAfterComment("-- comment注释2");
```

## Explanation:
In the new input pair1, the `sqlStatement` and `sqlStatement2` are the same as the original test case. However, the `sqlStatement2` has been modified by adding comments to the columns of the `MySqlInsertStatement`. The inferred relation is that the comments added to the columns of the `MySqlInsertStatement` should be the same as the comments added to the columns of the original `MySqlInsertStatement`. Therefore, the new input pair1 satisfies this relation.
