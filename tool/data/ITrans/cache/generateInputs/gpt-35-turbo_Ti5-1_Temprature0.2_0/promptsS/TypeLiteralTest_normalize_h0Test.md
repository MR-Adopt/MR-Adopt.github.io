# ORIGINAL TEST CASE
```java
@Test
public void normalize() {
    Class input = Integer.class;
    TypeLiteral<List<Integer>> type1 = TypeLiteral.listOf(input);
    TypeLiteral<List<Integer>> type2 = new TypeLiteral<List<Integer>>() {
    };
    TypeLiteral<List<Integer>> input2 = TypeLiteral.listOf(Integer.class);
    TypeLiteral<List<Integer>> type3 = TypeLiteral.normalize(input2);
    TypeLiteral<List<Integer>> type4 = TypeLiteral.normalize(type2);
    assertTypesEqual(type1, type3);
    assertEquals(type1, type3);
}

```
TEST INPUT: `input`


# METHOD UNDER TEST
```java
/**
 * Creates TypeLiteral that represents List&lt;T&gt; type.
 */
public static <T> TypeLiteral<List<T>> listOf(TypeLiteral<? extends T> type) {
    return new TypeLiteral<>(List.class, type.toString());
}

/**
 * Cuts references to outer objects in case of anonymous subclasses.
 */
static <T> TypeLiteral<T> normalize(TypeLiteral<T> type) {
    Objects.requireNonNull(type, "Null type");
    if (type.getClass() == TypeLiteral.class) {
        // direct instance, pass through
        return type;
    }
    // just recreate it with same content
    return new TypeLiteral<>(type.getRawType(), type.argumentTypes);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `input`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Class input = Integer.class;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 