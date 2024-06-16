## New input1:
```java
    Half half = Half.H1;
    int year = Year.MIN_VALUE;
```
Explanation: This input is valid because it tests the minimum value for the year input. The `Year.MIN_VALUE` represents the minimum value that can be assigned to a year.

## New input2:
```java
    Half half = Half.H2;
    int year = 2021;
```
Explanation: This input is valid because it tests a recent year (2021) with the second half of the year (Half.H2). It covers a common scenario where the year is not a leap year.

## New input3:
```java
    Half half = Half.H1;
    int year = 2000;
```
Explanation: This input is valid because it tests a leap year (2000) with the first half of the year (Half.H1). It covers a scenario where the year is divisible by 400, making it a leap year.

## New input4:
```java
    Half half = Half.H2;
    int year = 1600;
```
Explanation: This input is valid because it tests a leap year (1600) with the second half of the year (Half.H2). It covers a scenario where the year is divisible by 400, making it a leap year.

## New input5:
```java
    Half half = Half.H1;
    int year = 2024;
```
Explanation: This input is valid because it tests a leap year (2024) with the first half of the year (Half.H1). It covers a scenario where the year is divisible by 4 but not by 100, making it a leap year.