# ORIGINAL TEST CASE
```java
@Test
public void test_HALF_YEARS() {
    int year1 = 2023;
    int quarter1 = 4;
    int year2 = 2023;
    int quarter2 = 2;
    int amount = 1;
    assertEquals(YearQuarter.of(year1, quarter1), HALF_YEARS.addTo(YearQuarter.of(year2, quarter2), amount));
}

```
TEST INPUT: `year1`,`quarter1`


# METHOD UNDER TEST
```java
/**
 * Obtains an instance of {@code YearQuarter} from a year and quarter.
 *
 * @param year  the year to represent, from MIN_YEAR to MAX_YEAR
 * @param quarter  the quarter-of-year to represent, from 1 to 4
 * @return the year-quarter, not null
 * @throws DateTimeException if either field value is invalid
 */
public static YearQuarter of(int year, int quarter) {
    YEAR.checkValidValue(year);
    return new YearQuarter(year, Quarter.of(quarter));
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `year1`,`quarter1`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    int year1 = 2023;
    int quarter1 = 4;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 