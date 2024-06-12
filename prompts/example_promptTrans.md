# Task Description
<SYSTEM MESSAGE: START>
As an expert in Java programming, you excel at understanding the intentions behind code and developing functions that convert provided inputs into desired outputs.
In metamorphic testing, input transformation functions are crafted to automatically generate additional test inputs (denoted as 'FOLLOW UP INPUT') from initial test inputs (denoted as 'SOURCE INPUT') based on defined metamorphic relations (MRs).

Given the program under test (denoted as 'METHOD UNDER TEST'), an MR-encoded test case (denoted as 'TEST CASE'),
and additional pairs of 'SOURCE INPUT' and 'FOLLOW UP INPUT' (denoted as 'OTHER INPUT PAIRS'),\
your task is to analyze the program under test and the provided test case, deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.

The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Considering potential input pairs with boundary values as well.
<SYSTEM MESSAGE: END>


# METHOD UNDER TEST
```java
public static Date toMediumDate(String string) {
    if (StringUtils.isEmpty(dateString)) {
      return null;
    }
    try {
      return formatter.parseDateTime (dateString). toDate();
    } catch (IllegalInstantException e) {
      return formatter.parseLocalDateTime(dateString). toDate();
    }
}
```


# TEST CASE
```java
  @Test
  void testToMediumDate() {
    Date dateA = new DateTime("2024-01-01 00:00:00").toDate();
    Date dateB = new DateTime("2024-01-02 00:00:00").toDate();
    Date mediumDateA = DateUtils.toMediumDate(dateA);
    Date mediumDateB = DateUtils.toMediumDate(dateB);
    assertThat(mediumDateB, is(plusOneDay(mediumDateA)));
  }
```
SOURCE INPUT: `dateA = new DateTime("2024-01-01 00:00:00").toDate();`
FOLLOW UP INPUT: `dateB = new DateTime("2024-01-02 00:00:00").toDate();`


# OTHER INPUT PAIRS 
## New input pair1:
```java
    Date dateA = new DateTime("2024-12-31 23:59:59").toDate();
    Date dateB = new DateTime("2025-01-01 23:59:59").toDate();
```

## New input pair2:
```java
    Date dateA = new DateTime("2024-06-15 12:30:00").toDate();
    Date dateB = new DateTime("2024-06-16 12:30:00").toDate();
```

## New input pair3:
```java
    Date dateA = new DateTime("2024-02-29 00:00:00").toDate();
    Date dateB = new DateTime("2024-03-01 00:00:00").toDate();
```

## New input pair4:
```java
    Date dateA = new DateTime("2024-03-01 00:00:00").toDate();
    Date dateB = new DateTime("2024-03-02 00:00:00").toDate();
```


# OUTPUT FORMAT
```java
public class testToMediumDate {
    public static Date inputransformation_testToMediumDate(Date dateA) {
        // TODO
        Date dateB = 
        return dateB;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.