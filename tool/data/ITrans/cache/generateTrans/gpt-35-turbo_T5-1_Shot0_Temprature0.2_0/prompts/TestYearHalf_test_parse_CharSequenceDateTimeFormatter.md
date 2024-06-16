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


# TEST CASE
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
SOURCE INPUT: `text`,`f`
FOLLOW UP INPUT: `half`,`year`


# OTHER INPUT PAIRS 
## Input pair1:
```java
DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
CharSequence text = "H1 2012";
int year = 2012;
int half = 1;
```

## Input pair2:
```java
DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
CharSequence text = "H2 2020";
int year = 2020;
int half = 2;
```

## Input pair3:
```java
DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
CharSequence text = "H1 1999";
int year = 1999;
int half = 1;
```

## Input pair4:
```java
DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
CharSequence text = "H2 2022";
int year = 2022;
int half = 2;
```

## Input pair5:
```java
DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
CharSequence text = "H1 2005";
int year = 2005;
int half = 1;
```

## Input pair6:
```java
DateTimeFormatter f = new DateTimeFormatterBuilder().appendLiteral('H').appendValue(HALF_OF_YEAR, 1).appendLiteral(' ').appendValue(YEAR).toFormatter();
CharSequence text = "H2 2030";
int year = 2030;
int half = 2;
```



# OUTPUT FORMAT
```java
public class TestYearHalf_test_parse_CharSequenceDateTimeFormatter {
    public static List<Object> inputTransformation_test_parse_CharSequenceDateTimeFormatter(CharSequence text, DateTimeFormatter f)  {
        // TODO
        int half = 
		int year = 
		List<Object> transformed_inputs = Arrays.asList(half, year);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.