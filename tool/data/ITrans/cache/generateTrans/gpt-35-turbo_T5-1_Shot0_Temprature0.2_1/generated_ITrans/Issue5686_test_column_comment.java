package com.alibaba.druid.bvt.sql.mysql.issues;

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


import com.alibaba.druid.sql.ast.statement.SQLInsertStatement;
import com.alibaba.druid.sql.ast.statement.SQLInsertStatement.*;
import java.util.List;
import java.util.Arrays;

public class Issue5686_test_column_comment {
    public static MySqlInsertStatement inputTransformation_test_column_comment(MySqlInsertStatement sqlStatement) {
        MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) sqlStatement.clone();
        int ccc = 0;
        for (SQLExpr column : sqlStatement2.getColumns()) {
            column.addAfterComment("-- comment注释" + (ccc++));
        }
        return sqlStatement2;
    }
}