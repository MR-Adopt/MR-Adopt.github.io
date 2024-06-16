# ORIGINAL TEST CASE
```java
@Test
public void test_of_int_int() {
    int year = 100;
    int half = 1;
    int year2 = 100;
    int half2 = 1;
    YearHalf test = YearHalf.of(year, half);
    YearHalf test2 = YearHalf.of(year2, half2);
    assertEquals(year, test.getYear());
    assertEquals(half, test2.getHalfValue());
    assertEquals(Half.of(half), test.getHalf());
    assertEquals(test, YearHalf.of(year, half));
    assertEquals(test.hashCode(), YearHalf.of(year, half).hashCode());
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
 * Gets the half-of-year field from 1 to 2.
 * <p>
 * This method returns the half as an {@code int} from 1 to 2.
 * Application code is frequently clearer if the enum {@link Half}
 * is used by calling {@link #getHalf()}.
 *
 * @return the half-of-year, from 1 to 2
 * @see #getHalf()
 */
public int getHalfValue() {
    return half.getValue();
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `year`,`half`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    int year = 100;
    int half = 1;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 