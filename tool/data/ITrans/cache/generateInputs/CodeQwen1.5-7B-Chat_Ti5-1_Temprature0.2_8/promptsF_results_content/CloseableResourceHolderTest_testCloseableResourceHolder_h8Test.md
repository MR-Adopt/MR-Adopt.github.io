# New input pair0:
```java
    Closeable closeable = () -> {};
    ResourceHolder<Closeable> holder2 = new CloseableResourceHolder<Closeable>(closeable);
```
Generation code:
```java
    Closeable closeable = () -> {};
    ResourceHolder<Closeable> holder2 = ResourceHolder.fromCloseable(closeable);
```
Explanation: The inferred relation is that `holder2` is created by calling `fromCloseable(closeable)`. Since `closeable` is a lambda expression that does nothing, `holder2` should also be created by calling `fromCloseable(closeable)`.

# New input pair1:
```java
    Closeable closeable = new Closeable() {
        @Override
        public void close() throws IOException {
            // Do nothing
        }
    };
    ResourceHolder<Closeable> holder2 = new CloseableResourceHolder<Closeable>(closeable);
```
Generation code:
```java
    Closeable closeable = new Closeable() {
        @Override
        public void close() throws IOException {
            // Do nothing
        }
    };
    ResourceHolder<Closeable> holder2 = ResourceHolder.fromCloseable(closeable);
```
Explanation: The inferred relation is that `holder2` is created by calling `fromCloseable(closeable)`. Since `closeable` is an anonymous inner class that does nothing, `holder2` should also be created by calling `fromCloseable(closeable)`.

# New input pair2:
```java
    Closeable closeable = new Closeable() {
        @Override
        public void close() throws IOException {
            throw new IOException("Test exception");
        }
    };
    ResourceHolder<Closeable> holder2 = new CloseableResourceHolder<Closeable>(closeable);
```
Generation code:
```java
    Closeable closeable = new Closeable() {
        @Override
        public void close() throws IOException {
            throw new IOException("Test exception");
        }
    };
    ResourceHolder<Closeable> holder2 = ResourceHolder.fromCloseable(closeable);
```
Explanation: The inferred relation is that `holder2` is created by calling `fromCloseable(closeable)`. Since `closeable` is an anonymous inner class that throws an exception, `holder2` should also be created by calling `fromCloseable(closeable)`.
