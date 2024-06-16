# METHOD UNDER TEST
```java
/**
 * 转换为JSON字符串并写出到writer
 *
 * @param obj 被转为JSON的对象
 * @param writer Writer
 * @since 5.3.3
 */
public static void toJsonStr(Object obj, Writer writer) {
    if (null != obj) {
        toJsonStr(parse(obj), writer);
    }
}

/**
 * 转为实体类对象
 *
 * @param <T>         Bean类型
 * @param json        JSONObject
 * @param beanType    实体类对象类型
 * @param ignoreError 是否忽略转换错误
 * @return 实体类对象
 * @since 4.3.2
 */
@SuppressWarnings("deprecation")
public static <T> T toBean(JSON json, Type beanType, boolean ignoreError) {
    if (null == json) {
        return null;
    }
    return json.toBean(beanType, ignoreError);
}

```


# TEST CASE
```java
@Test
public void toBeanTest() {
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", true);
    String a = JSONUtil.toJsonStr(hutoolPair);
    String jsonString = "{\"key\":\"test1\",\"value\":true}";
    TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {
    };
    boolean ignoreError = false;
    Pair<String, Boolean> pair = JSONUtil.toBean(jsonString, typeReference, ignoreError);
    Assert.assertEquals(hutoolPair, pair);
}

```
SOURCE INPUT: `hutoolPair`
FOLLOW UP INPUT: `jsonString`,`typeReference`,`ignoreError`


# OTHER INPUT PAIRS 
## Input pair1:
```java
Pair<String, Boolean> hutoolPair = new Pair<>("test1", true);
String jsonString = "{\"key\":\"test1\",\"value\":true}";
TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {
};
boolean ignoreError = false;
```

## Input pair2:
```java
Pair<String, Boolean> hutoolPair = new Pair<>("", true);
String jsonString = "{\"key\":\"\",\"value\":true}";
TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {};
boolean ignoreError = false;
```

## Input pair3:
```java
Pair<String, Boolean> hutoolPair = new Pair<>("test2", false);
String jsonString = "{\"key\":\"test2\",\"value\":false}";
TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {};
boolean ignoreError = false;
```

## Input pair4:
```java
Pair<String, Boolean> hutoolPair = new Pair<>("test4", true);
String jsonString = "{\"key\":\"test4\",\"value\":true}";
TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {};
boolean ignoreError = false;
```

## Input pair5:
```java
Pair<String, Boolean> hutoolPair = new Pair<>("", true);
String jsonString = "{\"key\":\"\",\"value\":true}";
TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {
};
boolean ignoreError = false;
```

## Input pair6:
```java
Pair<String, Boolean> hutoolPair = new Pair<>("test2", false);
String jsonString = "{\"key\":\"test2\",\"value\":false}";
TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {
};
boolean ignoreError = false;
```

## Input pair7:
```java
Pair<String, Boolean> hutoolPair = new Pair<>("test4", true);
String jsonString = "{\"key\":\"test4\",\"value\":true}";
TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {
};
boolean ignoreError = false;
```

## Input pair8:
```java
Pair<String, Boolean> hutoolPair = new Pair<>("test1", false);
String jsonString = "{\"key\":\"test1\",\"value\":false}";
TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {};
boolean ignoreError = false;
```

## Input pair9:
```java
Pair<String, Boolean> hutoolPair = new Pair<>("test2", true);
String jsonString = "{\"key\":\"test2\",\"value\":true}";
TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {};
boolean ignoreError = false;
```



# OUTPUT FORMAT
```java
public class IssueI7GPGXTest_toBeanTest {
    public static List<Object> inputTransformation_toBeanTest(Pair<String, Boolean> hutoolPair)  {
        // TODO
        String jsonString = 
		TypeReference<Pair<String, Boolean>> typeReference = 
		boolean ignoreError = 
		List<Object> transformed_inputs = Arrays.asList(jsonString, typeReference, ignoreError);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.