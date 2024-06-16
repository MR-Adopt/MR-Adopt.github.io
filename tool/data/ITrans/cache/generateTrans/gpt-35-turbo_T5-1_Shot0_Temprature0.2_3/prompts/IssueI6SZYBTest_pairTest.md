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
public void pairTest() {
    Pair<Integer, Integer> pair = Pair.of(1, 2);
    String jsonStr = JSONUtil.toJsonStr(pair);
    String jsonString = "{\"key\":1,\"value\":2}";
    Class<Pair> beanClass = Pair.class;
    final Pair bean = JSONUtil.toBean(jsonString, beanClass);
    Assert.assertEquals(pair, bean);
}

```
SOURCE INPUT: `pair`
FOLLOW UP INPUT: `jsonString`,`beanClass`


# OTHER INPUT PAIRS 
## Input pair1:
```java
Pair<Integer, Integer> pair = Pair.of(1, 2);
String jsonString = "{\"key\":1,\"value\":2}";
Class<Pair> beanClass = Pair.class;
```

## Input pair2:
```java
Pair<Integer, Integer> pair = Pair.of(0, 0);
String jsonString = "{\"key\":0,\"value\":0}";
Class<Pair> beanClass = Pair.class;
```

## Input pair3:
```java
Pair<Integer, Integer> pair = Pair.of(-1, -1);
String jsonString = "{\"key\":-1,\"value\":-1}";
Class<Pair> beanClass = Pair.class;
```

## Input pair4:
```java
Pair<Integer, Integer> pair = Pair.of(100, 200);
String jsonString = "{\"key\":100,\"value\":200}";
Class<Pair> beanClass = Pair.class;
```

## Input pair5:
```java
Pair<Integer, Integer> pair = Pair.of(Integer.MAX_VALUE, Integer.MIN_VALUE);
String jsonString = "{\"key\":2147483647,\"value\":-2147483648}";
Class<Pair> beanClass = Pair.class;
```

## Input pair6:
```java
Pair<Integer, Integer> pair = Pair.of(123456789, 987654321);
String jsonString = "{\"key\":123456789,\"value\":987654321}";
Class<Pair> beanClass = Pair.class;
```

## Input pair7:
```java
Pair<Integer, Integer> pair = Pair.of(Integer.MAX_VALUE, Integer.MAX_VALUE);
String jsonString = "{\"key\":2147483647,\"value\":2147483647}";
Class<Pair> beanClass = Pair.class;
```

## Input pair8:
```java
Pair<Integer, Integer> pair = Pair.of(Integer.MIN_VALUE, Integer.MIN_VALUE);
String jsonString = "{\"key\":-2147483648,\"value\":-2147483648}";
Class<Pair> beanClass = Pair.class;
```

## Input pair9:
```java
Pair<Integer, Integer> pair = Pair.of(100, -100);
String jsonString = "{\"key\":100,\"value\":-100}";
Class<Pair> beanClass = Pair.class;
```



# OUTPUT FORMAT
```java
public class IssueI6SZYBTest_pairTest {
    public static List<Object> inputTransformation_pairTest(Pair<Integer,Integer> pair)  {
        // TODO
        String jsonString = 
		Class<Pair> beanClass = 
		List<Object> transformed_inputs = Arrays.asList(jsonString, beanClass);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.