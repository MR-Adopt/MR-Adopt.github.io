## New input1:
```java
    Half half = Half.H1;
    int year = Year.MIN_VALUE;
```
This input is valid because it tests the minimum possible value for the `year` parameter.

## New input2:
```java
    Half half = Half.H2;
    int year = 2000;
```
This input is valid because it tests a leap year (divisible by 4) with the second half of the year.

## New input3:
```java
    Half half = Half.H1;
    int year = 2021;
```
This input is valid because it tests a non-leap year (not divisible by 4) with the first half of the year.

## New input4:
```java
    Half half = Half.H2;
    int year = 2024;
```
This input is valid because it tests a leap year (divisible by 4) with the second half of the year.

## New input5:
```java
    Half half = Half.H1;
    int year = Year.MAX_VALUE;
```
This input is valid because it tests the maximum possible value for the `year` parameter.