## New input1:
```java
    int year1 = 0;
    int half1 = 1;
    int year2 = 1;
```
Explanation: This input is valid because the year 0 is a valid year in the range of MIN_YEAR to MAX_YEAR, and the half-of-year 1 is a valid value. This input tests the edge case where the year is at the minimum value and the half-of-year is at the valid value.

## New input2:
```java
    int year1 = 9999;
    int half1 = 2;
    int year2 = 10000;
```
Explanation: This input is valid because the year 9999 is a valid year in the range of MIN_YEAR to MAX_YEAR, and the half-of-year 2 is a valid value. This input tests the edge case where the year is at the maximum value and the half-of-year is at the valid value.

## New input3:
```java
    int year1 = 5000;
    int half1 = 1;
    int year2 = 5000;
```
Explanation: This input is valid because the year 5000 is a valid year in the range of MIN_YEAR to MAX_YEAR, and the half-of-year 1 is a valid value. This input tests the case where the year and half-of-year are at the same valid value.

## New input4:
```java
    int year1 = -1;
    int half1 = 2;
    int year2 = -2;
```
Explanation: This input is valid because the year -1 is a valid year in the range of MIN_YEAR to MAX_YEAR, and the half-of-year 2 is a valid value. This input tests the case where the year is at the minimum value and the half-of-year is at the valid value.

## New input5:
```java
    int year1 = 3000;
    int half1 = 1;
    int year2 = 3001;
```
Explanation: This input is valid because the year 3000 is a valid year in the range of MIN_YEAR to MAX_YEAR, and the half-of-year 1 is a valid value. This input tests the case where the year is at a valid value and the half-of-year is at the valid value.
