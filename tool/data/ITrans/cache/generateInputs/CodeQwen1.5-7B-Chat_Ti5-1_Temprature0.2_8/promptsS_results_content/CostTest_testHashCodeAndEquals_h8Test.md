## New input1:
```java
    Cost subject = Cost.costOfSeconds(0);
```
This input is valid because the `hashCode()` method is based on the value of the `Cost` object, and `costOfSeconds(0)` will have the same hash code as `costOfSeconds(10)`.

## New input2:
```java
    Cost subject = Cost.costOfSeconds(100);
```
This input is valid because the `hashCode()` method is based on the value of the `Cost` object, and `costOfSeconds(100)` will have a different hash code than `costOfSeconds(10)`.

## New input3:
```java
    Cost subject = Cost.costOfSeconds(-10);
```
This input is valid because the `hashCode()` method is based on the value of the `Cost` object, and `costOfSeconds(-10)` will have a different hash code than `costOfSeconds(10)`.

## New input4:
```java
    Cost subject = Cost.costOfSeconds(Integer.MAX_VALUE);
```
This input is valid because the `hashCode()` method is based on the value of the `Cost` object, and `costOfSeconds(Integer.MAX_VALUE)` will have a different hash code than `costOfSeconds(10)`.

## New input5:
```java
    Cost subject = Cost.costOfSeconds(Integer.MIN_VALUE);
```
This input is valid because the `hashCode()` method is based on the value of the `Cost` object, and `costOfSeconds(Integer.MIN_VALUE)` will have a different hash code than `costOfSeconds(10)`.
