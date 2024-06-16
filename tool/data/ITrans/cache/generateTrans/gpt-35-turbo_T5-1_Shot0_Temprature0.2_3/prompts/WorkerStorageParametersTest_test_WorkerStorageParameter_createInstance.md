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


# TEST CASE
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


# OTHER INPUT PAIRS 



# OUTPUT FORMAT
```java
public class WorkerStorageParametersTest_test_WorkerStorageParameter_createInstance {
    public static List<Object> inputTransformation_test_WorkerStorageParameter_createInstance(long l)  {
        // TODO
        long l2 = 
		boolean b = 
		List<Object> transformed_inputs = Arrays.asList(l2, b);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.