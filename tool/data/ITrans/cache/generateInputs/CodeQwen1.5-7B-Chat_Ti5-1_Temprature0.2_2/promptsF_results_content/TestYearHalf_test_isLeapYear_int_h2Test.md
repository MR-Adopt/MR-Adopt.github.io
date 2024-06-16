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
    int year = 1000;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## New input pair2:
```java
    Half half = Half.H1;
    int year = 4000;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## New input pair3:
```java
    Half half = Half.H2;
    int year = 5000;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

## New input pair4:
```java
    Half half = Half.H1;
    int year = -1;
    YearHalf test = YearHalf.of(year, half);
    assertEquals(Year.isLeap(year), test.isLeapYear());
```

Explanation:
The inferred relation between the source input and the follow-up input is that the source input `year` and `half` are used to create an instance of `YearHalf` using the `of` method. The follow-up input `test` is created by calling the `of` method with the same `year` and `half` values. The assertions in the original test case check if the year is a leap year, which is determined by calling the `isLeapYear` method on the `YearHalf` instance. The new input pairs satisfy this relation by using the same `year` and `half` values to create the `YearHalf` instance and then checking if the year is a leap year.
