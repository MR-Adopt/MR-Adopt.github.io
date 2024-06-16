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
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. The new source input satisfies this relation by using a different key ("key1") and a different value (100).

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
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. The new source input satisfies this relation by using an empty string as the key and a value of 0.

## New input pair2:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key3", null);
    String jsonString = "{\"key3\":null}";
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Generation code:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key3", null);
    String jsonString = JSONUtil.toJsonStr(pair);
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. The new source input satisfies this relation by using a key ("key3") and a null value.

## New input pair3:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key4", Integer.MAX_VALUE);
    String jsonString = "{\"key4\":2147483647}";
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Generation code:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key4", Integer.MAX_VALUE);
    String jsonString = JSONUtil.toJsonStr(pair);
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. The new source input satisfies this relation by using a key ("key4") and a value of Integer.MAX_VALUE.

## New input pair4:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key5", Integer.MIN_VALUE);
    String jsonString = "{\"key5\":-2147483648}";
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Generation code:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key5", Integer.MIN_VALUE);
    String jsonString = JSONUtil.toJsonStr(pair);
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. The new source input satisfies this relation by using a key ("key5") and a value of Integer.MIN_VALUE.
