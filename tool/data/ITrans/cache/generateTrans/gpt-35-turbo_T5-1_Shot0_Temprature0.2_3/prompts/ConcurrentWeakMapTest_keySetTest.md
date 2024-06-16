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


# TEST CASE
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
SOURCE INPUT: `anotherMap`
FOLLOW UP INPUT: `map`


# OTHER INPUT PAIRS 
## Input pair1:
```java
Map<Integer, Integer> anotherMap = new HashMap<>();
anotherMap.put(5, 10);
anotherMap.put(4, 3);
anotherMap.put(3, 7);
ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
map.put(5, 6);
map.put(3, 6);
map.put(4, 6);
```

## Input pair2:
```java
Map<Integer, Integer> anotherMap = new HashMap<>();
anotherMap.put(1, 2);
anotherMap.put(2, 3);
anotherMap.put(3, 4);
ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
map.putAll(anotherMap);
```

## Input pair3:
```java
Map<Integer, Integer> anotherMap = new HashMap<>();
anotherMap.put(10, 20);
anotherMap.put(20, 30);
anotherMap.put(30, 40);
ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
map.putAll(anotherMap);
```

## Input pair4:
```java
Map<Integer, Integer> anotherMap = new HashMap<>();
anotherMap.put(100, 200);
anotherMap.put(200, 300);
anotherMap.put(300, 400);
ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
map.putAll(anotherMap);
```

## Input pair5:
```java
Map<Integer, Integer> anotherMap = new HashMap<>();
anotherMap.put(0, 0);
anotherMap.put(1, 1);
anotherMap.put(2, 2);
ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
map.putAll(anotherMap);
```

## Input pair6:
```java
Map<Integer, Integer> anotherMap = new HashMap<>();
anotherMap.put(-1, -2);
anotherMap.put(-2, -3);
anotherMap.put(-3, -4);
ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
map.putAll(anotherMap);
```

## Input pair7:
```java
Map<Integer, Integer> anotherMap = new HashMap<>();
anotherMap.put(1, 2);
anotherMap.put(2, 3);
anotherMap.put(3, 4);
ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
map.put(1, 6);
map.put(2, 6);
map.put(3, 6);
```

## Input pair8:
```java
Map<Integer, Integer> anotherMap = new HashMap<>();
anotherMap.put(10, 20);
anotherMap.put(20, 30);
anotherMap.put(30, 40);
ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
map.put(10, 6);
map.put(20, 6);
map.put(30, 6);
```

## Input pair9:
```java
Map<Integer, Integer> anotherMap = new HashMap<>();
anotherMap.put(100, 200);
anotherMap.put(200, 300);
anotherMap.put(300, 400);
ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
map.put(100, 6);
map.put(200, 6);
map.put(300, 6);
```

## Input pair10:
```java
Map<Integer, Integer> anotherMap = new HashMap<>();
anotherMap.put(0, 0);
anotherMap.put(1, 1);
anotherMap.put(2, 2);
ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
map.put(0, 6);
map.put(1, 6);
map.put(2, 6);
```

## Input pair11:
```java
Map<Integer, Integer> anotherMap = new HashMap<>();
anotherMap.put(-1, -2);
anotherMap.put(-2, -3);
anotherMap.put(-3, -4);
ConcurrentWeakMap<Integer, Integer> map = new ConcurrentWeakMap<>();
map.put(-1, 6);
map.put(-2, 6);
map.put(-3, 6);
```



# OUTPUT FORMAT
```java
public class ConcurrentWeakMapTest_keySetTest {
    public static ConcurrentWeakMap<Integer, Integer> inputTransformation_keySetTest(Map<Integer, Integer> anotherMap)  {
        // TODO
        ConcurrentWeakMap<Integer, Integer> map = 
		return map;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.