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
SOURCE INPUT: `input`
FOLLOW UP INPUT: `input2`


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


# NEW SOURCE INPUTS
## New source input0:
```java
    Class input = Integer.class;
```

## New source input1:
```java
    Class input = String.class;
```

## New source input2:
```java
    Class input = List.class;
```

## New source input3:
```java
    Class input = ArrayList.class;
```

## New source input4:
```java
    Class input = new ArrayList<Integer>(){}.getClass();
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    Class input = Integer.class;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.