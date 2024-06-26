# METHOD UNDER TEST
```java
// -----------------------------------------------------------------------
/**
 * Obtains an instance of {@code YearHalf} from a temporal object.
 * <p>
 * This obtains a year-half based on the specified temporal.
 * A {@code TemporalAccessor} represents an arbitrary set of date and time information,
 * which this factory converts to an instance of {@code YearHalf}.
 * <p>
 * The conversion extracts the {@link ChronoField#YEAR YEAR} and
 * {@link TemporalFields#HALF_OF_YEAR HALF_OF_YEAR} fields.
 * The extraction is only permitted if the temporal object has an ISO
 * chronology, or can be converted to a {@code LocalDate}.
 * <p>
 * This method matches the signature of the functional interface {@link TemporalQuery}
 * allowing it to be used in queries via method reference, {@code YearHalf::from}.
 *
 * @param temporal  the temporal object to convert, not null
 * @return the year-half, not null
 * @throws DateTimeException if unable to convert to a {@code YearHalf}
 */
public static YearHalf from(TemporalAccessor temporal) {
    if (temporal instanceof YearHalf) {
        return (YearHalf) temporal;
    }
    Objects.requireNonNull(temporal, "temporal");
    try {
        TemporalAccessor adjusted = !IsoChronology.INSTANCE.equals(Chronology.from(temporal)) ? LocalDate.from(temporal) : temporal;
        // need to use getLong() as JDK Parsed class get() doesn't work properly
        int year = Math.toIntExact(adjusted.getLong(YEAR));
        int hoy = Math.toIntExact(adjusted.getLong(HALF_OF_YEAR));
        return of(year, hoy);
    } catch (DateTimeException ex) {
        throw new DateTimeException("Unable to obtain YearHalf from TemporalAccessor: " + temporal + " of type " + temporal.getClass().getName(), ex);
    }
}

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


# TEST CASE
```java
@Test
public void test_from_TemporalAccessor_leapYear() {
    LocalDate date = LocalDate.of(2008, 1, 1);
    int year = 2008;
    int expected = ((date.getMonthValue() - 1) / 6) + 1;
    YearHalf test = YearHalf.from(date);
    assertEquals(YearHalf.of(year, expected), test);
}

```
SOURCE INPUT: `date`
FOLLOW UP INPUT: `year`,`expected`


# OTHER INPUT PAIRS 



# OUTPUT FORMAT
```java
public class TestYearHalf_test_from_TemporalAccessor_leapYear {
    public static List<Object> inputTransformation_test_from_TemporalAccessor_leapYear(LocalDate date)  {
        // TODO
        int year = 
		int expected = 
		List<Object> transformed_inputs = Arrays.asList(year, expected);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.