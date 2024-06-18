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
SOURCE INPUT: `closeable`
FOLLOW UP INPUT: `holder2`


# METHOD UNDER TEST
```java
static <T extends Closeable> ResourceHolder<T> fromCloseable(final T resource) {
    return new CloseableResourceHolder<>(resource);
}

T get();

```


# NEW SOURCE INPUTS
## New source input0:
```java
    Closeable closeable = new FileInputStream("file.txt");
```

## New source input1:
```java
    Closeable closeable = new Socket("localhost", 8080);
```

## New source input2:
```java
    Closeable closeable = new ByteArrayInputStream(new byte[]{1, 2, 3});
```

## New source input3:
```java
    Closeable closeable = new PipedInputStream();
```

## New source input4:
```java
    Closeable closeable = new FilterInputStream(new FileInputStream("file.txt")) {
        @Override
        public void close() throws IOException {
            super.close();
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    Closeable closeable = closeCounter::incrementAndGet;
    ResourceHolder<Closeable> holder2 = new CloseableResourceHolder<Closeable>(closeable);
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.