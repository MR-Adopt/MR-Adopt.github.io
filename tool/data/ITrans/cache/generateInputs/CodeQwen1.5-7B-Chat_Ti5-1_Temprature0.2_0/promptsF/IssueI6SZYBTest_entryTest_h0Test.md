# ORIGINAL TEST CASE
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


# NEW SOURCE INPUTS
## New source input0:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("", 0);
```

## New source input1:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("1234567890", 1234567890);
```

## New source input2:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("null", null);
```

## New source input3:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("true", 1);
```

## New source input4:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("false", 0);
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("1", 2);
    String jsonString = "{\"1\":2}";
    Class beanClass = AbstractMap.SimpleEntry.class;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.