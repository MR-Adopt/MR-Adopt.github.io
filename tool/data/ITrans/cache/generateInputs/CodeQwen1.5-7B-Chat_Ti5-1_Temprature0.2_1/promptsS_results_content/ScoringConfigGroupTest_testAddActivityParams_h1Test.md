## New input1:
```java
    ActivityParams ap = new ActivityParams("");
```
Explanation: This input is valid because an empty string is a valid activity type. It tests the edge case where the activity type is an empty string.

## New input2:
```java
    ActivityParams ap = new ActivityParams(null);
```
Explanation: This input is valid because null is a valid activity type. It tests the edge case where the activity type is null.

## New input3:
```java
    ActivityParams ap = new ActivityParams("type1");
    ap.setMaximumDuration(0);
```
Explanation: This input is valid because a duration of 0 is a valid duration. It tests the edge case where the maximum duration is set to 0.

## New input4:
```java
    ActivityParams ap = new ActivityParams("type1");
    ap.setMaximumDuration(Double.MAX_VALUE);
```
Explanation: This input is valid because a duration of Double.MAX_VALUE is a valid duration. It tests the edge case where the maximum duration is set to the maximum possible value.

## New input5:
```java
    ActivityParams ap = new ActivityParams("type1");
    ap.setMaximumDuration(Double.MIN_VALUE);
```
Explanation: This input is valid because a duration of Double.MIN_VALUE is a valid duration. It tests the edge case where the maximum duration is set to the minimum possible value.
