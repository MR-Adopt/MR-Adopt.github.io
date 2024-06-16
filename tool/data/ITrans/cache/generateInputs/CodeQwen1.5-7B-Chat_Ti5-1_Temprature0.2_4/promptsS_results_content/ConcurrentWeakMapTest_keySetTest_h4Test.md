## New input1:
```java
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
    anotherMap.put(1, 1);
```
Explanation: This input is valid and boundary because it adds a new key-value pair to the map, where the key is 1 and the value is 1. This is a valid input because the keys in the map are unique and the values can be any integer.

## New input2:
```java
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
    anotherMap.put(0, 0);
```
Explanation: This input is valid and boundary because it adds a new key-value pair to the map, where the key is 0 and the value is 0. This is a valid input because the keys in the map are unique and the values can be any integer.

## New input3:
```java
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
    anotherMap.put(Integer.MAX_VALUE, Integer.MAX_VALUE);
```
Explanation: This input is valid and boundary because it adds a new key-value pair to the map, where the key is `Integer.MAX_VALUE` and the value is `Integer.MAX_VALUE`. This is a valid input because the keys in the map are unique and the values can be any integer.

## New input4:
```java
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
    anotherMap.put(Integer.MIN_VALUE, Integer.MIN_VALUE);
```
Explanation: This input is valid and boundary because it adds a new key-value pair to the map, where the key is `Integer.MIN_VALUE` and the value is `Integer.MIN_VALUE`. This is a valid input because the keys in the map are unique and the values can be any integer.

## New input5:
```java
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
    anotherMap.put(null, 10);
```
Explanation: This input is valid and boundary because it adds a new key-value pair to the map, where the key is `null` and the value is 10. This is a valid input because the keys in the map can be `null`.
