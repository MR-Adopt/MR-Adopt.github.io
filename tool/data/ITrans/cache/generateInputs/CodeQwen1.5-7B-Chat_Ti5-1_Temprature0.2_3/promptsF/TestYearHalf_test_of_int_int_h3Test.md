# ORIGINAL TEST CASE
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


# NEW SOURCE INPUTS
## New source input0:
```java
    int year = Year.MAX_VALUE;
    int half = 2;
```

## New source input1:
```java
    int year = Year.MIN_VALUE;
    int half = 1;
```

## New source input2:
```java
    int year = 0;
    int half = 1;
```

## New source input3:
```java
    int year = 0;
    int half = 2;
```

## New source input4:
```java
    int year = 100;
    int half = 2;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    int year = 100;
    int half = 1;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.