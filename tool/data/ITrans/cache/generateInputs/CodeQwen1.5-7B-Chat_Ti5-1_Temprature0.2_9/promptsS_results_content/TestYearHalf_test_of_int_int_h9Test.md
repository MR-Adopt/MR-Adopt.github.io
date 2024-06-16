## New input1:
```java
    int year = 0;
    int half = 1;
```
Explanation: This input is valid because the year 0 is a valid year according to the range of valid years in the `YEAR` field. The half-of-year 1 is also a valid value.

## New input2:
```java
    int year = 9999;
    int half = 2;
```
Explanation: This input is valid because the year 9999 is a valid year according to the range of valid years in the `YEAR` field. The half-of-year 2 is also a valid value.

## New input3:
```java
    int year = -1;
    int half = 1;
```
Explanation: This input is valid because the year -1 is a valid year according to the range of valid years in the `YEAR` field. The half-of-year 1 is also a valid value.

## New input4:
```java
    int year = 10000;
    int half = 1;
```
Explanation: This input is invalid because the year 10000 is not a valid year according to the range of valid years in the `YEAR` field.

## New input5:
```java
    int year = 100;
    int half = 3;
```
Explanation: This input is invalid because the half-of-year 3 is not a valid value.
