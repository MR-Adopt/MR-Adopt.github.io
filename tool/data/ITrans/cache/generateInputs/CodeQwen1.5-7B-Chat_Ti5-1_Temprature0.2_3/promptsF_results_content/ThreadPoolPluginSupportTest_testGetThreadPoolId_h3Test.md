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
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
```
### Code used to generate follow-up input:
```java
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
### Explanation:
The new source input0 is the `executor` object, which is created in the original test case. The follow-up input is the `support` object, which is created by passing the `executor.getThreadPoolId()` to the `TestSupport` constructor. This satisfies the inferred relation that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the same thread-pool id as the `getThreadPoolId()` method of the `ThreadPoolPluginSupport` class.

## New source input1:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
```
### Code used to generate follow-up input:
```java
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
### Explanation:
The new source input1 is the `executor` object, which is created in the original test case. The follow-up input is the `support` object, which is created by passing the `executor.getThreadPoolId()` to the `TestSupport` constructor. This satisfies the inferred relation that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the same thread-pool id as the `getThreadPoolId()` method of the `ThreadPoolPluginSupport` class.

## New source input2:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
```
### Code used to generate follow-up input:
```java
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
### Explanation:
The new source input2 is the `executor` object, which is created in the original test case. The follow-up input is the `support` object, which is created by passing the `executor.getThreadPoolId()` to the `TestSupport` constructor. This satisfies the inferred relation that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the same thread-pool id as the `getThreadPoolId()` method of the `ThreadPoolPluginSupport` class.

## New source input3:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
```
### Code used to generate follow-up input:
```java
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
### Explanation:
The new source input3 is the `executor` object, which is created in the original test case. The follow-up input is the `support` object, which is created by passing the `executor.getThreadPoolId()` to the `TestSupport` constructor. This satisfies the inferred relation that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the same thread-pool id as the `getThreadPoolId()` method of the `ThreadPoolPluginSupport` class.

## New source input4:
```java
ExtensibleThreadPoolExecutor executor = new ExtensibleThreadPoolExecutor("test", manager, 5, 5, 1000L, TimeUnit.MILLISECONDS, new ArrayBlockingQueue<>(1), Thread::new, new ThreadPoolExecutor.AbortPolicy());
```
### Code used to generate follow-up input:
```java
ThreadPoolPluginSupport support = new TestSupport(executor.getThreadPoolId(), executor, manager);
```
### Explanation:
The new source input4 is the `executor` object, which is created in the original test case. The follow-up input is the `support` object, which is created by passing the `executor.getThreadPoolId()` to the `TestSupport` constructor. This satisfies the inferred relation that the `getThreadPoolId()` method of the `ExtensibleThreadPoolExecutor` class returns the same thread-pool id as the `getThreadPoolId()` method of the `ThreadPoolPluginSupport` class.
