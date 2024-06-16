## New input pair0:
```java
    Half half = Half.H2;
    int year = 2000;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## New input pair1:
```java
    Half half = Half.H1;
    int year = 1900;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## New input pair2:
```java
    Half half = Half.H2;
    int year = 1904;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## New input pair3:
```java
    Half half = Half.H1;
    int year = 2100;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## New input pair4:
```java
    Half half = Half.H2;
    int year = 2400;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## Explanation:
The inferred relation between the source input and the follow-up input is that the `YearHalf` object created from the source input should have the same leap year status as the result of calling the `Year.isLeap()` method with the same year.

For example, if the source input is `year = 2000` and `half = Half.H2`, then the `YearHalf` object created from this input should have the same leap year status as the result of calling `Year.isLeap(2000)`. Similarly, for other source inputs, the `YearHalf` object created from these inputs should have the same leap year status as the result of calling `Year.isLeap()` with the corresponding year.

The code used to generate the follow-up input for each new source input is as follows:
- For `year = 2000` and `half = Half.H2`, the follow-up input is `YearHalf.of(2000, Half.H2)`.
- For `year = 1900` and `half = Half.H1`, the follow-up input is `YearHalf.of(1900, Half.H1)`.
- For `year = 1904` and `half = Half.H2`, the follow-up input is `YearHalf.of(1904, Half.H2)`.
- For `year = 2100` and `half = Half.H1`, the follow-up input is `YearHalf.of(2100, Half.H1)`.
- For `year = 2400` and `half = Half.H2`, the follow-up input is `YearHalf.of(2400, Half.H2)`.

The assertions in the original test case are used to verify that the `YearHalf` object created from the source input has the same leap year status as the result of calling the `Year.isLeap()` method with the same year.
