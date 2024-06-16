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
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. Since the key is "key1" and the value is 100, the JSON string representation should be `{"key1":100}`.

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
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. Since the key is an empty string and the value is 0, the JSON string representation should be `{"":0}`.

## New input pair2:
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
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. Since the key is "null" and the value is null, the JSON string representation should be `{"null":null}`.

## New input pair3:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("123", 456);
    String jsonString = "{\"123\":456}";
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Generation code:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("123", 456);
    String jsonString = JSONUtil.toJsonStr(pair);
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. Since the key is "123" and the value is 456, the JSON string representation should be `{"123":456}`.

## New input pair4:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("true", 1);
    String jsonString = "{\"true\":1}";
    Class beanClass = AbstractMap.SimpleEntry.class;
```
Generation code:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("true", 1);
    String jsonString = JSONUtil.toJsonStr(pair);
```
Explanation: The inferred relation is that the JSON string representation of the map entry should match the key-value pair in the map entry. Since the key is "true" and the value is 1, the JSON string representation should be `{"true":1}`.
