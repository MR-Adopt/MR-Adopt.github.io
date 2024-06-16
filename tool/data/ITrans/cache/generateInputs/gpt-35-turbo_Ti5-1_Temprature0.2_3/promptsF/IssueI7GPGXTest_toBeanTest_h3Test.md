# ORIGINAL TEST CASE
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
    Pair<String, Boolean> hutoolPair = new Pair<>("", true);
```

## New source input1:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>(null, true);
```

## New source input2:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", false);
```

## New source input3:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test2", true);
```

## New source input4:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", null);
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    Pair<String, Boolean> hutoolPair = new Pair<>("test1", true);
    String jsonString = "{\"key\":\"test1\",\"value\":true}";
    TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {
    };
    boolean ignoreError = false;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.