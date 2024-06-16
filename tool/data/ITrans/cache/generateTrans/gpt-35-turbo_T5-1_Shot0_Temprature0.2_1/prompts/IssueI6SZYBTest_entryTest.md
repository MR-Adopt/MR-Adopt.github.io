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
public void entryTest() {
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("1", 2);
    String jsonStr = JSONUtil.toJsonStr(pair);
    String jsonString = "{\"1\":2}";
    Class beanClass = AbstractMap.SimpleEntry.class;
    final Map.Entry bean = (Entry) JSONUtil.toBean(jsonString, beanClass);
    Assert.assertEquals(pair, bean);
}

```
SOURCE INPUT: `pair`
FOLLOW UP INPUT: `jsonString`,`beanClass`


# OTHER INPUT PAIRS 
## Input pair1:
```java
Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("1", 2);
String jsonString = "{\"1\":2}";
Class beanClass = AbstractMap.SimpleEntry.class;
```

## Input pair2:
```java
Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("abc", 123);
String jsonString = "{\"abc\":123}";
Class beanClass = AbstractMap.SimpleEntry.class;
```

## Input pair3:
```java
Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("xyz", 0);
String jsonString = "{\"xyz\":0}";
Class beanClass = AbstractMap.SimpleEntry.class;
```

## Input pair4:
```java
Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("", 999);
String jsonString = "{\"\":999}";
Class beanClass = AbstractMap.SimpleEntry.class;
```

## Input pair5:
```java
Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("abc123", -789);
String jsonString = "{\"abc123\":-789}";
Class beanClass = AbstractMap.SimpleEntry.class;
```

## Input pair6:
```java
Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key", -100);
String jsonString = "{\"key\":-100}";
Class beanClass = AbstractMap.SimpleEntry.class;
```

## Input pair7:
```java
Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("", 0);
String jsonString = "{\"\":0}";
Class beanClass = AbstractMap.SimpleEntry.class;
```

## Input pair8:
```java
Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key", -1);
String jsonString = "{\"key\":-1}";
Class beanClass = AbstractMap.SimpleEntry.class;
```

## Input pair9:
```java
Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key", Integer.MAX_VALUE);
String jsonString = "{\"key\":2147483647}";
Class beanClass = AbstractMap.SimpleEntry.class;
```

## Input pair10:
```java
Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key", 100);
String jsonString = "{\"key\":100}";
Class beanClass = AbstractMap.SimpleEntry.class;
```



# OUTPUT FORMAT
```java
public class IssueI6SZYBTest_entryTest {
    public static List<Object> inputTransformation_entryTest(Map.Entry<String,Integer> pair)  {
        // TODO
        String jsonString = 
		Class beanClass = 
		List<Object> transformed_inputs = Arrays.asList(jsonString, beanClass);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.