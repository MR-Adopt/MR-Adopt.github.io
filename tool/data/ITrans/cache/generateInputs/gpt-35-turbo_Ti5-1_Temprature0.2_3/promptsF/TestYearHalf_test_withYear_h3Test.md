# ORIGINAL TEST CASE
```java
@Test
public void test_withYear() {
    int year1 = 2007;
    int half1 = 2;
    int year2 = 2012;
    int year3 = 2012;
    int half3 = 2;
    assertEquals(YearHalf.of(year3, half3), YearHalf.of(year1, half1).withYear(year2));
}

```
SOURCE INPUT: `year1`,`half1`,`year2`
FOLLOW UP INPUT: `year3`,`half3`


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

```


# NEW SOURCE INPUTS
## New source input0:
```java
    int year1 = 2000;
    int half1 = 1;
    int year2 = 2005;
```

## New source input1:
```java
    int year1 = 2021;
    int half1 = 2;
    int year2 = 2022;
```

## New source input2:
```java
    int year1 = 1999;
    int half1 = 1;
    int year2 = 2000;
```

## New source input3:
```java
    int year1 = 2022;
    int half1 = 1;
    int year2 = 2023;
```

## New source input4:
```java
    int year1 = 1900;
    int half1 = 2;
    int year2 = 1901;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    int year1 = 2007;
    int half1 = 2;
    int year2 = 2012;
    int year3 = 2012;
    int half3 = 2;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.