## New input1:
```java
    Half half = Half.H1;
    int year = Year.MIN_VALUE;
```
This input is valid because it tests the minimum valid value for the `year` parameter. The `Year.MIN_VALUE` represents the minimum supported year value in the ISO calendar system.

## New input2:
```java
    Half half = Half.H2;
    int year = 2021;
```
This input is valid because it tests a recent year value (2021) with the second half of the year (Half.H2). It covers a common scenario where the year is not a leap year.

## New input3:
```java
    Half half = Half.H1;
    int year = 2000;
```
This input is valid because it tests a leap year (2000) with the first half of the year (Half.H1). It covers a scenario where the year is divisible by 400, making it a leap year according to the ISO calendar system.

## New input4:
```java
    Half half = Half.H2;
    int year = 1600;
```
This input is valid because it tests a leap year (1600) with the second half of the year (Half.H2). It covers a scenario where the year is divisible by 400, making it a leap year according to the ISO calendar system.

## New input5:
```java
    Half half = Half.H1;
    int year = Year.MAX_VALUE;
```
This input is valid because it tests the maximum valid value for the `year` parameter. The `Year.MAX_VALUE` represents the maximum supported year value in the ISO calendar system.