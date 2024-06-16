package org.apache.druid.k8s.overlord.common;

import org.junit.Assert;
import org.junit.Test;


import org.apache.druid.k8s.overlord.common.KubernetesOverlordUtils;
import org.apache.druid.k8s.overlord.common.KubernetesOverlordUtils.*;
import java.util.List;
import java.util.Arrays;

public class KubernetesOverlordUtilsTest_test_stripJobName_avoidDuplicatesWithLongDataSourceName {
    public static String inputTransformation_test_stripJobName_avoidDuplicatesWithLongDataSourceName(String taskId1)  {
        String taskId2 = taskId1.replaceAll("(\\d+)$", String.valueOf(Integer.parseInt("$1") + 1));
        return taskId2;
    }
}