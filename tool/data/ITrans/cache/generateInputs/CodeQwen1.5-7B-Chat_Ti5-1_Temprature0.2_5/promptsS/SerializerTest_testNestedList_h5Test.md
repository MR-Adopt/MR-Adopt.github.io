# ORIGINAL TEST CASE
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
TEST INPUT: `list`,`serializer`


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


# REQUIRED DELIVERABLE
Construct five new values for the test input `list`,`serializer`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    List<List<Object>> list = new ArrayList<>();
    list.add(null);
    list.add(new ArrayList<>());
    list.add(nestedList1);
    list.add(nestedList2);
    String serializer = "jackson";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 