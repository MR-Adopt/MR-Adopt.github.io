## New input1:
```java
    int year = 0;
    Half half = Half.H1;
```
Explanation: This input is valid because the minimum value for the `year` parameter is `MIN_YEAR`, which is 0.

## New input2:
```java
    int year = 2022;
    Half half = Half.H2;
```
Explanation: This input is valid because the `year` parameter is within the valid range from `MIN_YEAR` to `MAX_YEAR`, and the `half` parameter is set to `H2`, which represents the second half of the year.

## New input3:
```java
    int year = 9999;
    Half half = Half.H1;
```
Explanation: This input is valid because the `year` parameter is within the valid range from `MIN_YEAR` to `MAX_YEAR`, and the `half` parameter is set to `H1`, which represents the first half of the year.

## New input4:
```java
    int year = 2000;
    Half half = Half.H2;
```
Explanation: This input is valid because the `year` parameter is within the valid range from `MIN_YEAR` to `MAX_YEAR`, and the `half` parameter is set to `H2`, which represents the second half of the year.

## New input5:
```java
    int year = 2024;
    Half half = Half.H1;
```
Explanation: This input is valid because the `year` parameter is within the valid range from `MIN_YEAR` to `MAX_YEAR`, and the `half` parameter is set to `H1`, which represents the first half of the year. Additionally, the `year` value is a leap year, so it will have 366 days.