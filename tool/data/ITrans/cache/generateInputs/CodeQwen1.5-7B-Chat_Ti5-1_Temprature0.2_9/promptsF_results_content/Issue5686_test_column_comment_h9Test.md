## New input pair1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(DATE_ID,-- qianzhushi CUS_NO -- houzhushi, CUS_NAME) SELECT A.DATE_ID, A.CUS_NO, A.CUS_NAME FROM TABLE_TEST_2 WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    int ccc = 0;
    for (SQLExpr column : sqlStatement.getColumns()) {
        column.addAfterComment("-- comment注释" + (ccc++));
    }
```

## Explanation:
The inferred relation between the pair of test inputs is that the `MySqlInsertStatement` object `sqlStatement` and `sqlStatement2` should be equal after adding comments to the columns. The new input pair satisfies this relation because it adds comments to the columns of `sqlStatement` and then parses the resulting SQL string back into a `MySqlInsertStatement` object, which is then assigned to `sqlStatement2`. This ensures that the two objects are equal and pass the assertion in the original test case.
