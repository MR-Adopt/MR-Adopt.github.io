## New input1:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test2", false);
```
Explanation: This input is valid because it creates a new `Pair` object with a different key ("test2") and a different value (false). This ensures that the test case covers a different scenario than the original input.

## New input2:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test3", true);
```
Explanation: This input is valid because it creates a new `Pair` object with a different key ("test3") and the same value (true). This ensures that the test case covers a different scenario than the original input.

## New input3:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("", true);
```
Explanation: This input is valid because it creates a new `Pair` object with an empty key and the same value (true). This ensures that the test case covers a different scenario than the original input.

## New input4:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", null);
```
Explanation: This input is valid because it creates a new `Pair` object with the same key ("test1") but a null value. This ensures that the test case covers a different scenario than the original input.

## New input5:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>(null, true);
```
Explanation: This input is valid because it creates a new `Pair` object with a null key and the same value (true). This ensures that the test case covers a different scenario than the original input.
