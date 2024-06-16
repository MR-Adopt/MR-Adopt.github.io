## New input1:
```java
    int year = Year.MIN_YEAR;
    int half = 1;
```
Explanation: This input is valid because it tests the minimum value for the year, which is the minimum allowed value according to the method's documentation.

## New input2:
```java
    int year = Year.MAX_YEAR;
    int half = 2;
```
Explanation: This input is valid because it tests the maximum value for the year, which is the maximum allowed value according to the method's documentation. Additionally, it tests the maximum value for the half, which is also within the valid range.

## New input3:
```java
    int year = 2022;
    int half = 1;
```
Explanation: This input is valid because it tests a typical year value that falls within the valid range. It also tests the minimum value for the half, which is within the valid range.

## New input4:
```java
    int year = 2023;
    int half = 2;
```
Explanation: This input is valid because it tests a typical year value that falls within the valid range. It also tests the maximum value for the half, which is within the valid range.

## New input5:
```java
    int year = 1999;
    int half = 2;
```
Explanation: This input is valid because it tests a year value that falls within the valid range. It also tests the maximum value for the half, which is within the valid range. Additionally, it tests a year value that is not the minimum or maximum allowed value.