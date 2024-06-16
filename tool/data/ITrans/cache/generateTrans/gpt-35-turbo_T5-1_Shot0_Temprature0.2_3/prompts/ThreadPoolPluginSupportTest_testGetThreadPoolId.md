# METHOD UNDER TEST
```java
/**
 * Get thread-pool id
 *
 * @return thread-pool id
 */
String getThreadPoolId();

```


# TEST CASE
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


# OTHER INPUT PAIRS 
## Input pair1:
```java

```

## Input pair2:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```

## Input pair3:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("new-test", manager, 10, 10, 2000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```



# OUTPUT FORMAT
```java
public class ThreadPoolPluginSupportTest_testGetThreadPoolId {
    public static ThreadPoolPluginSupport inputTransformation_testGetThreadPoolId(ExtensibleThreadPoolExecutor executor)  {
        // TODO
        ThreadPoolPluginSupport support = 
		return support;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.