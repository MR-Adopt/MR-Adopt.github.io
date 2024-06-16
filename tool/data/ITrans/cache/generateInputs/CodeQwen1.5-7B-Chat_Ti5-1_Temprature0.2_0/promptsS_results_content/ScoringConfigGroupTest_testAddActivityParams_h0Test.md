## New input1:
```java
    ActivityParams ap = new ActivityParams("");
```
Explanation: This input is valid and boundary because an empty string is a valid activity type. It tests the edge case where the activity type is an empty string.

## New input2:
```java
    ActivityParams ap = new ActivityParams(null);
```
Explanation: This input is valid and boundary because null is a valid activity type. It tests the edge case where the activity type is null.

## New input3:
```java
    ActivityParams ap = new ActivityParams("1234567890");
```
Explanation: This input is valid and boundary because a string of digits is a valid activity type. It tests the edge case where the activity type is a long string of digits.

## New input4:
```java
    ActivityParams ap = new ActivityParams("a".repeat(1000));
```
Explanation: This input is valid and boundary because a string of 1000 'a's is a valid activity type. It tests the edge case where the activity type is a very long string.

## New input5:
```java
    ActivityParams ap = new ActivityParams("type1");
    ap.setMaximumDuration(0);
```
Explanation: This input is valid and boundary because setting the maximum duration to 0 is a valid scenario. It tests the edge case where the maximum duration is set to zero.
