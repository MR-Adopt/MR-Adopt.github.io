## New input1:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("", true);
```
Explanation: This input is valid and boundary because an empty string is a valid input for a key in a key-value pair. It tests the edge case where the key is an empty string.

## New input2:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", false);
```
Explanation: This input is valid and boundary because a boolean value can be either true or false. It tests the edge case where the value is false.

## New input3:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", null);
```
Explanation: This input is valid and boundary because null is a valid value for a key-value pair. It tests the edge case where the value is null.

## New input4:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", true);
    hutoolPair.setValue(null);
```
Explanation: This input is valid and boundary because null is a valid value for a key-value pair. It tests the edge case where the value is null after setting it.

## New input5:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", true);
    hutoolPair.setKey(null);
```
Explanation: This input is valid and boundary because null is a valid value for a key-value pair. It tests the edge case where the key is null after setting it.
