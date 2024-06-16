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

## Code used to generate follow-up input:
```java
int ccc = 0;
for (SQLExpr column : sqlStatement.getColumns()) {
    column.addAfterComment("-- comment注释" + (ccc++));
}
```

## Explanation:
The inferred relation between the source input and the follow-up input is that the `addAfterComment` method is being called on each column in the `sqlStatement` object. This method adds a comment to the column after the column name. The `ccc` variable is used to generate unique comments for each column. The resulting `sqlStatement2` object has the same columns as `sqlStatement` but with comments added to each column.
