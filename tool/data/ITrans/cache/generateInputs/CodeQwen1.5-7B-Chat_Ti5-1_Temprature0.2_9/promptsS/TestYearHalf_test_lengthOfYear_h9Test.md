# ORIGINAL TEST CASE
```java
@Test
public void test_lengthOfYear() {
    int year = 500;
    Half half = Half.H1;
    YearHalf test = YearHalf.of(year, half);
    YearHalf test2 = YearHalf.of(500, 1);
    assertEquals(Year.isLeap(year) ? 366 : 365, test2.lengthOfYear());
}

```
TEST INPUT: `year`,`half`


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

/**
 * Returns the length of the year.
 * <p>
 * This returns the length of the year in days, either 365 or 366.
 *
 * @return 366 if the year is leap, 365 otherwise
 */
public int lengthOfYear() {
    return (isLeapYear() ? 366 : 365);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `year`,`half`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    int year = 500;
    Half half = Half.H1;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 