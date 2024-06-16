## New input1:
```java
    Cost subject = Cost.costOfSeconds(0);
```
Explanation: This input is valid because it tests the scenario where the cost value is 0 seconds.

## New input2:
```java
    Cost subject = Cost.costOfSeconds(Integer.MAX_VALUE);
```
Explanation: This input is valid because it tests the scenario where the cost value is the maximum possible integer value.

## New input3:
```java
    Cost subject = Cost.costOfSeconds(-10);
```
Explanation: This input is valid because it tests the scenario where the cost value is a negative number.

## New input4:
```java
    Cost subject = Cost.costOfSeconds(1000000);
```
Explanation: This input is valid because it tests the scenario where the cost value is a large positive number.

## New input5:
```java
    Cost subject = Cost.costOfSeconds(Integer.MIN_VALUE);
```
Explanation: This input is valid because it tests the scenario where the cost value is the minimum possible integer value.