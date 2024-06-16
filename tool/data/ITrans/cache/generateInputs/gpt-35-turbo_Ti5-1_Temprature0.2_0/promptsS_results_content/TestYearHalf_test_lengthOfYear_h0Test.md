## New input1:
```java
    int year = 0;
    Half half = Half.H1;
```
Explanation: This input is valid because the minimum value for the year is MIN_YEAR, which is defined in the code but not shown here. By setting the year to 0, we are testing the boundary case where the year is at its minimum value.

## New input2:
```java
    int year = 2022;
    Half half = Half.H2;
```
Explanation: This input is valid because the year is within the valid range of MIN_YEAR to MAX_YEAR. By setting the year to 2022 and the half to H2, we are testing a normal case where the year is not a leap year.

## New input3:
```java
    int year = 2000;
    Half half = Half.H1;
```
Explanation: This input is valid because the year is within the valid range of MIN_YEAR to MAX_YEAR. By setting the year to 2000 and the half to H1, we are testing a normal case where the year is a leap year.

## New input4:
```java
    int year = 9999;
    Half half = Half.H2;
```
Explanation: This input is valid because the year is within the valid range of MIN_YEAR to MAX_YEAR. By setting the year to 9999 and the half to H2, we are testing the boundary case where the year is at its maximum value.

## New input5:
```java
    int year = -100;
    Half half = Half.H1;
```
Explanation: This input is valid because the year is within the valid range of MIN_YEAR to MAX_YEAR. By setting the year to -100 and the half to H1, we are testing a negative value for the year.