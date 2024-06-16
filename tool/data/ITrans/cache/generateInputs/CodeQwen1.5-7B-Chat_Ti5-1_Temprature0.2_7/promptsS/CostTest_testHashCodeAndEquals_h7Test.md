# ORIGINAL TEST CASE
```java
@Test
void testHashCodeAndEquals() {
    Cost subject = Cost.costOfSeconds(10);
    Cost same = Cost.costOfSeconds(10);
    Cost other = Cost.costOfSeconds(11);
    assertNotEquals(subject.hashCode(), other.hashCode());
}

```
TEST INPUT: `subject`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return value;
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `subject`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Cost subject = Cost.costOfSeconds(10);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 