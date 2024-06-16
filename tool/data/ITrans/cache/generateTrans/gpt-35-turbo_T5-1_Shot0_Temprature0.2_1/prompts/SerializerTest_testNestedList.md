# METHOD UNDER TEST
```java
public static String serialize(Object object, String serializer) {
    try {
        return serializeWithException(object, serializer);
    } catch (Throwable ex) {
        LogManager.warn("serializer-serialize", StringUtil.format("can not serialize object: %s, cause: %s", TypeUtil.errorSerializeToString(object), ex.toString()));
        return null;
    }
}

public static <T> T deserialize(String value, String typeName) {
    return deserialize(value, typeName, null);
}

```


# TEST CASE
```java
@Test
void testNestedList() {
    List<List<Object>> list = new ArrayList<>();
    list.add(null);
    list.add(new ArrayList<>());
    List<Object> nestedList1 = new ArrayList<>();
    nestedList1.add("nestList1-1");
    nestedList1.add("nestList1-2");
    List<Object> nestedList2 = new LinkedList<>();
    nestedList2.add("nestList2-1");
    nestedList2.add("nestList2-2");
    list.add(nestedList1);
    list.add(nestedList2);
    String serializer = "jackson";
    String json = Serializer.serialize(list, serializer);
    String json2 = "nullA@R#E$X[]A@R#E$X[\"nestList1-1\",\"nestList1-2\"]A@R#E$X[\"nestList2-1\",\"nestList2-2\"]";
    String typeName2 = "java.util.ArrayList-java.util.ArrayList,java.lang.String,java.lang.String";
    List<List<Object>> actualResult = Serializer.deserialize(json2, typeName2);
    assertEquals(list, actualResult);
    // empty list
    String emptyListTypeName = TypeUtil.getName(new ArrayList<>());
    List<Object> emptyList = Serializer.deserialize("[]", emptyListTypeName);
}

```
SOURCE INPUT: `list`,`serializer`
FOLLOW UP INPUT: `json2`,`typeName2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
List<List<Object>> list = new ArrayList<>();
list.add(null);
list.add(new ArrayList<>());
list.add(nestedList1);
list.add(nestedList2);
String serializer = "jackson";
String json2 = "nullA@R#E$X[]A@R#E$X[\"nestList1-1\",\"nestList1-2\"]A@R#E$X[\"nestList2-1\",\"nestList2-2\"]";
String typeName2 = "java.util.ArrayList-java.util.ArrayList,java.lang.String,java.lang.String";
```

## Input pair2:
```java
List<List<Object>> list = new ArrayList<>();
list.add(null);
list.add(new ArrayList<>());
list.add(new ArrayList<>());
String serializer = "jackson";
String json2 = "nullA@R#E$X[]A@R#E$X[]";
String typeName2 = "java.util.ArrayList-java.util.ArrayList";
```



# OUTPUT FORMAT
```java
public class SerializerTest_testNestedList {
    public static List<Object> inputTransformation_testNestedList(List<List<Object>> list, String serializer)  {
        // TODO
        String json2 = 
		String typeName2 = 
		List<Object> transformed_inputs = Arrays.asList(json2, typeName2);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.