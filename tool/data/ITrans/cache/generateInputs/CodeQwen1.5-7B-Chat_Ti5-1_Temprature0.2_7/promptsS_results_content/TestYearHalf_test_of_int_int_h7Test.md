## New input1:
```java
    int year = 0;
    int half = 1;
```
Explanation: This input is valid because the year 0 is a valid year in the range of MIN_YEAR (1) to MAX_YEAR (9999) in the YearHalf class. The half-of-year 1 is also a valid value from 1 to 2.

## New input2:
```java
    int year = 9999;
    int half = 2;
```
Explanation: This input is valid because the year 9999 is a valid year in the range of MIN_YEAR (1) to MAX_YEAR (9999) in the YearHalf class. The half-of-year 2 is also a valid value from 1 to 2.

## New input3:
```java
    int year = 5000;
    int half = 1;
```
Explanation: This input is valid because the year 5000 is a valid year in the range of MIN_YEAR (1) to MAX_YEAR (9999) in the YearHalf class. The half-of-year 1 is also a valid value from 1 to 2.

## New input4:
```java
    int year = 1;
    int half = 3;
```
Explanation: This input is valid because the year 1 is a valid year in the range of MIN_YEAR (1) to MAX_YEAR (9999) in the YearHalf class. The half-of-year 3 is not a valid value from 1 to 2. However, since the method of YearHalf.of() throws a DateTimeException if the half-of-year is not valid, this input will cause the test case to fail.

## New input5:
```java
    int year = -1;
    int half = 2;
```
Explanation: This input is valid because the year -1 is not a valid year in the range of MIN_YEAR (1) to MAX_YEAR (9999) in the YearHalf class. The half-of-year 2 is also not a valid value from 1 to 2. However, since the method of YearHalf.of() throws a DateTimeException if the year is not valid, this input will cause the test case to fail.
