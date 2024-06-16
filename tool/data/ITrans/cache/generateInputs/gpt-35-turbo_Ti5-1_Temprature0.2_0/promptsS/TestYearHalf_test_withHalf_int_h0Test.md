# ORIGINAL TEST CASE
```java
@Test
public void test_withHalf_int() {
    int year1 = 2007;
    int half1 = 2;
    int half2 = 1;
    int year3 = 2007;
    int half3 = 1;
    assertEquals(YearHalf.of(year3, half3), YearHalf.of(year1, half1).withHalf(half2));
}

```
TEST INPUT: `year1`,`half1`,`half2`


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

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `year1`,`half1`,`half2`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    int year1 = 2007;
    int half1 = 2;
    int half2 = 1;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 