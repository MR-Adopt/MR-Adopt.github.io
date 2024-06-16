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
TEST INPUT: `pair`


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


# REQUIRED DELIVERABLE
Construct five new values for the test input `pair`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("1", 2);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 