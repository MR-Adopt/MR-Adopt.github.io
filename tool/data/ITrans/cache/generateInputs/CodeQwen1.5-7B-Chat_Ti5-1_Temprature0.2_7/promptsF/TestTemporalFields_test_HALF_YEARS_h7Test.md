# ORIGINAL TEST CASE
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


# NEW SOURCE INPUTS
## New source input0:
```java
    int year1 = 2023;
    int quarter1 = 1;
```

## New source input1:
```java
    int year1 = 2023;
    int quarter1 = 2;
```

## New source input2:
```java
    int year1 = 2023;
    int quarter1 = 3;
```

## New source input3:
```java
    int year1 = 2023;
    int quarter1 = 4;
```

## New source input4:
```java
    int year1 = 2023;
    int quarter1 = 5;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    int year1 = 2023;
    int quarter1 = 4;
    int year2 = 2023;
    int quarter2 = 2;
    int amount = 1;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.