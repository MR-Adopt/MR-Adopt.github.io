# ORIGINAL TEST CASE
```java
@Test
public void testGetThreadPoolId() {
    ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
    ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
    Assert.assertEquals(executor.getThreadPoolId(), support.getThreadPoolId());
}

```
SOURCE INPUT: `executor`
FOLLOW UP INPUT: `support`


# METHOD UNDER TEST
```java
/**
 * Get thread-pool id
 *
 * @return thread-pool id
 */
String getThreadPoolId();

```


# NEW SOURCE INPUTS
## New source input0:
```java

```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java

```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.