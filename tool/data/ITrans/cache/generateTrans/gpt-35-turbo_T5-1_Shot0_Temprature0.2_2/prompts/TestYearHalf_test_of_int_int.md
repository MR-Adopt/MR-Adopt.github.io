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
 * Gets the half-of-year field from 1 to 2.
 * <p>
 * This method returns the half as an {@code int} from 1 to 2.
 * Application code is frequently clearer if the enum {@link Half}
 * is used by calling {@link #getHalf()}.
 *
 * @return the half-of-year, from 1 to 2
 * @see #getHalf()
 */
public int getHalfValue() {
    return half.getValue();
}

```


# TEST CASE
```java
@Test
public void test_of_int_int() {
    int year = 100;
    int half = 1;
    int year2 = 100;
    int half2 = 1;
    YearHalf test = YearHalf.of(year, half);
    YearHalf test2 = YearHalf.of(year2, half2);
    assertEquals(year, test.getYear());
    assertEquals(half, test2.getHalfValue());
    assertEquals(Half.of(half), test.getHalf());
    assertEquals(test, YearHalf.of(year, half));
    assertEquals(test.hashCode(), YearHalf.of(year, half).hashCode());
}

```
SOURCE INPUT: `year`,`half`
FOLLOW UP INPUT: `test2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
int year = 100;
int half = 1;
```

## Input pair2:
```java
int year = 2022;
int half = 1;
YearHalf test2 = YearHalf.of(year, half);
```

## Input pair3:
```java
int year = 2023;
int half = 2;
YearHalf test2 = YearHalf.of(year, half);
```

## Input pair4:
```java
int year = 2000;
int half = 2;
YearHalf test2 = YearHalf.of(year, half);
```

## Input pair5:
```java
int year = 0;
int half = 1;
YearHalf test2 = YearHalf.of(year, half);
```

## Input pair6:
```java
int year = 9999;
int half = 2;
YearHalf test2 = YearHalf.of(year, half);
```

## Input pair7:
```java
int year = 2024;
int half = 2;
YearHalf test2 = YearHalf.of(year, half);
```



# OUTPUT FORMAT
```java
public class TestYearHalf_test_of_int_int {
    public static YearHalf inputTransformation_test_of_int_int(int year, int half)  {
        // TODO
        YearHalf test2 = 
		return test2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.