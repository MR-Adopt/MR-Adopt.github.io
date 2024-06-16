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
package org.apache.druid.k8s.overlord.common;

import org.apache.druid.k8s.overlord.common.KubernetesOverlordUtils;
import org.apache.druid.k8s.overlord.common.KubernetesOverlordUtils.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.junit.Assert;
import org.junit.Test;

public class KubernetesOverlordUtilsTest_test_stripJobName_avoidDuplicatesWithLongDataSourceName_h1Test4 {

    @Test
    public void test_stripJobName_avoidDuplicatesWithLongDataSourceName_h1Test4() {
    String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z_with_null_taskId";
    String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_117_pcgkebcl_2023-07-19T16:53:11.416Z_with_null_taskId";
        String jobName1 = KubernetesOverlordUtils.convertTaskIdToJobName(taskId1);
        String jobName2 = KubernetesOverlordUtils.convertTaskIdToJobName(taskId2);
        Assert.assertNotEquals(jobName1, jobName2);
    }
}

