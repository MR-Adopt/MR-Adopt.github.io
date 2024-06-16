## New input1:
```java
    Half half = Half.H1;
    int year = 0;
```
Explanation: This input is valid and boundary-case because the year 0 is a leap year in the proleptic Gregorian calendar, and it is the earliest year that can be represented by the `int` data type. This input tests the edge case where the year is at the lower limit of the `int` data type.

## New input2:
```java
    Half half = Half.H2;
    int year = 9999;
```
Explanation: This input is valid and boundary-case because the year 9999 is a leap year in the proleptic Gregorian calendar, and it is the upper limit of the `int` data type. This input tests the edge case where the year is at the upper limit of the `int` data type.

## New input3:
```java
    Half half = Half.H1;
    int year = 10000;
```
Explanation: This input is invalid because the year 10000 is not a leap year in the proleptic Gregorian calendar, and it exceeds the maximum value that can be represented by the `int` data type. This input tests the edge case where the year is beyond the maximum limit of the `int` data type.

## New input4:
```java
    Half half = Half.H2;
    int year = -1;
```
Explanation: This input is invalid because the year -1 is not a leap year in the proleptic Gregorian calendar, and it is the minimum value that can be represented by the `int` data type. This input tests the edge case where the year is at the lower limit of the `int` data type.

## New input5:
```java
    Half half = Half.H1;
    int year = -9999;
```
Explanation: This input is invalid because the year -9999 is not a leap year in the proleptic Gregorian calendar, and it is the lower limit of the `int` data type. This input tests the edge case where the year is at the lower limit of the `int` data type.
