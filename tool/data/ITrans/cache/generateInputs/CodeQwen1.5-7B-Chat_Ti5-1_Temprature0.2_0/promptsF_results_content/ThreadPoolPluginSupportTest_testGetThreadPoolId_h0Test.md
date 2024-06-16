# New input pair1:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
## Code used to generate follow-up input1:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
Explanation: The inferred relation is that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the thread-pool id, and the `getThreadPoolId()` method of the `ThreadPoolPluginSupport` class returns the thread-pool id. Therefore, to generate a follow-up input, we can create an `ExtensibleThreadPoolExecutor` object and use its `getThreadPoolId()` method to create a `ThreadPoolPluginSupport` object. This satisfies the inferred relation and ensures that the assertions in the original test case pass.
