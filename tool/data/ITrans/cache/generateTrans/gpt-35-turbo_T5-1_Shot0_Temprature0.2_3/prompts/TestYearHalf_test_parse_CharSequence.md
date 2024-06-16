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
public void test_parse_CharSequence() {
    int year = 2012;
    int half = 2;
    CharSequence text = "2012-H2";
    assertEquals(YearHalf.of(year, half), YearHalf.parse(text));
}

```
SOURCE INPUT: `year`,`half`
FOLLOW UP INPUT: `text`


# OTHER INPUT PAIRS 
## Input pair1:
```java
int year = 2012;
int half = 2;
CharSequence text = "2012-H2";
```

## Input pair2:
```java
int year = 2020;
int half = 1;
CharSequence text = "2020-H1";
```

## Input pair3:
```java
int year = 1999;
int half = 2;
CharSequence text = "1999-H2";
```

## Input pair4:
```java
int year = 2025;
int half = 1;
CharSequence text = "2025-H1";
```

## Input pair5:
```java
int year = 2005;
int half = 2;
CharSequence text = "2005-H2";
```

## Input pair6:
```java
int year = 2030;
int half = 1;
CharSequence text = "2030-H1";
```

## Input pair7:
```java
int year = 2000;
int half = 2;
CharSequence text = "2000-H2";
```

## Input pair8:
```java
int year = 1990;
int half = 2;
CharSequence text = "1990-H2";
```

## Input pair9:
```java
int year = 2023;
int half = 1;
CharSequence text = "2023-H1";
```

## Input pair10:
```java
int year = 1980;
int half = 1;
CharSequence text = "1980-H1";
```

## Input pair11:
```java
int year = 2021;
int half = 2;
CharSequence text = "2021-H2";
```

## Input pair12:
```java
int year = 2000;
int half = 1;
CharSequence text = "2000-H1";
```

## Input pair13:
```java
int year = 2025;
int half = 2;
CharSequence text = "2025-H2";
```

## Input pair14:
```java
int year = 1999;
int half = 1;
CharSequence text = "1999-H1";
```



# OUTPUT FORMAT
```java
public class TestYearHalf_test_parse_CharSequence {
    public static CharSequence inputTransformation_test_parse_CharSequence(int year, int half)  {
        // TODO
        CharSequence text = 
		return text;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.