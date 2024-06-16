# METHOD UNDER TEST
```java
// It's okay to store clients in a map here because all the configs for specifying azure retries are static, and there are only 2 of them.
// The 2 configs are AzureAccountConfig.maxTries and AzureOutputConfig.maxRetry.
// We will only ever have at most 2 clients in cachedBlobServiceClients per storage account.
public BlobServiceClient getBlobServiceClient(@Nullable Integer retryCount, String storageAccount) {
    return cachedBlobServiceClients.computeIfAbsent(Pair.of(storageAccount, retryCount != null ? retryCount : config.getMaxTries()), key -> buildNewClient(key.rhs, key.lhs));
}

```


# TEST CASE
```java
@Test
public void test_blobServiceClientBuilder_useNewClientForDifferentRetryCount() {
    Integer retryCount1 = null;
    String ACCOUNT1 = "account";
    Integer retryCount2 = 1;
    String ACCOUNT2 = "account";
    AzureAccountConfig config = new AzureAccountConfig();
    config.setUseAzureCredentialsChain(true);
    azureClientFactory = new AzureClientFactory(config);
    BlobServiceClient blobServiceClient = azureClientFactory.getBlobServiceClient(retryCount1, ACCOUNT1);
    BlobServiceClient blobServiceClient2 = azureClientFactory.getBlobServiceClient(retryCount2, ACCOUNT2);
    Assert.assertNotEquals(blobServiceClient, blobServiceClient2);
}

```
SOURCE INPUT: `retryCount1`,`ACCOUNT1`
FOLLOW UP INPUT: `retryCount2`,`ACCOUNT2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
Integer retryCount1 = null;
String ACCOUNT1 = "account";
Integer retryCount2 = 1;
String ACCOUNT2 = "account";
```

## Input pair2:
```java
Integer retryCount1 = 0;
String ACCOUNT1 = "account";
Integer retryCount2 = 1;
String ACCOUNT2 = "account";
```

## Input pair3:
```java
Integer retryCount1 = 3;
String ACCOUNT1 = "account";
Integer retryCount2 = 4;
String ACCOUNT2 = "account";
```

## Input pair4:
```java
Integer retryCount1 = 3;
String ACCOUNT1 = "account";
Integer retryCount2 = 1;
String ACCOUNT2 = "account";
```

## Input pair5:
```java
Integer retryCount1 = null;
String ACCOUNT1 = "";
Integer retryCount2 = 1;
String ACCOUNT2 = "";
```

## Input pair6:
```java
Integer retryCount1 = 5;
String ACCOUNT1 = "";
Integer retryCount2 = 1;
String ACCOUNT2 = "";
```

## Input pair7:
```java
Integer retryCount1 = null;
String ACCOUNT1 = "account123";
Integer retryCount2 = 1;
String ACCOUNT2 = "account123";
```



# OUTPUT FORMAT
```java
public class AzureClientFactoryTest_test_blobServiceClientBuilder_useNewClientForDifferentRetryCount {
    public static List<Object> inputTransformation_test_blobServiceClientBuilder_useNewClientForDifferentRetryCount(Integer retryCount1, String ACCOUNT1)  {
        // TODO
        Integer retryCount2 = 
		String ACCOUNT2 = 
		List<Object> transformed_inputs = Arrays.asList(retryCount2, ACCOUNT2);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.