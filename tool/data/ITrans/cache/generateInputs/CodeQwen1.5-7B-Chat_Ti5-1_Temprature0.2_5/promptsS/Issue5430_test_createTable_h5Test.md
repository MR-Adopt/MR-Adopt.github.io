# ORIGINAL TEST CASE
```java
@Test
public void test_createTable() throws Exception {
    DbType dbType = DbType.hive;
    int index = 0;
    String sql = "CREATE TABLE my_table(a string, b bigint)\n" + "ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe'\n" + "STORED AS TEXTFILE";
    String normalizeSql = normalizeSql(sql);
    System.out.println("第" + index + "条原始的sql格式归一化===" + normalizeSql);
    SQLStatementParser parser = SQLParserUtils.createSQLStatementParser(sql, dbType);
    SQLStatement statement = parser.parseStatement();
    String newSql = "CREATE TABLE my_table (a string,b bigint) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe' STORED AS TEXTFILE";
    String normalizeNewSql = normalizeSql(newSql);
    System.out.println("第" + index + "条生成的sql格式归一化===" + normalizeNewSql);
    assertEquals(normalizeSql.toLowerCase(), normalizeNewSql.toLowerCase());
    if (!normalizeSql.equalsIgnoreCase(normalizeNewSql)) {
        System.err.println("第" + index + "条是解析失败原始的sql===" + normalizeSql);
    }
    // assertTrue(newSql.equalsIgnoreCase(sql));
    SchemaStatVisitor visitor = SQLUtils.createSchemaStatVisitor(dbType);
    statement.accept(visitor);
    System.out.println("getTables==" + visitor.getTables());
    Map<Name, TableStat> tableMap = visitor.getTables();
// assertFalse(tableMap.isEmpty());
}

```
TEST INPUT: `sql`


# METHOD UNDER TEST
```java
static String normalizeSql(String sql) {
    sql = StringUtils.replace(sql, " ( ", "(");
    sql = StringUtils.replace(sql, "( ", "(");
    sql = StringUtils.replace(sql, " )", ")");
    sql = StringUtils.replace(sql, "\t", " ");
    sql = StringUtils.replace(sql, "\n", " ");
    sql = StringUtils.replace(sql, "\'", "\"");
    sql = StringUtils.replace(sql, " ( ", "(");
    sql = StringUtils.replace(sql, " (", "(");
    sql = StringUtils.replace(sql, "( ", "(");
    sql = StringUtils.replace(sql, " )", ")");
    sql = StringUtils.replace(sql, "( ", "(");
    sql = StringUtils.replace(sql, "  ", " ");
    sql = StringUtils.replace(sql, "  ", " ");
    sql = StringUtils.replace(sql, "  ", " ");
    sql = StringUtils.replace(sql, "  ", " ");
    sql = StringUtils.replace(sql, "( ", "(");
    sql = StringUtils.replace(sql, ", ", ",");
    sql = StringUtils.replace(sql, " ,", ",");
    return sql;
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `sql`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    String sql = "CREATE TABLE my_table(a string, b bigint)\n" + "ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe'\n" + "STORED AS TEXTFILE";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 