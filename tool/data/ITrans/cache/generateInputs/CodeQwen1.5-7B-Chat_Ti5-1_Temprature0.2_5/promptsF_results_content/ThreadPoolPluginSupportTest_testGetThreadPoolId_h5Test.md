# NEW SOURCE INPUTS
## New source input1:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
### Code to generate follow-up input1:
```java
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
Explanation: The inferred relation between the source input and the follow-up input is that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the same value as the `getThreadPoolId()` method of the `ThreadPoolPluginSupport` class. Therefore, when we create a new `ThreadPoolPluginSupport` object using the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` object, the two objects will have the same thread-pool id.

## New source input2:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
### Code to generate follow-up input2:
```java
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
Explanation: The inferred relation between the source input and the follow-up input is that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the same value as the `getThreadPoolId()` method of the `ThreadPoolPluginSupport` class. Therefore, when we create a new `ThreadPoolPluginSupport` object using the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` object, the two objects will have the same thread-pool id.

## New source input3:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
### Code to generate follow-up input3:
```java
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
Explanation: The inferred relation between the source input and the follow-up input is that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the same value as the `getThreadPoolId()` method of the `ThreadPoolPluginSupport` class. Therefore, when we create a new `ThreadPoolPluginSupport` object using the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` object, the two objects will have the same thread-pool id.
