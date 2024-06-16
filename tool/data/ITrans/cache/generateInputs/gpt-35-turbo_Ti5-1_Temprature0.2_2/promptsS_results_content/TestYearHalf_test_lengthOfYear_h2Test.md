## New input1:
```java
    int year = 0;
    Half half = Half.H1;
```
Explanation: This input is valid because the minimum value for the `year` parameter is `MIN_YEAR`, which is defined in the code but not shown here. In this case, `MIN_YEAR` is assumed to be 0.

## New input2:
```java
    int year = 2022;
    Half half = Half.H2;
```
Explanation: This input is valid because the `year` parameter falls within the valid range of `MIN_YEAR` to `MAX_YEAR`, which is not shown in the code but assumed to be defined. In this case, `MIN_YEAR` and `MAX_YEAR` are assumed to be 0 and 9999 respectively.

## New input3:
```java
    int year = 2024;
    Half half = Half.H1;
```
Explanation: This input is valid because the `year` parameter falls within the valid range of `MIN_YEAR` to `MAX_YEAR`, and the `half` parameter is set to `Half.H1`, which is a valid value according to the code.

## New input4:
```java
    int year = 2021;
    Half half = Half.H2;
```
Explanation: This input is valid because the `year` parameter falls within the valid range of `MIN_YEAR` to `MAX_YEAR`, and the `half` parameter is set to `Half.H2`, which is a valid value according to the code.

## New input5:
```java
    int year = 9999;
    Half half = Half.H2;
```
Explanation: This input is valid because the `year` parameter falls within the valid range of `MIN_YEAR` to `MAX_YEAR`, and the `half` parameter is set to `Half.H2`, which is a valid value according to the code. Additionally, `MAX_YEAR` is assumed to be 9999 in this case.