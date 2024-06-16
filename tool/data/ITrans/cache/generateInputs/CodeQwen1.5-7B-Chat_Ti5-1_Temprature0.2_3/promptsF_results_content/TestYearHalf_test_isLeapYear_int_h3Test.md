## New input pair0:
```java
    Half half = Half.H1;
    int year = 0;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## New input pair1:
```java
    Half half = Half.H2;
    int year = 9999;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## New input pair2:
```java
    Half half = Half.H1;
    int year = 10000;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## New input pair3:
```java
    Half half = Half.H2;
    int year = -1;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## New input pair4:
```java
    Half half = Half.H1;
    int year = -9999;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

Explanation:
The inferred relation is that the `isLeapYear()` method of the `YearHalf` class should return the same value as the `Year.isLeap()` method for the given year. Therefore, for each new source input, we create a corresponding `YearHalf` object and call the `isLeapYear()` method on it, and assert that it returns the same value as the `Year.isLeap()` method for the given year.
