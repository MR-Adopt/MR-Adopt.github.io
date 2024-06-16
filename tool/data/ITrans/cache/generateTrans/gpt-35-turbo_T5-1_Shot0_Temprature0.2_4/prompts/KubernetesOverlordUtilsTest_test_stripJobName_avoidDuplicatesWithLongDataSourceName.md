# METHOD UNDER TEST
```java
public static String convertTaskIdToJobName(String taskId) {
    return taskId == null ? "" : StringUtils.left(RegExUtils.replaceAll(taskId, K8S_TASK_ID_PATTERN, "").toLowerCase(Locale.ENGLISH), 30) + "-" + Hashing.murmur3_128().hashString(taskId, StandardCharsets.UTF_8);
}

```


# TEST CASE
```java
@Test
public void test_stripJobName_avoidDuplicatesWithLongDataSourceName() {
    String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z";
    String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_117_pcgkebcl_2023-07-19T16:53:11.416Z";
    String jobName1 = KubernetesOverlordUtils.convertTaskIdToJobName(taskId1);
    String jobName2 = KubernetesOverlordUtils.convertTaskIdToJobName(taskId2);
    Assert.assertNotEquals(jobName1, jobName2);
}

```
SOURCE INPUT: `taskId1`
FOLLOW UP INPUT: `taskId2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z";
String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_117_pcgkebcl_2023-07-19T16:53:11.416Z";
```

## Input pair2:
```java
String taskId1 = "coordinator-issued_compact_5678_telemetry_wikipedia_geteditfailuresinsouthamerica_agg_summ_118_pcgkebcl_2023-07-19T16:53:11.416Z";
String taskId2 = "coordinator-issued_compact_5678_telemetry_wikipedia_geteditfailuresinsouthamerica_agg_summ_119_pcgkebcl_2023-07-19T16:53:11.416Z";
```

## Input pair3:
```java
String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z_extra";
String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_117_pcgkebcl_2023-07-19T16:53:11.416Z_extra";
```

## Input pair4:
```java
String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z_";
String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_117_pcgkebcl_2023-07-19T16:53:11.416Z_";
```

## Input pair5:
```java
String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z_123";
String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_117_pcgkebcl_2023-07-19T16:53:11.416Z_123";
```

## Input pair6:
```java
String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z_extra";
String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z_extra2";
```

## Input pair7:
```java
String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_118_pcgkebcl_2023-07-19T16:53:11.416Z";
String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_117_pcgkebcl_2023-07-19T16:53:11.416Z";
```

## Input pair8:
```java
String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.417Z";
String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z";
```

## Input pair9:
```java
String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:12.416Z";
String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z";
```

## Input pair10:
```java
String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:54:11.416Z";
String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z";
```

## Input pair11:
```java
String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T17:53:11.416Z";
String taskId2 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z";
```



# OUTPUT FORMAT
```java
public class KubernetesOverlordUtilsTest_test_stripJobName_avoidDuplicatesWithLongDataSourceName {
    public static String inputTransformation_test_stripJobName_avoidDuplicatesWithLongDataSourceName(String taskId1)  {
        // TODO
        String taskId2 = 
		return taskId2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.