package com.alibaba.druid.bvt.sql.mysql.issues;

import com.alibaba.druid.sql.ast.statement.SQLInsertStatement;
import com.alibaba.druid.sql.ast.statement.SQLInsertStatement.*;
import com.alibaba.druid.DbType;
import com.alibaba.druid.sql.SQLUtils;
import com.alibaba.druid.sql.SQLUtils.FormatOption;
import com.alibaba.druid.sql.ast.SQLExpr;
import com.alibaba.druid.sql.ast.SQLStatement;
import com.alibaba.druid.sql.dialect.mysql.ast.statement.MySqlInsertStatement;
import com.alibaba.druid.sql.parser.SQLParserUtils;
import com.alibaba.druid.sql.parser.SQLStatementParser;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * 验证 SQL 解析保持注释和添加注释的功能
 *
 * @author lizongbo
 * @see <a href="https://github.com/alibaba/druid/issues/5686">Issue来源</a>
 */
public class Issue5686_test_column_comment_h3Test1 {

    @Test
    public void test_column_comment_h3Test1() throws Exception {

        System.out.println("原始的sql===" + sql);
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
}

