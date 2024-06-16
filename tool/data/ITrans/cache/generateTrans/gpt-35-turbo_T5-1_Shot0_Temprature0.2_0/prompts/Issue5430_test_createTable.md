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


# TEST CASE
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


# OTHER INPUT PAIRS 
## Input pair1:
```java
String sql = "CREATE TABLE my_table(a string, b bigint)\n" + "ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe'\n" + "STORED AS TEXTFILE";
String newSql = "CREATE TABLE my_table (a string,b bigint) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe' STORED AS TEXTFILE";
```

## Input pair2:
```java
String sql = "CREATE TABLE my_table(a string, b bigint)";
String newSql = "CREATE TABLE my_table(a string,b bigint)";
```

## Input pair3:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) STORED AS PARQUET";
String newSql = "CREATE TABLE my_table(a string,b bigint) STORED AS PARQUET";
```

## Input pair4:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) PARTITIONED BY (c int)";
String newSql = "CREATE TABLE my_table(a string,b bigint) PARTITIONED BY (c int)";
```

## Input pair5:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) ROW FORMAT DELIMITED FIELDS TERMINATED BY ','";
String newSql = "CREATE TABLE my_table(a string,b bigint) ROW FORMAT DELIMITED FIELDS TERMINATED BY ','";
```

## Input pair6:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) LOCATION '/path/to/table'";
String newSql = "CREATE TABLE my_table(a string,b bigint) LOCATION '/path/to/table'";
```

## Input pair7:
```java
String sql = "CREATE TABLE my_table(a string, b bigint, c double)\n" + "ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe'\n" + "STORED AS TEXTFILE";
String newSql = "CREATE TABLE my_table (a string,b bigint,c double) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe' STORED AS TEXTFILE";
```

## Input pair8:
```java
String sql = "CREATE TABLE my_table(a string)\n" + "ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe'\n" + "STORED AS TEXTFILE";
String newSql = "CREATE TABLE my_table (a string) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe' STORED AS TEXTFILE";
```

## Input pair9:
```java
String sql = "CREATE TABLE my_table(a string, b bigint)\n" + "ROW FORMAT DELIMITED FIELDS TERMINATED BY ','\n" + "STORED AS TEXTFILE";
String newSql = "CREATE TABLE my_table (a string,b bigint) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE";
```

## Input pair10:
```java
String sql = "CREATE TABLE my_table(a string, b bigint)\n" + "ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'\n" + "STORED AS TEXTFILE";
String newSql = "CREATE TABLE my_table (a string,b bigint) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe' STORED AS TEXTFILE";
```

## Input pair11:
```java
String sql = "CREATE TABLE my_table(a string, b bigint)";
String newSql = "CREATE TABLE my_table (a string,b bigint)";
```

## Input pair12:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe' STORED AS TEXTFILE";
String newSql = "CREATE TABLE my_table (a string,b bigint) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe' STORED AS TEXTFILE";
```

## Input pair13:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE";
String newSql = "CREATE TABLE my_table (a string,b bigint) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE";
```

## Input pair14:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) STORED AS PARQUET";
String newSql = "CREATE TABLE my_table (a string,b bigint) STORED AS PARQUET";
```

## Input pair15:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) LOCATION '/path/to/table'";
String newSql = "CREATE TABLE my_table (a string,b bigint) LOCATION '/path/to/table'";
```

## Input pair16:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) PARTITIONED BY (c int) STORED AS PARQUET";
String newSql = "CREATE TABLE my_table (a string,b bigint) PARTITIONED BY (c int) STORED AS PARQUET";
```

## Input pair17:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe'";
String newSql = "CREATE TABLE my_table (a string,b bigint) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe'";
```

## Input pair18:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) STORED AS TEXTFILE";
String newSql = "CREATE TABLE my_table (a string,b bigint) STORED AS TEXTFILE";
```

## Input pair19:
```java
String sql = "CREATE TABLE my_table(a string, b bigint) COMMENT 'This is a table'";
String newSql = "CREATE TABLE my_table (a string,b bigint) COMMENT 'This is a table'";
```



# OUTPUT FORMAT
```java
public class Issue5430_test_createTable {
    public static String inputTransformation_test_createTable(String sql)  {
        // TODO
        String newSql = 
		return newSql;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.