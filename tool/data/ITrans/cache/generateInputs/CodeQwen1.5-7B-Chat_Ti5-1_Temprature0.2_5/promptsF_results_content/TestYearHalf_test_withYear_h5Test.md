# REQUIRED DELIVERABLE
## New input pair0:
```java
    int year1 = 0;
    int half1 = 1;
    int year2 = 0;
    int year3 = 0;
    int half3 = 1;
```
### Explanation:
The inferred relation is that `YearHalf.of(year3, half3)` should be equal to `YearHalf.of(year1, half1).withYear(year2)`.
To satisfy this relation, we can set `year3` and `half3` to the same values as `year1` and `half1`, respectively. This ensures that the `withYear` method is called with the same year, and the resulting `YearHalf` object is equal to the original `YearHalf` object.

## New input pair1:
```java
    int year1 = 999999999;
    int half1 = 2;
    int year2 = 999999999;
    int year3 = 999999999;
    int half3 = 2;
```
### Explanation:
The inferred relation is that `YearHalf.of(year3, half3)` should be equal to `YearHalf.of(year1, half1).withYear(year2)`.
To satisfy this relation, we can set `year3` and `half3` to the same values as `year1` and `half1`, respectively. This ensures that the `withYear` method is called with the same year, and the resulting `YearHalf` object is equal to the original `YearHalf` object.

## New input pair2:
```java
    int year1 = 2000;
    int half1 = 1;
    int year2 = 2000;
    int year3 = 2000;
    int half3 = 1;
```
### Explanation:
The inferred relation is that `YearHalf.of(year3, half3)` should be equal to `YearHalf.of(year1, half1).withYear(year2)`.
To satisfy this relation, we can set `year3` and `half3` to the same values as `year1` and `half1`, respectively. This ensures that the `withYear` method is called with the same year, and the resulting `YearHalf` object is equal to the original `YearHalf` object.

## New input pair3:
```java
    int year1 = 2000;
    int half1 = 2;
    int year2 = 2000;
    int year3 = 2000;
    int half3 = 2;
```
### Explanation:
The inferred relation is that `YearHalf.of(year3, half3)` should be equal to `YearHalf.of(year1, half1).withYear(year2)`.
To satisfy this relation, we can set `year3` and `half3` to the same values as `year1` and `half1`, respectively. This ensures that the `withYear` method is called with the same year, and the resulting `YearHalf` object is equal to the original `YearHalf` object.

## New input pair4:
```java
    int year1 = 2000;
    int half1 = 3;
    int year2 = 2000;
    int year3 = 2000;
    int half3 = 3;
```
### Explanation:
The inferred relation is that `YearHalf.of(year3, half3)` should be equal to `YearHalf.of(year1, half1).withYear(year2)`.
To satisfy this relation, we can set `year3` and `half3` to the same values as `year1` and `half1`, respectively. This ensures that the `withYear` method is called with the same year, and the resulting `YearHalf` object is equal to the original `YearHalf` object.
