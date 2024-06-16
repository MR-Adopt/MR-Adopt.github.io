# ORIGINAL TEST CASE
```java
@Test
public void test_isLeapYear_int() {
    Half half = Half.H1;
    int year = 500;
    YearHalf test = YearHalf.of(year, half);
    int year2 = 500;
    int halfValue = 1;
    YearHalf test2 = YearHalf.of(year2, halfValue);
    assertEquals(Year.isLeap(year), test2.isLeapYear());
}

```
SOURCE INPUT: `year`,`half`
FOLLOW UP INPUT: `test2`


# METHOD UNDER TEST
```java
/**
 * Obtains an instance of {@code YearHalf} from a year and half.
 *
 * @param year  the year to represent, from MIN_YEAR to MAX_YEAR
 * @param half  the half-of-year to represent, from 1 to 2
 * @return the year-half, not null
 * @throws DateTimeException if either field value is invalid
 */
public static YearHalf of(int year, int half) {
    YEAR.checkValidValue(year);
    return new YearHalf(year, Half.of(half));
}

// -----------------------------------------------------------------------
/**
 * Checks if the year is a leap year, according to the ISO proleptic
 * calendar system rules.
 * <p>
 * This method applies the current rules for leap years across the whole time-line.
 * In general, a year is a leap year if it is divisible by four without
 * remainder. However, years divisible by 100, are not leap years, with
 * the exception of years divisible by 400 which are.
 * <p>
 * For example, 1904 is a leap year it is divisible by 4.
 * 1900 was not a leap year as it is divisible by 100, however 2000 was a
 * leap year as it is divisible by 400.
 * <p>
 * The calculation is proleptic - applying the same rules into the far future and far past.
 * This is historically inaccurate, but is correct for the ISO-8601 standard.
 *
 * @return true if the year is leap, false otherwise
 */
public boolean isLeapYear() {
    return IsoChronology.INSTANCE.isLeapYear(year);
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    Half half = Half.H1;
    int year = 0;
```

## New source input1:
```java
    Half half = Half.H2;
    int year = 2021;
```

## New source input2:
```java
    Half half = Half.H1;
    int year = 2000;
```

## New source input3:
```java
    Half half = Half.H2;
    int year = 1900;
```

## New source input4:
```java
    Half half = Half.H1;
    int year = 9999;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    Half half = Half.H1;
    int year = 500;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.