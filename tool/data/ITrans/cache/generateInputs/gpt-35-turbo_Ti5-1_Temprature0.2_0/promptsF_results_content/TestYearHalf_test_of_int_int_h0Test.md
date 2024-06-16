## Inferred Relation
Based on the provided test case and the code under test, the inferred relation between the source input (`year`, `half`) and the follow-up input (`test2`) is as follows:

- The `year` and `half` values from the source input are used to create a `YearHalf` object using the `of` method.
- The `getHalfValue` method is called on the `test2` object to retrieve the half value.
- The retrieved half value should be equal to the `half` value from the source input.

## New input pair 0:
```java
    int year = Year.MIN_YEAR;
    int half = 1;
```
Follow-up input:
```java
    YearHalf test2 = YearHalf.of(year, half);
```
Explanation:
In this new input pair, the `year` is set to the minimum year value (`Year.MIN_YEAR`) and the `half` is set to 1. The follow-up input creates a `YearHalf` object using these values. Since the `half` value is 1, the `getHalfValue` method should return 1, which matches the `half` value from the source input.

## New input pair 1:
```java
    int year = Year.MAX_YEAR;
    int half = 2;
```
Follow-up input:
```java
    YearHalf test2 = YearHalf.of(year, half);
```
Explanation:
In this new input pair, the `year` is set to the maximum year value (`Year.MAX_YEAR`) and the `half` is set to 2. The follow-up input creates a `YearHalf` object using these values. Since the `half` value is 2, the `getHalfValue` method should return 2, which matches the `half` value from the source input.

## New input pair 2:
```java
    int year = 2022;
    int half = 1;
```
Follow-up input:
```java
    YearHalf test2 = YearHalf.of(year, half);
```
Explanation:
In this new input pair, the `year` is set to 2022 and the `half` is set to 1. The follow-up input creates a `YearHalf` object using these values. Since the `half` value is 1, the `getHalfValue` method should return 1, which matches the `half` value from the source input.

## New input pair 3:
```java
    int year = 2000;
    int half = 2;
```
Follow-up input:
```java
    YearHalf test2 = YearHalf.of(year, half);
```
Explanation:
In this new input pair, the `year` is set to 2000 and the `half` is set to 2. The follow-up input creates a `YearHalf` object using these values. Since the `half` value is 2, the `getHalfValue` method should return 2, which matches the `half` value from the source input.

## New input pair 4:
```java
    int year = 2023;
    int half = 2;
```
Follow-up input:
```java
    YearHalf test2 = YearHalf.of(year, half);
```
Explanation:
In this new input pair, the `year` is set to 2023 and the `half` is set to 2. The follow-up input creates a `YearHalf` object using these values. Since the `half` value is 2, the `getHalfValue` method should return 2, which matches the `half` value from the source input.