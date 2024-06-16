## New input1:
```java
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
    anotherMap.put(2, 5);
```
Explanation: This input includes a new key-value pair (2, 5), which is a valid entry in the map. It is a boundary case because it is adding a new entry to the map, which is not present in the original map.

## New input2:
```java
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
    anotherMap.put(5, 15);
```
Explanation: This input includes an existing key-value pair (5, 15), which is a valid entry in the map. It is a boundary case because it is updating an existing entry in the map, which is present in the original map.

## New input3:
```java
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
    anotherMap.put(null, 5);
```
Explanation: This input includes a null key-value pair (null, 5), which is a valid entry in the map. It is a boundary case because it is adding a new entry with a null key, which is not present in the original map.

## New input4:
```java
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
    anotherMap.put(5, null);
```
Explanation: This input includes a null value-key pair (5, null), which is a valid entry in the map. It is a boundary case because it is updating an existing entry with a null value, which is present in the original map.

## New input5:
```java
    Map<Integer, Integer> anotherMap = new HashMap<>();
    anotherMap.put(5, 10);
    anotherMap.put(4, 3);
    anotherMap.put(3, 7);
    anotherMap.put(0, 0);
```
Explanation: This input includes a zero key-value pair (0, 0), which is a valid entry in the map. It is a boundary case because it is adding a new entry with a zero key, which is not present in the original map.
