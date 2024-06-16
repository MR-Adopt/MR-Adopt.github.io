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
SOURCE INPUT: `sql`
FOLLOW UP INPUT: `newSql`


# OTHER INPUT PAIRS 
## Input pair1:
```java
String sql = "CREATE TABLE orders_p4 PARTITION OF orders\n" + "    FOR VALUES WITH (MODULUS 4, REMAINDER 3);";
String newSql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 4 , REMAINDER 3);";
```

## Input pair2:
```java
String sql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 4, REMAINDER 3);";
String newSql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 4 , REMAINDER 3);";
```

## Input pair3:
```java
String sql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 4, REMAINDER 2);";
String newSql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 4 , REMAINDER 2);";
```

## Input pair4:
```java
String sql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 8, REMAINDER 3);";
String newSql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 8 , REMAINDER 3);";
```

## Input pair5:
```java
String sql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 4, REMAINDER 0);";
String newSql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 4 , REMAINDER 0);";
```

## Input pair6:
```java
String sql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 2, REMAINDER 1);";
String newSql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 2 , REMAINDER 1);";
```

## Input pair7:
```java
String sql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 8, REMAINDER 7);";
String newSql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 8 , REMAINDER 7);";
```

## Input pair8:
```java
String sql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 1, REMAINDER 0);";
String newSql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 1 , REMAINDER 0);";
```

## Input pair9:
```java
String sql = "CREATE TABLE orders_p5 PARTITION OF orders\n" + "    FOR VALUES WITH (MODULUS 5, REMAINDER 4);";
String newSql = "CREATE TABLE orders_p5 PARTITION OF orders FOR VALUES WITH (MODULUS 5 , REMAINDER 4);";
```

## Input pair10:
```java
String sql = "CREATE TABLE orders_p6 PARTITION OF orders\n" + "    FOR VALUES WITH (MODULUS 6, REMAINDER 2);";
String newSql = "CREATE TABLE orders_p6 PARTITION OF orders FOR VALUES WITH (MODULUS 6 , REMAINDER 2);";
```

## Input pair11:
```java
String sql = "CREATE TABLE orders_p7 PARTITION OF orders\n" + "    FOR VALUES WITH (MODULUS 7, REMAINDER 5);";
String newSql = "CREATE TABLE orders_p7 PARTITION OF orders FOR VALUES WITH (MODULUS 7 , REMAINDER 5);";
```

## Input pair12:
```java
String sql = "CREATE TABLE orders_p8 PARTITION OF orders\n" + "    FOR VALUES WITH (MODULUS 8, REMAINDER 6);";
String newSql = "CREATE TABLE orders_p8 PARTITION OF orders FOR VALUES WITH (MODULUS 8 , REMAINDER 6);";
```

## Input pair13:
```java
String sql = "CREATE TABLE orders_p9 PARTITION OF orders\n" + "    FOR VALUES WITH (MODULUS 9, REMAINDER 1);";
String newSql = "CREATE TABLE orders_p9 PARTITION OF orders FOR VALUES WITH (MODULUS 9 , REMAINDER 1);";
```

## Input pair14:
```java
String sql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 5, REMAINDER 3);";
String newSql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 5 , REMAINDER 3);";
```



# OUTPUT FORMAT
```java
public class Issue5366_test_create_table {
    public static String inputTransformation_test_create_table(String sql)  {
        // TODO
        String newSql = 
		return newSql;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.