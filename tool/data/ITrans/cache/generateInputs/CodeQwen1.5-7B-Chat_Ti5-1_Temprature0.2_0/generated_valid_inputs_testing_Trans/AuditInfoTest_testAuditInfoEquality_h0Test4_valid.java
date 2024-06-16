/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package org.apache.druid.audit;

import org.apache.druid.audit.AuditInfoTest_testAuditInfoEquality;

import org.apache.druid.audit.AuditInfo;
import org.apache.druid.audit.AuditInfo.*;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.apache.druid.jackson.DefaultObjectMapper;
import org.apache.druid.java.util.common.DateTimes;
import org.junit.Assert;
import org.junit.Test;
import java.io.IOException;

public class AuditInfoTest_testAuditInfoEquality_h0Test4_valid {

    private final ObjectMapper mapper = new DefaultObjectMapper();

    @Test
    public void testAuditInfoEquality_h0Test4() {
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "0.0.0.0");
    AuditInfo auditInfo2  = AuditInfoTest_testAuditInfoEquality.inputTransformation_testAuditInfoEquality(auditInfo1);
        Assert.assertEquals(auditInfo1.hashCode(), auditInfo2.hashCode());
    }
}

