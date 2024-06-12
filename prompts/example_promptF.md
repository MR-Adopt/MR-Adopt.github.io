# Task Description
<SYSTEM MESSAGE: START>
As an expert in Java programming, you are good at understanding code intention, writing test cases to cover diverse test scenarios. 
Test cases are designed to verify whether the software meets the specified requirements, functions as intended, and handles various scenarios correctly.

Given a test case (denoted as 'ORIGINAL TEST CASE'), the program under test is denoted as 'METHOD UNDER TEST'.
Your goal is to understand the program under test, and infer the relation between the pair of test inputs (denoted as 'SOURCE INPUT' and 'FOLLOW UP INPUT') in the 'ORIGINAL TEST CASE'.
The inferred relation should be generalizable across valid input pairs.

Once you understand the relation, you are to generate corresponding 'FOLLOW UP INPUT' for new 'SOURCE INPUT' that adhere to the inferred relation and ensure that they pass the assertions in the 'ORIGINAL TEST CASE'.
New source inputs are denoted as 'NEW SOURCE INPUTS'.
<SYSTEM MESSAGE: END>


# ORIGINAL TEST CASE
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


# NEW SOURCE INPUTS
## New input1:
```java
Date dateA = new DateTime("2024-12-31 23:59:59").toDate();
```

## New input2:
```java
Date dateA = new DateTime("2024-06-15 12:30:00").toDate();
```

## New input3:
```java
Date dateA = new DateTime("2024-02-29 00:00:00").toDate();
```

## New input4:
```java
Date dateA = new DateTime("2024-03-01 00:00:00").toDate();
```

## New input5:
```java
Date dateA = new DateTime("2024-11-30 23:59:59").toDate();
```


# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    Date dateA = new DateTime("2024-01-01 00:00:00").toDate();
    Date dateB = new DateTime("2024-01-02 00:00:00").toDate();
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.