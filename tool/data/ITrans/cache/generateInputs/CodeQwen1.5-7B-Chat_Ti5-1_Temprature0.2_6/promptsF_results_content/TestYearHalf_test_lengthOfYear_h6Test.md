## New input pair0:
```java
    int year = 2020;
    Half half = Half.H2;
```
Follow-up input:
```java
    YearHalf test2 = YearHalf.of(2020, 2);
```
Explanation:
The inferred relation is that the length of the year is determined by the year and half-of-year. Since the year 2020 is a leap year, the length of the year is 366. Therefore, the follow-up input `test2` is constructed using the year 2020 and half-of-year 2, which satisfies the inferred relation.

## New input pair1:
```java
    int year = 1900;
    Half half = Half.H1;
```
Follow-up input:
```java
    YearHalf test2 = YearHalf.of(1900, 1);
```
Explanation:
The inferred relation is that the length of the year is determined by the year and half-of-year. Since the year 1900 is not a leap year, the length of the year is 365. Therefore, the follow-up input `test2` is constructed using the year 1900 and half-of-year 1, which satisfies the inferred relation.

## New input pair2:
```java
    int year = 2000;
    Half half = Half.H2;
```
Follow-up input:
```java
    YearHalf test2 = YearHalf.of(2000, 2);
```
Explanation:
The inferred relation is that the length of the year is determined by the year and half-of-year. Since the year 2000 is a leap year, the length of the year is 366. Therefore, the follow-up input `test2` is constructed using the year 2000 and half-of-year 2, which satisfies the inferred relation.

## New input pair3:
```java
    int year = 2100;
    Half half = Half.H1;
```
Follow-up input:
```java
    YearHalf test2 = YearHalf.of(2100, 1);
```
Explanation:
The inferred relation is that the length of the year is determined by the year and half-of-year. Since the year 2100 is not a leap year, the length of the year is 365. Therefore, the follow-up input `test2` is constructed using the year 2100 and half-of-year 1, which satisfies the inferred relation.

## New input pair4:
```java
    int year = 1800;
    Half half = Half.H2;
```
Follow-up input:
```java
    YearHalf test2 = YearHalf.of(1800, 2);
```
Explanation:
The inferred relation is that the length of the year is determined by the year and half-of-year. Since the year 1800 is not a leap year, the length of the year is 365. Therefore, the follow-up input `test2` is constructed using the year 1800 and half-of-year 2, which satisfies the inferred relation.
