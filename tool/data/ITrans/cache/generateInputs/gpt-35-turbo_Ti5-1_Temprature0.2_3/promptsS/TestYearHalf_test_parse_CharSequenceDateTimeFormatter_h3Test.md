# ORIGINAL TEST CASE
```java
@Test
public void test_parse_CharSequenceDateTimeFormatter() {
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H1 2012";
    int year = 2012;
    int half = 1;
    assertEquals(YearHalf.parse(text, f), YearHalf.of(year, half));
}

```
TEST INPUT: `text`,`f`


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
 * Obtains an instance of {@code YearHalf} from a text string using a specific formatter.
 * <p>
 * The text is parsed using the formatter, returning a year-half.
 *
 * @param text  the text to parse, not null
 * @param formatter  the formatter to use, not null
 * @return the parsed year-half, not null
 * @throws DateTimeParseException if the text cannot be parsed
 */
public static YearHalf parse(CharSequence text, DateTimeFormatter formatter) {
    Objects.requireNonNull(formatter, "formatter");
    return formatter.parse(text, YearHalf::from);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `text`,`f`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
    CharSequence text = "H1 2012";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 