## New input1:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("", true);
```
Explanation: This input is valid and boundary because an empty string is a valid input for a key in a key-value pair, and true is a valid boolean value. This input tests the edge case where the key is an empty string.

## New input2:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", false);
```
Explanation: This input is valid and boundary because "test1" is a valid string and false is a valid boolean value. This input tests the edge case where the boolean value is false.

## New input3:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", null);
```
Explanation: This input is valid and boundary because "test1" is a valid string and null is a valid boolean value. This input tests the edge case where the boolean value is null.

## New input4:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>(null, true);
```
Explanation: This input is valid and boundary because null is a valid string and true is a valid boolean value. This input tests the edge case where the key is null.

## New input5:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", true);
```
Explanation: This input is valid and boundary because "test1" is a valid string and true is a valid boolean value. This input tests the normal case where the key and boolean value are valid.
