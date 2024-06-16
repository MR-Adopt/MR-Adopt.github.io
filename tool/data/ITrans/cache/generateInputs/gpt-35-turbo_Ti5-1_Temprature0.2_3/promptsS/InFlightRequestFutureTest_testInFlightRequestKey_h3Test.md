# ORIGINAL TEST CASE
```java
@Test
public void testInFlightRequestKey() {
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 1);
    Assert.assertEquals(requestKey1.hashCode(), requestKey2.hashCode());
}

```
TEST INPUT: `requestKey1`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return Objects.hashCode(group);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `requestKey1`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 