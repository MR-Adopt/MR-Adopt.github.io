## New input1:
```java
    Cost subject = Cost.costOfSeconds(0);
```
Explanation: This input is valid because it tests the scenario where the cost is zero seconds.

## New input2:
```java
    Cost subject = Cost.costOfSeconds(Integer.MAX_VALUE);
```
Explanation: This input is valid because it tests the scenario where the cost is the maximum possible value for an integer.

## New input3:
```java
    Cost subject = Cost.costOfSeconds(-10);
```
Explanation: This input is valid because it tests the scenario where the cost is a negative value.

## New input4:
```java
    Cost subject = Cost.costOfSeconds(1000000);
```
Explanation: This input is valid because it tests the scenario where the cost is a large positive value.

## New input5:
```java
    Cost subject = Cost.costOfSeconds(1);
```
Explanation: This input is valid because it tests the scenario where the cost is a small positive value.