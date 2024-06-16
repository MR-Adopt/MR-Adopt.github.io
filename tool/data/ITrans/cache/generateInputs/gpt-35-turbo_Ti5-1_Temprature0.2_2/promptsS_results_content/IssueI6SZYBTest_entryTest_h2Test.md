## New input1:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("abc", 123);
```
Explanation: This input is valid because it creates a new `Map.Entry` object with a `String` key "abc" and an `Integer` value 123.

## New input2:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("xyz", 0);
```
Explanation: This input is valid because it creates a new `Map.Entry` object with a `String` key "xyz" and an `Integer` value 0.

## New input3:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key", -100);
```
Explanation: This input is valid because it creates a new `Map.Entry` object with a `String` key "key" and an `Integer` value -100.

## New input4:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("", 999);
```
Explanation: This input is valid because it creates a new `Map.Entry` object with an empty `String` key and an `Integer` value 999.

## New input5:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>(null, null);
```
Explanation: This input is valid because it creates a new `Map.Entry` object with `null` key and `null` value.