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
SOURCE INPUT: `l`
FOLLOW UP INPUT: `l2`,`b`


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


# NEW SOURCE INPUTS
## New source input0:
```java
    long l = 0;
```

## New source input1:
```java
    long l = Long.MAX_VALUE;
```

## New source input2:
```java
    long l = 100000000;
```

## New source input3:
```java
    long l = -1;
```

## New source input4:
```java
    long l = 500000000;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    long l = 1000000000;
    long l2 = 2_250_000_000L;
    boolean b = true;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.