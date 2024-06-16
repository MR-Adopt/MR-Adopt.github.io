## New input1:
```java
    int year = 0;
    int half = 1;
```
Explanation: This input is valid because the year 0 is a valid year in the range of MIN_YEAR to MAX_YEAR in the YearHalf class. The half-of-year 1 is also a valid value from 1 to 2. This input tests the edge case where the year is at the minimum valid value.

## New input2:
```java
    int year = 9999;
    int half = 2;
```
Explanation: This input is valid because the year 9999 is a valid year in the range of MIN_YEAR to MAX_YEAR in the YearHalf class. The half-of-year 2 is also a valid value from 1 to 2. This input tests the edge case where the year is at the maximum valid value.

## New input3:
```java
    int year = 5000;
    int half = 1;
```
Explanation: This input is valid because the year 5000 is a valid year in the range of MIN_YEAR to MAX_YEAR in the YearHalf class. The half-of-year 1 is also a valid value from 1 to 2. This input tests the case where the year is in the middle of the valid range.

## New input4:
```java
    int year = -1;
    int half = 2;
```
Explanation: This input is valid because the year -1 is a valid year in the range of MIN_YEAR to MAX_YEAR in the YearHalf class. The half-of-year 2 is also a valid value from 1 to 2. This input tests the case where the year is at the minimum invalid value.

## New input5:
```java
    int year = 10000;
    int half = 1;
```
Explanation: This input is valid because the year 10000 is a valid year in the range of MIN_YEAR to MAX_YEAR in the YearHalf class. The half-of-year 1 is also a valid value from 1 to 2. This input tests the case where the year is at the maximum invalid value.
