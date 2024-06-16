## New input1:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test2", false);
```
Explanation: This input is valid because it changes the key from "test1" to "test2" and the value from true to false. This will test the functionality of the method toBean() when the JSON string contains a different key and value.

## New input2:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test3", true);
```
Explanation: This input is valid because it changes the key from "test1" to "test3". This will test the functionality of the method toBean() when the JSON string contains a different key.

## New input3:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", false);
```
Explanation: This input is valid because it changes the value from true to false. This will test the functionality of the method toBean() when the JSON string contains a different value.

## New input4:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("", true);
```
Explanation: This input is valid because it changes the key from "test1" to an empty string. This will test the functionality of the method toBean() when the JSON string contains an empty key.

## New input5:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", null);
```
Explanation: This input is valid because it changes the value from true to null. This will test the functionality of the method toBean() when the JSON string contains a null value.
