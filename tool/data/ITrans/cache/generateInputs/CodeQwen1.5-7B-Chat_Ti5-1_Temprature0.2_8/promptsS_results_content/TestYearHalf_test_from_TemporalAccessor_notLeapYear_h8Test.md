## New input1:
```java
LocalDate date1 = LocalDate.of(2020, 6, 15);
```
Explanation: This input is valid because it represents a date in the middle of the second half of the year 2020, which is a leap year.

## New input2:
```java
LocalDate date2 = LocalDate.of(2021, 1, 1);
```
Explanation: This input is valid because it represents a date in the first half of the year 2021, which is not a leap year.

## New input3:
```java
LocalDate date3 = LocalDate.of(1900, 12, 31);
```
Explanation: This input is valid because it represents a date in the last day of the year 1900, which is not a leap year.

## New input4:
```java
LocalDate date4 = LocalDate.of(2000, 2, 29);
```
Explanation: This input is valid because it represents a date in February 29, 2000, which is a leap year.

## New input5:
```java
LocalDate date5 = LocalDate.of(2100, 2, 29);
```
Explanation: This input is valid because it represents a date in February 29, 2100, which is not a leap year.
