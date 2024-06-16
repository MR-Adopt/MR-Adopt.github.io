## New input1:
```java
    Cost subject = Cost.costOfSeconds(0);
```
Explanation: This input is valid and boundary because it represents the minimum possible value for a cost, which is 0 seconds.

## New input2:
```java
    Cost subject = Cost.costOfSeconds(100);
```
Explanation: This input is valid and boundary because it represents the maximum possible value for a cost, which is 100 seconds.

## New input3:
```java
    Cost subject = Cost.costOfSeconds(-1);
```
Explanation: This input is invalid because it represents a negative value for a cost, which is not a valid input.

## New input4:
```java
    Cost subject = Cost.costOfSeconds(50);
```
Explanation: This input is valid and typical because it represents a typical value for a cost, which is 50 seconds.

## New input5:
```java
    Cost subject = Cost.costOfSeconds(999);
```
Explanation: This input is valid and boundary because it represents a value close to the maximum possible value for a cost, which is 999 seconds.
