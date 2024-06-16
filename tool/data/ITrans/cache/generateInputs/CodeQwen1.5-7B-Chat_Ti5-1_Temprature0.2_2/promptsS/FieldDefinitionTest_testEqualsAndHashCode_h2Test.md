# ORIGINAL TEST CASE
```java
@Test
void testEqualsAndHashCode() {
    FieldDefinition subject = new FieldDefinition("foo", TokenType.STRING);
    var same = new FieldDefinition(NAME, TOKEN_TYPE);
    var other1 = new FieldDefinition(NAME, TokenType.INT);
    var other2 = new FieldDefinition("Bar", TOKEN_TYPE);
    FieldDefinition other3 = new FieldDefinition("foo", TokenType.STRING).deprecate();
    assertNotEquals(other3.hashCode(), subject.hashCode());
}

```
TEST INPUT: `subject`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return Objects.hash(name, type, deprecated);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `subject`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    FieldDefinition subject = new FieldDefinition("foo", TokenType.STRING);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 