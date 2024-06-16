## New input1:
```java
    ActivityParams ap = new ActivityParams("");
```
Explanation: This input is valid and boundary because an empty string is a valid activity type. It tests the edge case where the activity type is an empty string.

## New input2:
```java
    ActivityParams ap = new ActivityParams(null);
```
Explanation: This input is valid and boundary because null is not a valid activity type. It tests the edge case where the activity type is null.

## New input3:
```java
    ActivityParams ap = new ActivityParams("type1");
    ap.setMode("car");
```
Explanation: This input is valid and boundary because setting a mode for the activity type "type1" is a valid operation. It tests the edge case where the mode is set for the activity type.

## New input4:
```java
    ActivityParams ap = new ActivityParams("type1");
    ap.setMaximumDuration(Duration.ofHours(24));
```
Explanation: This input is valid and boundary because setting a maximum duration of 24 hours for the activity type "type1" is a valid operation. It tests the edge case where the maximum duration is set for the activity type.

## New input5:
```java
    ActivityParams ap = new ActivityParams("type1");
    ap.setScoreExpression("1");
```
Explanation: This input is valid and boundary because setting a score expression of "1" for the activity type "type1" is a valid operation. It tests the edge case where the score expression is set for the activity type.
