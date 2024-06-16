# METHOD UNDER TEST
```java
/**
 * Append the index to the path.
 *
 * @param index the index
 * @return the path
 */
public JsonNodePath append(int index) {
    return new JsonNodePath(this, index);
}

```


# TEST CASE
```java
@Test
void equalsEquals() {
    JsonNodePath root = new JsonNodePath(PathType.JSON_POINTER);
    String token1 = "a";
    String token2 = "a";
    JsonNodePath a1 = root.append(token1);
    JsonNodePath a2 = root.append(token2);
    assertEquals(a1, a2);
}

```
SOURCE INPUT: `token1`
FOLLOW UP INPUT: `token2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
String token1 = "a";
String token2 = "a";
```

## Input pair2:
```java
String token1 = "b";
String token2 = "b";
```

## Input pair3:
```java
String token1 = "";
String token2 = "";
```

## Input pair4:
```java
String token1 = "123";
String token2 = "123";
```

## Input pair5:
```java
String token1 = "a.b";
String token2 = "a.b";
```

## Input pair6:
```java
String token1 = "A";
String token2 = "A";
```

## Input pair7:
```java
String token1 = "abc";
String token2 = "abc";
```

## Input pair8:
```java
String token1 = "1";
String token2 = "1";
```



# OUTPUT FORMAT
```java
public class JsonNodePathTest_equalsEquals {
    public static String inputTransformation_equalsEquals(String token1)  {
        // TODO
        String token2 = 
		return token2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.