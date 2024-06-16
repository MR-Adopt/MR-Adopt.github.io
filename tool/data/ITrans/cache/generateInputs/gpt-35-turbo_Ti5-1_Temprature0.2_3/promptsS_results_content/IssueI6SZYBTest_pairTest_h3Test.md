## New input1:
```java
    Pair<Integer, Integer> pair = Pair.of(0, 0);
```
Explanation: This input is valid because it tests the scenario where both key and value are zero.

## New input2:
```java
    Pair<Integer, Integer> pair = Pair.of(-1, -1);
```
Explanation: This input is valid because it tests the scenario where both key and value are negative numbers.

## New input3:
```java
    Pair<Integer, Integer> pair = Pair.of(Integer.MAX_VALUE, Integer.MAX_VALUE);
```
Explanation: This input is valid because it tests the scenario where both key and value are the maximum possible integer values.

## New input4:
```java
    Pair<Integer, Integer> pair = Pair.of(Integer.MIN_VALUE, Integer.MIN_VALUE);
```
Explanation: This input is valid because it tests the scenario where both key and value are the minimum possible integer values.

## New input5:
```java
    Pair<Integer, Integer> pair = Pair.of(100, -100);
```
Explanation: This input is valid because it tests the scenario where the key is a positive number and the value is a negative number.