## New input1:
```java
    Half half = Half.H2;
    int year = 2000;
```
Explanation: This input is valid because it tests the edge case where the year is a leap year and the half is the second half of the year.

## New input2:
```java
    Half half = Half.H1;
    int year = 1900;
```
Explanation: This input is valid because it tests the edge case where the year is not a leap year and the half is the first half of the year.

## New input3:
```java
    Half half = Half.H2;
    int year = 1901;
```
Explanation: This input is valid because it tests the case where the year is not a leap year but the half is the second half of the year.

## New input4:
```java
    Half half = Half.H1;
    int year = 2100;
```
Explanation: This input is valid because it tests the case where the year is not a leap year but the half is the first half of the year.

## New input5:
```java
    Half half = Half.H2;
    int year = 2101;
```
Explanation: This input is valid because it tests the case where the year is not a leap year but the half is the second half of the year.
