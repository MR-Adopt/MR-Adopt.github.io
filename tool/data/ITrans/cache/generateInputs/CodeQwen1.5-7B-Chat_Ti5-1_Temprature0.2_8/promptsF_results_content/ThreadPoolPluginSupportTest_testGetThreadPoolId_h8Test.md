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
Explanation: The inferred relation between the source input and follow-up input is that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the same thread-pool id as the `getThreadPoolId()` method of the `ThreadPoolPluginSupport` class. Therefore, when we create a new `ExtensibleThreadPoolExecutor` instance and pass its `getThreadPoolId()` method result to the `ThreadPoolPluginSupport` constructor, the two thread-pool ids should be the same.

# New input pair2:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
## Code used to generate follow-up input2:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
Explanation: The inferred relation between the source input and follow-up input is that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the same thread-pool id as the `getThreadPoolId()` method of the `ThreadPoolPluginSupport` class. Therefore, when we create a new `ExtensibleThreadPoolExecutor` instance and pass its `getThreadPoolId()` method result to the `ThreadPoolPluginSupport` constructor, the two thread-pool ids should be the same.
