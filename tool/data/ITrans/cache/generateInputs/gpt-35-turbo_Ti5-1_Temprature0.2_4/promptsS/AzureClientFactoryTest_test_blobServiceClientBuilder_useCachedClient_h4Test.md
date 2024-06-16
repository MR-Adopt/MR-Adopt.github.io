# ORIGINAL TEST CASE
```java
@Test
public void test_blobServiceClientBuilder_useCachedClient() {
    Integer retryCount1 = null;
    String ACCOUNT1 = "account";
    Integer retryCount2 = null;
    String ACCOUNT2 = "account";
    AzureAccountConfig config = new AzureAccountConfig();
    config.setUseAzureCredentialsChain(true);
    azureClientFactory = new AzureClientFactory(config);
    BlobServiceClient blobServiceClient = azureClientFactory.getBlobServiceClient(retryCount1, ACCOUNT1);
    BlobServiceClient blobServiceClient2 = azureClientFactory.getBlobServiceClient(retryCount2, ACCOUNT2);
    Assert.assertEquals(blobServiceClient, blobServiceClient2);
}

```
TEST INPUT: `retryCount1`,`ACCOUNT1`


# METHOD UNDER TEST
```java
// It's okay to store clients in a map here because all the configs for specifying azure retries are static, and there are only 2 of them.
// The 2 configs are AzureAccountConfig.maxTries and AzureOutputConfig.maxRetry.
// We will only ever have at most 2 clients in cachedBlobServiceClients per storage account.
public BlobServiceClient getBlobServiceClient(@Nullable Integer retryCount, String storageAccount) {
    return cachedBlobServiceClients.computeIfAbsent(Pair.of(storageAccount, retryCount != null ? retryCount : config.getMaxTries()), key -> buildNewClient(key.rhs, key.lhs));
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `retryCount1`,`ACCOUNT1`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Integer retryCount1 = null;
    String ACCOUNT1 = "account";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 