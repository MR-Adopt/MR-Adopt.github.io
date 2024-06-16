## New input1:
```java
    Cost subject = Cost.costOfSeconds(0);
```
Explanation: This input is valid because the `costOfSeconds` method allows for the creation of a cost of 0 seconds. This is a boundary case as it is the lowest possible value for a cost.

## New input2:
```java
    Cost subject = Cost.costOfSeconds(100);
```
Explanation: This input is valid because the `costOfSeconds` method allows for the creation of a cost of 100 seconds. This is a boundary case as it is the highest possible value for a cost.

## New input3:
```java
    Cost subject = Cost.costOfSeconds(-1);
```
Explanation: This input is invalid because the `costOfSeconds` method does not allow for the creation of a cost of -1 seconds. This is a boundary case as it is the lowest possible value for a non-negative cost.

## New input4:
```java
    Cost subject = Cost.costOfSeconds(999999999);
```
Explanation: This input is valid because the `costOfSeconds` method allows for the creation of a cost of 999999999 seconds. This is a boundary case as it is the highest possible value for a cost.

## New input5:
```java
    Cost subject = Cost.costOfSeconds(50);
```
Explanation: This input is valid because the `costOfSeconds` method allows for the creation of a cost of 50 seconds. This is a typical case as it is a common value for a cost.
