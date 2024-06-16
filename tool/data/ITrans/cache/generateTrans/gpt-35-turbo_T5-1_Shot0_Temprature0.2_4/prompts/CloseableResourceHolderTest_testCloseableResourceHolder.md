# METHOD UNDER TEST
```java
static <T extends Closeable> ResourceHolder<T> fromCloseable(final T resource) {
    return new CloseableResourceHolder<>(resource);
}

T get();

```


# TEST CASE
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
SOURCE INPUT: `closeable`
FOLLOW UP INPUT: `holder2`


# OTHER INPUT PAIRS 



# OUTPUT FORMAT
```java
public class CloseableResourceHolderTest_testCloseableResourceHolder {
    public static ResourceHolder<Closeable> inputTransformation_testCloseableResourceHolder(Closeable closeable)  {
        // TODO
        ResourceHolder<Closeable> holder2 = 
		return holder2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.