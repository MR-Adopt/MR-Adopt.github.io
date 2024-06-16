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


# TEST CASE
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


# OTHER INPUT PAIRS 



# OUTPUT FORMAT
```java
public class TypeLiteralTest_normalize {
    public static TypeLiteral inputTransformation_normalize(Class input)  {
        // TODO
        TypeLiteral<List<Integer>> input2 = 
		return input2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.