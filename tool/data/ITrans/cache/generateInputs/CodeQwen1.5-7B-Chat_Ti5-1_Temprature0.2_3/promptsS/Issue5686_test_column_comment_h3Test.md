# ORIGINAL TEST CASE
```java
@Test
public void test_column_comment() throws Exception {
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    System.out.println("原始的sql===" + sql);
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    int ccc = 0;
    for (SQLExpr column : sqlStatement.getColumns()) {
        column.addAfterComment("-- comment注释" + (ccc++));
    }
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    int ccc2 = 0;
    for (SQLExpr column : sqlStatement2.getColumns()) {
        column.addAfterComment("-- comment注释" + (ccc2++));
    }
    System.out.println("MARK sqlStatement:" + sqlStatement);
    String newSql = sqlStatement.toString();
    System.out.println("首次解析后生成的sql===" + newSql);
    MySqlInsertStatement sqlStatementNew = (MySqlInsertStatement) SQLUtils.parseSingleStatement(newSql, DbType.mysql, true);
    String newSql2 = sqlStatement2.toString();
    System.out.println("再次解析后生成的sql===" + newSql2);
    assertEquals(newSql, newSql2);
}

```
TEST INPUT: `sqlStatement`


# METHOD UNDER TEST
```java
public String toString() {
    return SQLUtils.toSQLString(this, dbType);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `sqlStatement`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 