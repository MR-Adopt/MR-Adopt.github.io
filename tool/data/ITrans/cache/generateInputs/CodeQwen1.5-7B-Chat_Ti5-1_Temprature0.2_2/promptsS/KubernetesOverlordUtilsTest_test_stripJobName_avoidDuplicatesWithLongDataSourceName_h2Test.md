# ORIGINAL TEST CASE
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
TEST INPUT: `taskId1`


# METHOD UNDER TEST
```java
public static String convertTaskIdToJobName(String taskId) {
    return taskId == null ? "" : StringUtils.left(RegExUtils.replaceAll(taskId, K8S_TASK_ID_PATTERN, "").toLowerCase(Locale.ENGLISH), 30) + "-" + Hashing.murmur3_128().hashString(taskId, StandardCharsets.UTF_8);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `taskId1`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    String taskId1 = "coordinator-issued_compact_1234_telemetry_wikipedia_geteditfailuresinnorthamerica_agg_summ_116_pcgkebcl_2023-07-19T16:53:11.416Z";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 