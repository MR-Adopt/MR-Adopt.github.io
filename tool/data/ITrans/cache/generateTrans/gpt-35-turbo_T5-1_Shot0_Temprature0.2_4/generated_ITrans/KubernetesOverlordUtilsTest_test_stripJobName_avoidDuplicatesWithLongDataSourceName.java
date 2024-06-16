package org.apache.druid.k8s.overlord.common;

import org.junit.Assert;
import org.junit.Test;


import org.apache.druid.k8s.overlord.common.KubernetesOverlordUtils;
import org.apache.druid.k8s.overlord.common.KubernetesOverlordUtils.*;
import java.util.List;
import java.util.Arrays;

public class KubernetesOverlordUtilsTest_test_stripJobName_avoidDuplicatesWithLongDataSourceName {
    public static String inputTransformation_test_stripJobName_avoidDuplicatesWithLongDataSourceName(String taskId1)  {
        // Extract the last digit from taskId1
        int lastDigit = Character.getNumericValue(taskId1.charAt(taskId1.length() - 1));
        
        // Increment the last digit by 1
        int incrementedDigit = lastDigit + 1;
        
        // Replace the last digit in taskId1 with the incremented digit
        String taskId2 = taskId1.substring(0, taskId1.length() - 1) + incrementedDigit;
        
        return taskId2;
    }
}