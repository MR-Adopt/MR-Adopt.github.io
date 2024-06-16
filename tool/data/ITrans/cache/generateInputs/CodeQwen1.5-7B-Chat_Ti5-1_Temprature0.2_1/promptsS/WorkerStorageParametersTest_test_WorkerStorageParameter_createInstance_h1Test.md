# ORIGINAL TEST CASE
```java
@Test
public void test_WorkerStorageParameter_createInstance() {
    long l = 1000000000;
    long l2 = 2_250_000_000L;
    boolean b = true;
    Assert.assertEquals(WorkerStorageParameters.createInstanceForTests(l), WorkerStorageParameters.createInstance(l2, b));
}

```
TEST INPUT: `l`


# METHOD UNDER TEST
```java
@VisibleForTesting
public static WorkerStorageParameters createInstanceForTests(final long tmpStorageBytesPerTask) {
    return new WorkerStorageParameters(tmpStorageBytesPerTask);
}

/**
 * Returns an object specifiying temporary disk-usage parameters
 * @param tmpStorageBytesPerTask                  amount of disk space to be allocated per task for intermediate files.
 * @param isIntermediateSuperSorterStorageEnabled whether intermediate super sorter storage is enabled
 */
public static WorkerStorageParameters createInstance(final long tmpStorageBytesPerTask, final boolean isIntermediateSuperSorterStorageEnabled) {
    if (!isIntermediateSuperSorterStorageEnabled || tmpStorageBytesPerTask == -1) {
        return new WorkerStorageParameters(-1);
    }
    Preconditions.checkArgument(tmpStorageBytesPerTask > 0, "Temporary storage bytes passed: [%s] should be > 0", tmpStorageBytesPerTask);
    long intermediateSuperSorterStorageMaxLocalBytes = computeUsableStorage(tmpStorageBytesPerTask);
    log.info("Intermediate super sorter local storage size: %d bytes", intermediateSuperSorterStorageMaxLocalBytes);
    if (intermediateSuperSorterStorageMaxLocalBytes < MINIMUM_SUPER_SORTER_TMP_STORAGE_BYTES) {
        throw new MSQException(new NotEnoughTemporaryStorageFault(calculateSuggestedMinTemporaryStorage(), tmpStorageBytesPerTask));
    }
    return new WorkerStorageParameters(intermediateSuperSorterStorageMaxLocalBytes);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `l`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    long l = 1000000000;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 