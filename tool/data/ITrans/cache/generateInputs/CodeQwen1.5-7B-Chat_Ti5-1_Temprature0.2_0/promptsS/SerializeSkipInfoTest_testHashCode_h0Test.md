# ORIGINAL TEST CASE
```java
@Test
void testHashCode() {
    SerializeSkipInfo serializeSkipInfo = new SerializeSkipInfo();
    serializeSkipInfo.setFieldName("testFieldName1,testFieldName2");
    serializeSkipInfo.setFullClassName("testFullClassName");
    SerializeSkipInfo serializeSkipInfo2 = new SerializeSkipInfo();
    serializeSkipInfo2.setFieldName("testFieldName1,testFieldName2");
    serializeSkipInfo2.setFullClassName("testFullClassName");
    assertEquals(serializeSkipInfo2.hashCode(), serializeSkipInfo.hashCode());
}

```
TEST INPUT: `serializeSkipInfo`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return fullClassName.hashCode() * 17 + fieldName.hashCode();
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `serializeSkipInfo`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    SerializeSkipInfo serializeSkipInfo = new SerializeSkipInfo();
    serializeSkipInfo.setFieldName("testFieldName1,testFieldName2");
    serializeSkipInfo.setFullClassName("testFullClassName");
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 