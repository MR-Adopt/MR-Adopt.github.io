## New input pair0:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID,-- qianzhushi\n" + "\tCUS_NO -- houzhushi\n,\n" + "\tCUS_NAME\n" + ")\n" + "SELECT A.DATE_ID,\n" + "\tA.CUS_NO,\n" + "\tA.CUS_NAME\n" + "FROM TABLE_TEST_2 \n" + "WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
Inferred relation: The `sqlStatement` and `sqlStatement2` are created by parsing the same SQL string `sql` using `SQLUtils.parseSingleStatement()`. Therefore, they should represent the same SQL statement.

Explanation: The new source input `sql` is the same as the original source input `sql`. The `sqlStatement` and `sqlStatement2` are created by parsing the same SQL string `sql` using `SQLUtils.parseSingleStatement()`. Hence, the new input pair satisfies the inferred relation.

## New input pair1:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "VALUES ('2022-01-01', '123456', 'John Doe');";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
Inferred relation: The `sqlStatement` and `sqlStatement2` are created by parsing the same SQL string `sql` using `SQLUtils.parseSingleStatement()`. Therefore, they should represent the same SQL statement.

Explanation: The new source input `sql` is a simple INSERT statement with VALUES clause. The `sqlStatement` and `sqlStatement2` are created by parsing the same SQL string `sql` using `SQLUtils.parseSingleStatement()`. Hence, the new input pair satisfies the inferred relation.

## New input pair2:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "SELECT DATE_ID, CUS_NO, CUS_NAME FROM TABLE_TEST_2 WHERE COL1='1';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
Inferred relation: The `sqlStatement` and `sqlStatement2` are created by parsing the same SQL string `sql` using `SQLUtils.parseSingleStatement()`. Therefore, they should represent the same SQL statement.

Explanation: The new source input `sql` is an INSERT statement with SELECT clause. The `sqlStatement` and `sqlStatement2` are created by parsing the same SQL string `sql` using `SQLUtils.parseSingleStatement()`. Hence, the new input pair satisfies the inferred relation.

## New input pair3:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "VALUES ('2022-01-01', '123456', 'John Doe'), ('2022-01-02', '789012', 'Jane Smith');";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
Inferred relation: The `sqlStatement` and `sqlStatement2` are created by parsing the same SQL string `sql` using `SQLUtils.parseSingleStatement()`. Therefore, they should represent the same SQL statement.

Explanation: The new source input `sql` is an INSERT statement with multiple rows in the VALUES clause. The `sqlStatement` and `sqlStatement2` are created by parsing the same SQL string `sql` using `SQLUtils.parseSingleStatement()`. Hence, the new input pair satisfies the inferred relation.

## New input pair4:
```java
    String sql = "INSERT INTO TABLE_TEST_1(\n" + "\tDATE_ID, CUS_NO, CUS_NAME\n" + ")\n" + "SELECT DATE_ID, CUS_NO, CUS_NAME FROM TABLE_TEST_2 WHERE COL1='1' UNION SELECT DATE_ID, CUS_NO, CUS_NAME FROM TABLE_TEST_3 WHERE COL2='2';";
    MySqlInsertStatement sqlStatement = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
    MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);
```
Inferred relation: The `sqlStatement` and `sqlStatement2` are created by parsing the same SQL string `sql` using `SQLUtils.parseSingleStatement()`. Therefore, they should represent the same SQL statement.

Explanation: The new source input `sql` is an INSERT statement with UNION in the SELECT clause. The `sqlStatement` and `sqlStatement2` are created by parsing the same SQL string `sql` using `SQLUtils.parseSingleStatement()`. Hence, the new input pair satisfies the inferred relation.