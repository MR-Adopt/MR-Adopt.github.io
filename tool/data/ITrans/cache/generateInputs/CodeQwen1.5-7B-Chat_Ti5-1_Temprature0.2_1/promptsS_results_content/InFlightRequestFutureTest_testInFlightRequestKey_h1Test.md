## New input1:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
```
Explanation: This input is valid because it represents the original test case scenario with the same group name, partition, and offset. This is a boundary-case scenario as all values are at their minimum.

## New input2:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", Integer.MAX_VALUE, Integer.MAX_VALUE);
```
Explanation: This input is valid because it represents the maximum possible values for partition and offset. This is a boundary-case scenario as all values are at their maximum.

## New input3:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("", 0, 0);
```
Explanation: This input is valid because it represents an empty group name. This is a boundary-case scenario as the group name is an empty string.

## New input4:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, -1);
```
Explanation: This input is valid because it represents an offset that is less than zero. This is a boundary-case scenario as the offset is negative.

## New input5:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", -1, 0);
```
Explanation: This input is valid because it represents a partition that is less than zero. This is a boundary-case scenario as the partition is negative.
