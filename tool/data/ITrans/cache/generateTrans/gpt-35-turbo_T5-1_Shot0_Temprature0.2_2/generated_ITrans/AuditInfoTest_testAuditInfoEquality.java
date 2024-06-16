package org.apache.druid.audit;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.druid.jackson.DefaultObjectMapper;
import org.apache.druid.java.util.common.DateTimes;
import org.junit.Assert;
import org.junit.Test;
import java.io.IOException;


import org.apache.druid.audit.AuditInfo;
import org.apache.druid.audit.AuditInfo.*;
import java.util.List;
import java.util.Arrays;

public class AuditInfoTest_testAuditInfoEquality {
    public static AuditInfo inputTransformation_testAuditInfoEquality(AuditInfo auditInfo1)  {
        AuditInfo auditInfo2 = new AuditInfo(auditInfo1.getAuthor(), auditInfo1.getIdentity(), auditInfo1.getComment(), auditInfo1.getIp());
        return auditInfo2;
    }
}