## New input1:
```java
    int year = 2020;
    Half half = Half.H2;
```
Explanation: This input is valid because the year 2020 is a leap year, and the half-of-year 2 is valid.

## New input2:
```java
    int year = 1900;
    Half half = Half.H1;
```
Explanation: This input is valid because the year 1900 is not a leap year, and the half-of-year 1 is valid.

## New input3:
```java
    int year = 0;
    Half half = Half.H2;
```
Explanation: This input is valid because the year 0 is not a leap year, and the half-of-year 2 is valid.

## New input4:
```java
    int year = 9999;
    Half half = Half.H1;
```
Explanation: This input is valid because the year 9999 is not a leap year, and the half-of-year 1 is valid.

## New input5:
```java
    int year = 10000;
    Half half = Half.H2;
```
Explanation: This input is valid because the year 10000 is not a leap year, and the half-of-year 2 is valid.
