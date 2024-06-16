## New input1:
```java
    int year = 0;
    int half = 1;
```
Explanation: This input is valid because the year 0 is within the valid range of the year field in the YearHalf class. The half-of-year field can be 1 or 2, which is also within the valid range. This input tests the edge case where the year is at the minimum valid value.

## New input2:
```java
    int year = 9999;
    int half = 2;
```
Explanation: This input is valid because the year 9999 is within the valid range of the year field in the YearHalf class. The half-of-year field can be 1 or 2, which is also within the valid range. This input tests the edge case where the year is at the maximum valid value.

## New input3:
```java
    int year = 5000;
    int half = 1;
```
Explanation: This input is valid because the year 5000 is within the valid range of the year field in the YearHalf class. The half-of-year field can be 1 or 2, which is also within the valid range. This input tests the middle case where the year is in the middle of the valid range.

## New input4:
```java
    int year = -1;
    int half = 2;
```
Explanation: This input is valid because the year -1 is within the valid range of the year field in the YearHalf class. The half-of-year field can be 1 or 2, which is also within the valid range. This input tests the edge case where the year is at the minimum valid value.

## New input5:
```java
    int year = 10000;
    int half = 1;
```
Explanation: This input is not valid because the year 10000 is outside the valid range of the year field in the YearHalf class. The half-of-year field can be 1 or 2, which is also within the valid range. This input tests the edge case where the year is at the maximum valid value plus one.
