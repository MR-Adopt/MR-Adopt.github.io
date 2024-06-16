# ORIGINAL TEST CASE
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


# NEW SOURCE INPUTS
## New source input0:
```java
    int year = 0;
    Half half = Half.H1;
```

## New source input1:
```java
    int year = 2022;
    Half half = Half.H2;
```

## New source input2:
```java
    int year = 9999;
    Half half = Half.H1;
```

## New source input3:
```java
    int year = 2000;
    Half half = Half.H2;
```

## New source input4:
```java
    int year = 2024;
    Half half = Half.H1;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    int year = 500;
    Half half = Half.H1;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.