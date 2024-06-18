package com.alibaba.druid.bvt.sql.postgresql.issues;

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


import com.alibaba.druid.bvt.sql.postgresql.issues.Issue5366;
import com.alibaba.druid.bvt.sql.postgresql.issues.Issue5366.*;
import java.util.List;
import java.util.Arrays;

public class Issue5366_test_create_table {
    public static String inputTransformation_test_create_table(String sql)  {
        // Remove unnecessary spaces
        sql = sql.replaceAll("\\s+", " ");
        
        // Align comma (',')
        sql = sql.replaceAll(",\\s*", ", ");
        
        // Align opening and closing parentheses ('(', ')')
        sql = sql.replaceAll("\\(\\s*", "(");
        sql = sql.replaceAll("\\s*\\)", ")");
        
        return sql;
    }
}