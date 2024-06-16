package com.alibaba.druid.bvt.sql.hive.issues;

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


import com.alibaba.druid.bvt.sql.hive.issues.Issue5430;
import com.alibaba.druid.bvt.sql.hive.issues.Issue5430.*;
import java.util.List;
import java.util.Arrays;

public class Issue5430_test_createTable {
    public static String inputTransformation_test_createTable(String sql)  {
        sql = StringUtils.replace(sql, " ( ", "(");
        sql = StringUtils.replace(sql, "( ", "(");
        sql = StringUtils.replace(sql, " )", ")");
        sql = StringUtils.replace(sql, "\t", " ");
        sql = StringUtils.replace(sql, "\n", " ");
        sql = StringUtils.replace(sql, "\'", "\"");
        sql = StringUtils.replace(sql, "  ", " ");
        return sql;
    }
}