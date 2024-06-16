# ORIGINAL TEST CASE
```java
@Test
public void testCloseableResourceHolder() {
    AtomicLong closeCounter = new AtomicLong();
    Closeable closeable = closeCounter::incrementAndGet;
    ResourceHolder<Closeable> holder = ResourceHolder.fromCloseable(closeable);
    ResourceHolder<Closeable> holder2 = new CloseableResourceHolder<Closeable>(closeable);
    Assert.assertSame(closeable, holder2.get());
}

```
TEST INPUT: `closeable`


# METHOD UNDER TEST
```java
static <T extends Closeable> ResourceHolder<T> fromCloseable(final T resource) {
    return new CloseableResourceHolder<>(resource);
}

T get();

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `closeable`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Closeable closeable = closeCounter::incrementAndGet;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 