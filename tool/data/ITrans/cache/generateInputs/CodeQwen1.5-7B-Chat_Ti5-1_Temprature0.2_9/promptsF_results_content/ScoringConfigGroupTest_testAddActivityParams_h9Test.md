## New input pair0:
```java
    ActivityParams ap = new ActivityParams("type2");
    String type = "type2";
```
Follow-up input:
```java
    c.addActivityParams(ap);
    Assertions.assertEquals(ap, c.getActivityParams(type));
```
Explanation: The new source input `ap` is created with a different activity type ("type2") than the original source input `ap` ("type1"). The follow-up input adds the new activity parameters to the `ScoringConfigGroup` and then retrieves them using the new activity type. This satisfies the inferred relation that the new source input should be related to the original source input in terms of adding and retrieving activity parameters.

## New input pair1:
```java
    ActivityParams ap = new ActivityParams("");
    String type = "";
```
Follow-up input:
```java
    c.addActivityParams(ap);
    Assertions.assertEquals(ap, c.getActivityParams(type));
```
Explanation: The new source input `ap` is created with an empty activity type (""). The follow-up input adds the new activity parameters to the `ScoringConfigGroup` and then retrieves them using the empty activity type. This satisfies the inferred relation that the new source input should be related to the original source input in terms of adding and retrieving activity parameters.

## New input pair2:
```java
    ActivityParams ap = new ActivityParams(null);
    String type = null;
```
Follow-up input:
```java
    c.addActivityParams(ap);
    Assertions.assertEquals(ap, c.getActivityParams(type));
```
Explanation: The new source input `ap` is created with a null activity type (null). The follow-up input adds the new activity parameters to the `ScoringConfigGroup` and then retrieves them using the null activity type. This satisfies the inferred relation that the new source input should be related to the original source input in terms of adding and retrieving activity parameters.

## New input pair3:
```java
    ActivityParams ap = new ActivityParams("type1");
    ap.setMaximumDuration(3600);
    String type = "type1";
```
Follow-up input:
```java
    c.addActivityParams(ap);
    Assertions.assertEquals(ap, c.getActivityParams(type));
```
Explanation: The new source input `ap` is created with the same activity type ("type1") as the original source input `ap`. It also sets a maximum duration of 3600 seconds. The follow-up input adds the new activity parameters to the `ScoringConfigGroup` and then retrieves them using the same activity type. This satisfies the inferred relation that the new source input should be related to the original source input in terms of adding and retrieving activity parameters.

## New input pair4:
```java
    ActivityParams ap = new ActivityParams("type1");
    ap.setMinimumDuration(1800);
    String type = "type1";
```
Follow-up input:
```java
    c.addActivityParams(ap);
    Assertions.assertEquals(ap, c.getActivityParams(type));
```
Explanation: The new source input `ap` is created with the same activity type ("type1") as the original source input `ap`. It also sets a minimum duration of 1800 seconds. The follow-up input adds the new activity parameters to the `ScoringConfigGroup` and then retrieves them using the same activity type. This satisfies the inferred relation that the new source input should be related to the original source input in terms of adding and retrieving activity parameters.
