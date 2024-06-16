package org.apache.druid.k8s.overlord.common;

import org.junit.Assert;
import org.junit.Test;


import org.apache.druid.k8s.overlord.common.KubernetesOverlordUtils;
import org.apache.druid.k8s.overlord.common.KubernetesOverlordUtils.*;
import java.util.List;
import java.util.Arrays;

public class KubernetesOverlordUtilsTest_test_stripJobName_avoidDuplicatesWithLongDataSourceName {
    public static String inputTransformation_test_stripJobName_avoidDuplicatesWithLongDataSourceName(String taskId1)  {
        int lastUnderscoreIndex = taskId1.lastIndexOf("_");
        String prefix = taskId1.substring(0, lastUnderscoreIndex + 1);
        String numericValue = taskId1.substring(lastUnderscoreIndex + 1);
        int incrementedValue = Integer.parseInt(numericValue) + 1;
        String taskId2 = prefix + incrementedValue + taskId1.substring(lastUnderscoreIndex + numericValue.length() + 1);
        return taskId2;
    }
}