# ORIGINAL TEST CASE
```java
@Test
public void test_create_table() throws Exception {
    DbType dbType = DbType.postgresql;
    String sql = "CREATE TABLE orders_p4 PARTITION OF orders\n" + "    FOR VALUES WITH (MODULUS 4, REMAINDER 3);";
    System.out.println(dbType + "原始的sql===" + sql);
    String normalizeSql = normalizeSql(sql);
    // SQLStatementParser parser = SQLParserUtils.createSQLStatementParser(sql, dbType);
    // SQLStatement statement = parser.parseStatement();
    // System.out.println(dbType + "生成的sql===" + statement);
    String newSql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 4 , REMAINDER 3);";
    System.out.println("newSql:" + newSql);
    String normalizeNewSql = normalizeSql(newSql);
    assertEquals(normalizeSql.toLowerCase(), normalizeNewSql.toLowerCase());
// SchemaStatVisitor visitor = SQLUtils.createSchemaStatVisitor(dbType);
// statement.accept(visitor);
// System.out.println(dbType + "getTables==" + visitor.getTables());
// Map<TableStat.Name, TableStat> tableMap = visitor.getTables();
// assertTrue(!tableMap.isEmpty());
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
    String sql = "CREATE TABLE orders_p4 PARTITION OF orders\n" + "    FOR VALUES WITH (MODULUS 4, REMAINDER 3);";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 