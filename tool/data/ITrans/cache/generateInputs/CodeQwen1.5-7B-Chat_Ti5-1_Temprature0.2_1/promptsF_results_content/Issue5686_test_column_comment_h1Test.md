# New input pair1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement2.getColumns().get(0).addAfterComment("-- comment注释0");
    sqlStatement2.getColumns().get(1).addAfterComment("-- comment注释1");
    sqlStatement2.getColumns().get(2).addAfterComment("-- comment注释2");
```

## Explanation:
The inferred relation is that the `toString()` method of the `MySqlInsertStatement` class should produce the same output when called with the same object. In this new input pair, we are adding comments to the columns of the `MySqlInsertStatement` object `sqlStatement2` and then calling the `toString()` method to generate the SQL string. Since the comments are added to the same columns as in `sqlStatement`, the output of `toString()` should remain the same. Therefore, this new input pair satisfies the inferred relation.

# New input pair2:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    sqlStatement2.getColumns().get(0).addAfterComment("-- comment注释0");
    sqlStatement2.getColumns().get(1).addAfterComment("-- comment注释1");
    sqlStatement2.getColumns().get(2).addAfterComment("-- comment注释2");
    sqlStatement2.getColumns().get(0).addAfterComment("-- comment注释3");
    sqlStatement2.getColumns().get(1).addAfterComment("-- comment注释4");
    sqlStatement2.getColumns().get(2).addAfterComment("-- comment注释5");
```

## Explanation:
In this new input pair, we are adding more comments to the columns of the `MySqlInsertStatement` object `sqlStatement2` than in the previous input pair. However, the output of `toString()` should remain the same as before, since the comments are added to the same columns as in `sqlStatement`. Therefore, this new input pair satisfies the inferred relation.
