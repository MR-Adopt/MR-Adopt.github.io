# NEW SOURCE INPUTS
## New source input0:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
### Code to generate follow-up input:
```java
String followUpInput = executor.getThreadPoolId();
```
### Explanation:
The inferred relation between the source input and follow-up input is that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the thread-pool id, which is used to create the `ThreadPoolPluginSupport` object. Therefore, the follow-up input is the thread-pool id obtained from the `executor` object.

## New input pair1:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
### Code to generate follow-up input:
```java
String followUpInput = executor.getThreadPoolId();
```
### Explanation:
The inferred relation between the source input and follow-up input is that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the thread-pool id, which is used to create the `ThreadPoolPluginSupport` object. Therefore, the follow-up input is the thread-pool id obtained from the `executor` object.

## New input pair2:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
### Code to generate follow-up input:
```java
String followUpInput = executor.getThreadPoolId();
```
### Explanation:
The inferred relation between the source input and follow-up input is that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the thread-pool id, which is used to create the `ThreadPoolPluginSupport` object. Therefore, the follow-up input is the thread-pool id obtained from the `executor` object.
