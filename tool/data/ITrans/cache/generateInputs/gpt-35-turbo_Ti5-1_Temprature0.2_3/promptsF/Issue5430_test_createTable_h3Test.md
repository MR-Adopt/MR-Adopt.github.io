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
SOURCE INPUT: `sql`
FOLLOW UP INPUT: `newSql`


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


# NEW SOURCE INPUTS
## New source input0:
```java
    String sql = "CREATE TABLE my_table(a string, b bigint)";
```

## New source input1:
```java
    String sql = "CREATE TABLE my_table(a string, b bigint) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe' STORED AS TEXTFILE";
```

## New source input2:
```java
    String sql = "CREATE TABLE my_table(a string, b bigint) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE";
```

## New source input3:
```java
    String sql = "CREATE TABLE my_table(a string, b bigint) PARTITIONED BY (c int) STORED AS PARQUET";
```

## New source input4:
```java
    String sql = "CREATE EXTERNAL TABLE my_table(a string, b bigint) LOCATION '/path/to/data' STORED AS ORC";
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    String sql = "CREATE TABLE my_table(a string, b bigint)\n" + "ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe'\n" + "STORED AS TEXTFILE";
    String newSql = "CREATE TABLE my_table (a string,b bigint) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe' STORED AS TEXTFILE";
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.