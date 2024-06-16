# ORIGINAL TEST CASE
```java
@Test
public void testGetThreadPoolId() {
    ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
    ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
    Assert.assertEquals(executor.getThreadPoolId(), support.getThreadPoolId());
}

```
TEST INPUT: `executor`


# METHOD UNDER TEST
```java
/**
 * Get thread-pool id
 *
 * @return thread-pool id
 */
String getThreadPoolId();

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `executor`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java

```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 