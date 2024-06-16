## New input1:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key1", 100);
```
Explanation: This input is valid because it creates a `Map.Entry` with a non-empty string key and a non-negative integer value. This covers a different scenario from the original test case, as it uses a different key and a different value.

## New input2:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("", 0);
```
Explanation: This input is valid because it creates a `Map.Entry` with an empty string key and a zero integer value. This covers a different scenario from the original test case, as it uses a different key and a different value.

## New input3:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key2", -1);
```
Explanation: This input is valid because it creates a `Map.Entry` with a non-empty string key and a negative integer value. This covers a different scenario from the original test case, as it uses a different key and a different value.

## New input4:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key3", null);
```
Explanation: This input is valid because it creates a `Map.Entry` with a non-empty string key and a null integer value. This covers a different scenario from the original test case, as it uses a different key and a different value.

## New input5:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>(null, 2);
```
Explanation: This input is valid because it creates a `Map.Entry` with a null string key and a non-negative integer value. This covers a different scenario from the original test case, as it uses a different key and a different value.
