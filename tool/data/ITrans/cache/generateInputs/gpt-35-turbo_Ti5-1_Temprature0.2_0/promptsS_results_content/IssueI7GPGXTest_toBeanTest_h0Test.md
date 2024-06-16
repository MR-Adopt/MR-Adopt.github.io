## New input1:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("", true);
```
Explanation: This input is valid because it tests the scenario where the key is an empty string.

## New input2:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test2", false);
```
Explanation: This input is valid because it tests the scenario where the value is false.

## New input3:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test3", null);
```
Explanation: This input is valid because it tests the scenario where the value is null.

## New input4:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>(null, true);
```
Explanation: This input is valid because it tests the scenario where the key is null.

## New input5:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test4", true);
```
Explanation: This input is valid because it tests the scenario where both the key and value are non-null and valid.