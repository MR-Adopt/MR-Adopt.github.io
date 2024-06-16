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


# TEST CASE
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


# OTHER INPUT PAIRS 
## Input pair1:
```java
int year1 = 2007;
int half1 = 2;
int year2 = 2012;
int year3 = 2012;
int half3 = 2;
```

## Input pair2:
```java
int year1 = 2000;
int half1 = 1;
int year2 = 2005;
int year3 = 2005;
int half3 = 1;
```

## Input pair3:
```java
int year1 = 2021;
int half1 = 2;
int year2 = 2022;
int year3 = 2022;
int half3 = 2;
```

## Input pair4:
```java
int year1 = 1990;
int half1 = 1;
int year2 = 1995;
int year3 = 1995;
int half3 = 1;
```

## Input pair5:
```java
int year1 = 2030;
int half1 = 2;
int year2 = 2035;
int year3 = 2035;
int half3 = 2;
```

## Input pair6:
```java
int year1 = 1985;
int half1 = 1;
int year2 = 1990;
int year3 = 1990;
int half3 = 1;
```

## Input pair7:
```java
int year1 = 1999;
int half1 = 1;
int year2 = 2000;
int year3 = 2000;
int half3 = 1;
```

## Input pair8:
```java
int year1 = 2022;
int half1 = 1;
int year2 = 2023;
int year3 = 2023;
int half3 = 1;
```

## Input pair9:
```java
int year1 = 1900;
int half1 = 2;
int year2 = 1901;
int year3 = 1901;
int half3 = 2;
```



# OUTPUT FORMAT
```java
public class TestYearHalf_test_withYear {
    public static List<Object> inputTransformation_test_withYear(int year1, int half1, int year2)  {
        // TODO
        int year3 = 
		int half3 = 
		List<Object> transformed_inputs = Arrays.asList(year3, half3);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.