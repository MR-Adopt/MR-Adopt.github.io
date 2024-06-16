## New input pair0:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key1", 100);
    String jsonString = "{\"key1\":100}";
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Generation code:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key1", 100);
    String jsonString = JSONUtil.toJsonStr(pair);
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. The new input pair satisfies this relation by using a different key ("key1") and a different value (100).

## New input pair1:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("", 0);
    String jsonString = "{\"\":0}";
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Generation code:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("", 0);
    String jsonString = JSONUtil.toJsonStr(pair);
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. The new input pair satisfies this relation by using an empty string as the key and a value of 0.

## New input pair2:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("1234567890", 1234567890);
    String jsonString = "{\"1234567890\":1234567890}";
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Generation code:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("1234567890", 1234567890);
    String jsonString = JSONUtil.toJsonStr(pair);
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. The new input pair satisfies this relation by using a long key ("1234567890") and a corresponding long value (1234567890).

## New input pair3:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("null", null);
    String jsonString = "{\"null\":null}";
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Generation code:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("null", null);
    String jsonString = JSONUtil.toJsonStr(pair);
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. The new input pair satisfies this relation by using the string "null" as the key and a null value.

## New input pair4:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key", Integer.MAX_VALUE);
    String jsonString = "{\"key\":2147483647}";
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Generation code:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key", Integer.MAX_VALUE);
    String jsonString = JSONUtil.toJsonStr(pair);
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. The new input pair satisfies this relation by using the string "key" as the key and the maximum integer value (2147483647) as the value.
