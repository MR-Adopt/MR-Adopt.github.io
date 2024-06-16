## New input1:
```java
    int year1 = 0;
    int half1 = 1;
    int year2 = 0;
```
Explanation: This input is valid because the `YEAR` field in the `YearHalf` class is a `Year` object, which is a valid year from MIN_YEAR (1) to MAX_YEAR (999999999). The `Half` enum is also valid, with values 1 and 2 representing the first and second halves of the year, respectively.

## New input2:
```java
    int year1 = 999999999;
    int half1 = 2;
    int year2 = 999999999;
```
Explanation: This input is valid because the `YEAR` field in the `YearHalf` class is a `Year` object, which is a valid year from MIN_YEAR (1) to MAX_YEAR (999999999). The `Half` enum is also valid, with values 1 and 2 representing the first and second halves of the year, respectively.

## New input3:
```java
    int year1 = 2000;
    int half1 = 1;
    int year2 = 2000;
```
Explanation: This input is valid because the `YEAR` field in the `YearHalf` class is a `Year` object, which is a valid year from MIN_YEAR (1) to MAX_YEAR (999999999). The `Half` enum is also valid, with values 1 and 2 representing the first and second halves of the year, respectively.

## New input4:
```java
    int year1 = 2000;
    int half1 = 2;
    int year2 = 2000;
```
Explanation: This input is valid because the `YEAR` field in the `YearHalf` class is a `Year` object, which is a valid year from MIN_YEAR (1) to MAX_YEAR (999999999). The `Half` enum is also valid, with values 1 and 2 representing the first and second halves of the year, respectively.

## New input5:
```java
    int year1 = 2000;
    int half1 = 3;
    int year2 = 2000;
```
Explanation: This input is invalid because the `Half` enum only has values 1 and 2, and there is no third half of the year.
