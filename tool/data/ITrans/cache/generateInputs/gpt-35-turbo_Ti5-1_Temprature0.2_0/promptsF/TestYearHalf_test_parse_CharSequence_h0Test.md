# ORIGINAL TEST CASE
```java
@Test
public void test_parse_CharSequence() {
    int year = 2012;
    int half = 2;
    CharSequence text = "2012-H2";
    assertEquals(YearHalf.of(year, half), YearHalf.parse(text));
}

```
SOURCE INPUT: `year`,`half`
FOLLOW UP INPUT: `text`


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


# NEW SOURCE INPUTS
## New source input0:
```java
    int year = 2020;
    int half = 1;
```

## New source input1:
```java
    int year = 1999;
    int half = 2;
```

## New source input2:
```java
    int year = 2025;
    int half = 1;
```

## New source input3:
```java
    int year = 2005;
    int half = 2;
```

## New source input4:
```java
    int year = 2030;
    int half = 1;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    int year = 2012;
    int half = 2;
    CharSequence text = "2012-H2";
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.