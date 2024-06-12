# Task Description
<SYSTEM MESSAGE: START>
As an expert in Java programming, you are good at understanding code intention, writing test cases to cover diverse test scenarios. 
Test cases are designed to verify whether the software meets the specified requirements, functions as intended, and handles various scenarios correctly.

Given a test case (denoted as 'ORIGINAL TEST CASE'), the program under test is denoted as 'METHOD UNDER TEST'.
Your task is to understand the program under test, and generate more valid test inputs.
<SYSTEM MESSAGE: END>


# ORIGINAL TEST CASE
```java
@Test
  void testToMediumDate() {
    Date dateA = new DateTime("2024-01-01-00-00").toDate();
    Date dateB = new DateTime("2024-01-02-00-00").toDate();
    Date mediumDateA = DateUtils.toMediumDate(dateA);
    Date mediumDateB = DateUtils.toMediumDate(dateB);
    assertThat(mediumDateB, is(plusOneDay(mediumDateA)));
  }
```
TEST INPUT: `dateA = new DateTime("2024-01-01 00:00:00").toDate();`


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


# REQUIRED DELIVERABLE
Construct five new values for the test input `dateA`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
Date dateA = new DateTime("2024-01-01-00-00").toDate();
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 