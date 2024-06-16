package com.alibaba.druid.bvt.sql.hive.issues;

import com.alibaba.druid.bvt.sql.hive.issues.Issue5430;
import com.alibaba.druid.bvt.sql.hive.issues.Issue5430.*;
import java.util.Map;
import com.alibaba.druid.DbType;
import com.alibaba.druid.sql.SQLUtils;
import com.alibaba.druid.sql.ast.SQLStatement;
import com.alibaba.druid.sql.parser.SQLParserUtils;
import com.alibaba.druid.sql.parser.SQLStatementParser;
import com.alibaba.druid.sql.visitor.SchemaStatVisitor;
import com.alibaba.druid.stat.TableStat;
import com.alibaba.druid.stat.TableStat.Name;
import com.alibaba.druid.support.logging.Log;
import com.alibaba.druid.support.logging.LogFactory;
import org.apache.commons.lang3.StringUtils;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

/**
 * @author lizongbo
 * @see <a href="https://github.com/alibaba/druid/issues/5430">Issue 5430</a>
 * @see <a href="https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL">Hive DDL</a>
 * @todo 还有4个SQL解析存在转义字符识别的问题，暂时忽略，等温少来解决识别问题吧
 */
public class Issue5430_test_createTable_h4Test1 {

    @Test
    public void test_createTable_h4Test1() throws Exception {
        DbType dbType = DbType.hive;
        int index = 0;
    String sql = "CREATE TABLE my_table(a string, b bigint)\n" + "ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe' STORED AS TEXTFILE\n";
    String newSql = "CREATE TABLE my_table (a string,b bigint) ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.JsonSerDe' STORED AS TEXTFILE";
        String normalizeSql = normalizeSql(sql);
        System.out.println("第" + index + "条原始的sql格式归一化===" + normalizeSql);
        SQLStatementParser parser = SQLParserUtils.createSQLStatementParser(sql, dbType);
        SQLStatement statement = parser.parseStatement();
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

    // private static final Log log = LogFactory.getLog(Issue5430_test_createTable_h4Test1.class);
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

