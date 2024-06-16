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


# TEST CASE
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


# OTHER INPUT PAIRS 



# OUTPUT FORMAT
```java
public class TestYearHalf_test_isLeapYear_int {
    public static YearHalf inputTransformation_test_isLeapYear_int(int year, Half half)  {
        // TODO
        YearHalf test2 = 
		return test2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.