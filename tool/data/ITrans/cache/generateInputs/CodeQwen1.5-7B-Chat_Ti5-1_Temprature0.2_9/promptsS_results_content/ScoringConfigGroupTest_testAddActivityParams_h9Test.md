## New input1:
```java
    ActivityParams ap = new ActivityParams("type2");
```
Explanation: This input is valid because it creates a new `ActivityParams` object with a different activity type ("type2") than the original one ("type1"). This ensures that the method under test is tested with a different scenario.

## New input2:
```java
    ActivityParams ap = new ActivityParams("");
```
Explanation: This input is valid because it creates a new `ActivityParams` object with an empty activity type. This could be a valid scenario for the method under test, as it might handle empty activity types gracefully.

## New input3:
```java
    ActivityParams ap = new ActivityParams(null);
```
Explanation: This input is valid because it creates a new `ActivityParams` object with a null activity type. This could be a valid scenario for the method under test, as it might handle null activity types gracefully.

## New input4:
```java
    ActivityParams ap = new ActivityParams("type1");
    ap.setMaximumDuration(3600);
```
Explanation: This input is valid because it creates a new `ActivityParams` object with the same activity type ("type1") as the original one, but with a maximum duration of 3600 seconds. This ensures that the method under test is tested with a different scenario.

## New input5:
```java
    ActivityParams ap = new ActivityParams("type1");
    ap.setMinimumDuration(1800);
```
Explanation: This input is valid because it creates a new `ActivityParams` object with the same activity type ("type1") as the original one, but with a minimum duration of 1800 seconds. This ensures that the method under test is tested with a different scenario.
