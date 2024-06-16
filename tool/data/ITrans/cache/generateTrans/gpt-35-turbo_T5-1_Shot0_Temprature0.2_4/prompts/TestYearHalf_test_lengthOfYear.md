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
 * Returns the length of the year.
 * <p>
 * This returns the length of the year in days, either 365 or 366.
 *
 * @return 366 if the year is leap, 365 otherwise
 */
public int lengthOfYear() {
    return (isLeapYear() ? 366 : 365);
}

```


# TEST CASE
```java
@Test
public void test_lengthOfYear() {
    int year = 500;
    Half half = Half.H1;
    YearHalf test = YearHalf.of(year, half);
    YearHalf test2 = YearHalf.of(500, 1);
    assertEquals(Year.isLeap(year) ? 366 : 365, test2.lengthOfYear());
}

```
SOURCE INPUT: `year`,`half`
FOLLOW UP INPUT: `test2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
int year = 500;
Half half = Half.H1;
```

## Input pair2:
```java
int year = 2022;
Half half = Half.H2;
```

## Input pair3:
```java
int year = 9999;
Half half = Half.H2;
```

## Input pair4:
```java
int year = -100;
Half half = Half.H1;
```

## Input pair5:
```java
int year = 9999;
Half half = Half.H1;
```

## Input pair6:
```java
int year = 1582;
Half half = Half.H1;
```



# OUTPUT FORMAT
```java
public class TestYearHalf_test_lengthOfYear {
    public static YearHalf inputTransformation_test_lengthOfYear(int year, Half half)  {
        // TODO
        YearHalf test2 = 
		return test2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.