# ORIGINAL TEST CASE
```java
@Test
public void test_from_TemporalAccessor_notLeapYear() {
    LocalDate date = LocalDate.of(2007, 1, 1);
    int year = 2007;
    int expected = ((date.getMonthValue() - 1) / 6) + 1;
    YearHalf test = YearHalf.from(date);
    assertEquals(YearHalf.of(year, expected), test);
}

```
SOURCE INPUT: `date`
FOLLOW UP INPUT: `year`,`expected`


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


# NEW SOURCE INPUTS
## New source input0:
```java
LocalDate date = LocalDate.of(2020, 1, 1);
```

## New source input1:
```java
LocalDate date = LocalDate.of(2021, 12, 31);
```

## New source input2:
```java
LocalDate date = LocalDate.of(1900, 2, 28);
```

## New source input3:
```java
LocalDate date = LocalDate.of(2000, 2, 29);
```

## New source input4:
```java
LocalDate date = LocalDate.of(2022, 6, 15);
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    int year = 2007;
    int expected = ((date.getMonthValue() - 1) / 6) + 1;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.