# ORIGINAL TEST CASE
```java
@Test
public void testGetCacheKey() {
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "hello", null);
    EqualityFilter f4 = new EqualityFilter("x", ColumnType.STRING, "hello", null);
    IsFalseDimFilter f1_3 = IsFalseDimFilter.of(f3);
    IsFalseDimFilter f1_4 = IsFalseDimFilter.of(f4);
    Assert.assertArrayEquals(f1_3.getCacheKey(), f1_4.getCacheKey());
}

```
TEST INPUT: `f3`


# METHOD UNDER TEST
```java
public static IsFalseDimFilter of(DimFilter field) {
    return new IsFalseDimFilter(field);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `f3`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "hello", null);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 