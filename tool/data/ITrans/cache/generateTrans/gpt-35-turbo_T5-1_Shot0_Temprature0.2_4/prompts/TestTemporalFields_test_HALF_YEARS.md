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


# TEST CASE
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
SOURCE INPUT: `year1`,`quarter1`
FOLLOW UP INPUT: `year2`,`quarter2`,`amount`


# OTHER INPUT PAIRS 



# OUTPUT FORMAT
```java
public class TestTemporalFields_test_HALF_YEARS {
    public static List<Object> inputTransformation_test_HALF_YEARS(int year1, int quarter1)  {
        // TODO
        int year2 = 
		int quarter2 = 
		int amount = 
		List<Object> transformed_inputs = Arrays.asList(year2, quarter2, amount);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.