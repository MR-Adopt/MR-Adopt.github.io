package org.apache.druid.k8s.overlord.common;

import org.junit.Assert;
import org.junit.Test;


import org.apache.druid.k8s.overlord.common.KubernetesOverlordUtils;
import org.apache.druid.k8s.overlord.common.KubernetesOverlordUtils.*;
import java.util.List;
import java.util.Arrays;

public class KubernetesOverlordUtilsTest_test_stripJobName_avoidDuplicatesWithLongDataSourceName {
    public static String inputTransformation_test_stripJobName_avoidDuplicatesWithLongDataSourceName(String taskId1)  {
        // Extract the numeric part from the taskId
        String numericPart = taskId1.replaceAll("[^0-9]", "");
        
        // Increment the numeric part by 1
        int numericValue = Integer.parseInt(numericPart);
        numericValue++;
        String incrementedNumericPart = String.format("%03d", numericValue);
        
        // Replace the numeric part in the follow-up input
        String taskId2 = taskId1.replaceAll("[0-9]+", incrementedNumericPart);
        
        return taskId2;
    }
}