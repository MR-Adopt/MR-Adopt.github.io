# ORIGINAL TEST CASE
```java
@Test
public void keySetTest() {
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
    ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
    map.put(5, 6);
    map.put(3, 6);
    map.put(4, 6);
    Assert.assertEquals(anotherMap.keySet(), map.keySet());
}

```
TEST INPUT: `anotherMap`


# METHOD UNDER TEST
```java
/**
 * {@inheritDoc}
 */
@Override
public void putAll(Map<? extends K, ? extends V> m) {
    map.putAll(m);
}

/**
 * {@inheritDoc}
 */
@Override
public Set<K> keySet() {
    return map.keySet();
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `anotherMap`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 