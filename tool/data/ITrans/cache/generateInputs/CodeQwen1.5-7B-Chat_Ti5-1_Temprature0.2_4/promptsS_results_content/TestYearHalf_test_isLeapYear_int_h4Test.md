## New input1:
```java
    Half half = Half.H1;
    int year = 0;
```
Explanation: Year 0 is a leap year according to the proleptic Gregorian calendar. This input tests the edge case where the year is at the minimum possible value.

## New input2:
```java
    Half half = Half.H2;
    int year = 9999;
```
Explanation: Year 9999 is not a leap year according to the proleptic Gregorian calendar. This input tests the edge case where the year is at the maximum possible value.

## New input3:
```java
    Half half = Half.H1;
    int year = 10000;
```
Explanation: Year 10000 is not a leap year according to the proleptic Gregorian calendar. This input tests the edge case where the year is beyond the maximum possible value.

## New input4:
```java
    Half half = Half.H2;
    int year = -1;
```
Explanation: Year -1 is not a leap year according to the proleptic Gregorian calendar. This input tests the edge case where the year is at the minimum possible negative value.

## New input5:
```java
    Half half = Half.H1;
    int year = -10000;
```
Explanation: Year -10000 is not a leap year according to the proleptic Gregorian calendar. This input tests the edge case where the year is beyond the minimum possible negative value.
