package com.alibaba.druid.bvt.sql.postgresql.issues;

import com.alibaba.druid.bvt.sql.postgresql.issues.Issue5366_test_create_table;

import com.alibaba.druid.bvt.sql.postgresql.issues.Issue5366;
import com.alibaba.druid.bvt.sql.postgresql.issues.Issue5366.*;
import java.util.Map;
import com.alibaba.druid.DbType;
import com.alibaba.druid.sql.SQLUtils;
import com.alibaba.druid.sql.ast.SQLStatement;
import com.alibaba.druid.sql.parser.SQLParserUtils;
import com.alibaba.druid.sql.parser.SQLStatementParser;
import com.alibaba.druid.sql.visitor.SchemaStatVisitor;
import com.alibaba.druid.stat.TableStat;
import org.apache.commons.lang3.StringUtils;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

/**
 * 验证 Postgresql 无法解析 create table PARTITION OF 语句 #5366
 *
 * @author lizongbo
 * @see <a href="https://github.com/alibaba/druid/issues/5366">增强 #5366</a>
 * @see <a href="https://www.postgresql.org/docs/current/sql-createtable.html">CREATE TABLE</a>
 */
public class Issue5366_test_create_table_h4Test2_valid {

    @Test
    public void test_create_table_h4Test2() throws Exception {
        DbType dbType = DbType.postgresql;
    String sql = "CREATE TABLE orders_p4 PARTITION OF orders FOR VALUES WITH (MODULUS 5, REMAINDER 3);";
    String newSql  = Issue5366_test_create_table.inputTransformation_test_create_table(sql);
        System.out.println(dbType + "原始的sql===" + sql);
        String normalizeSql = normalizeSql(sql);
        // SQLStatementParser parser = SQLParserUtils.createSQLStatementParser(sql, dbType);
        // SQLStatement statement = parser.parseStatement();
        // System.out.println(dbType + "生成的sql===" + statement);
        System.out.println("newSql:" + newSql);
        String normalizeNewSql = normalizeSql(newSql);
        assertEquals(normalizeSql.toLowerCase(), normalizeNewSql.toLowerCase());
    // SchemaStatVisitor visitor = SQLUtils.createSchemaStatVisitor(dbType);
    // statement.accept(visitor);
    // System.out.println(dbType + "getTables==" + visitor.getTables());
    // Map<TableStat.Name, TableStat> tableMap = visitor.getTables();
    // assertTrue(!tableMap.isEmpty());
    }

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
}

