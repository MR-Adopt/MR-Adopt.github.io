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
    Pair<Integer, Integer> pair = Pair.of(Integer.MAX_VALUE, Integer.MIN_VALUE);
```
Explanation: This input is valid because it tests the scenario where the key is the maximum value of Integer and the value is the minimum value of Integer.

## New input4:
```java
    Pair<Integer, Integer> pair = Pair.of(null, null);
```
Explanation: This input is valid because it tests the scenario where both key and value are null.

## New input5:
```java
    Pair<Integer, Integer> pair = Pair.of(123456789, 987654321);
```
Explanation: This input is valid because it tests the scenario where both key and value are positive numbers.