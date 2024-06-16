## New input1:
```java
    int year = 0;
    int half = 1;
```
Explanation: This input is valid because the year 0 is a valid year in the range of MIN_YEAR to MAX_YEAR. The half-of-year 1 is also a valid value from 1 to 2. This input tests the edge case where the year is at the minimum valid value.

## New input2:
```java
    int year = 9999;
    int half = 2;
```
Explanation: This input is valid because the year 9999 is a valid year in the range of MIN_YEAR to MAX_YEAR. The half-of-year 2 is also a valid value from 1 to 2. This input tests the edge case where the year is at the maximum valid value.

## New input3:
```java
    int year = -1;
    int half = 1;
```
Explanation: This input is valid because the year -1 is a valid year in the range of MIN_YEAR to MAX_YEAR. The half-of-year 1 is also a valid value from 1 to 2. This input tests the boundary case where the year is below the minimum valid value.

## New input4:
```java
    int year = 100;
    int half = 3;
```
Explanation: This input is invalid because the half-of-year 3 is not a valid value from 1 to 2. This input tests the boundary case where the half-of-year is above the maximum valid value.

## New input5:
```java
    int year = 100;
    int half = 0;
```
Explanation: This input is invalid because the half-of-year 0 is not a valid value from 1 to 2. This input tests the boundary case where the half-of-year is below the minimum valid value.
