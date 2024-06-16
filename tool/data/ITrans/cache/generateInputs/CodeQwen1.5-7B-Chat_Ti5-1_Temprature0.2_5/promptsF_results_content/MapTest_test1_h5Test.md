# New input pair0:
```java
    v01.put("123", 123);
    v01.put("12x", 123);
```

Follow-up input:
```java
    String str2 = JSON.toJSONString(v01);
    Map<String, Integer> mapType = JSON.parseObject(str2, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

Generation code:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("123", 123);
    v01.put("12x", 123);
    String str2 = JSON.toJSONString(v01);
    Map<String, Integer> mapType = JSON.parseObject(str2, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

Explanation:
The inferred relation between the source input and the follow-up input is that the source input is a `Map<String, Integer>` and the follow-up input is a `Map<String, Integer>` obtained by parsing the JSON string obtained from the source input. The source input is created by adding two key-value pairs to an empty `Map<String, Integer>`, where the key is a string and the value is an integer. The follow-up input is created by parsing the JSON string obtained from the source input using the `JSON.parseObject` method.

# New input pair1:
```java
    v01.put("empty", "");
    v01.put("null", null);
```

Follow-up input:
```java
    String str2 = JSON.toJSONString(v01);
    Map<String, String> mapType = JSON.parseObject(str2, new TypeReference<Map<String, String>>() {
    }.getType());
```

Generation code:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("empty", "");
    v01.put("null", null);
    String str2 = JSON.toJSONString(v01);
    Map<String, String> mapType = JSON.parseObject(str2, new TypeReference<Map<String, String>>() {
    }.getType());
```

Explanation:
The inferred relation between the source input and the follow-up input is that the source input is a `Map<String, Integer>` and the follow-up input is a `Map<String, String>` obtained by parsing the JSON string obtained from the source input. The source input is created by adding two key-value pairs to an empty `Map<String, Integer>`, where the key is a string and the value is an integer. The follow-up input is created by parsing the JSON string obtained from the source input using the `JSON.parseObject` method, with the type parameter specified as `Map<String, String>`.

# New input pair2:
```java
    v01.put("negative", -123);
    v01.put("positive", 456);
```

Follow-up input:
```java
    String str2 = JSON.toJSONString(v01);
    Map<String, Integer> mapType = JSON.parseObject(str2, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

Generation code:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("negative", -123);
    v01.put("positive", 456);
    String str2 = JSON.toJSONString(v01);
    Map<String, Integer> mapType = JSON.parseObject(str2, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

Explanation:
The inferred relation between the source input and the follow-up input is that the source input is a `Map<String, Integer>` and the follow-up input is a `Map<String, Integer>` obtained by parsing the JSON string obtained from the source input. The source input is created by adding two key-value pairs to an empty `Map<String, Integer>`, where the key is a string and the value is an integer. The follow-up input is created by parsing the JSON string obtained from the source input using the `JSON.parseObject` method, with the type parameter specified as `Map<String, Integer>`.

# New input pair3:
```java
    v01.put("large", 1234567890);
    v01.put("small", -123456789);
```

Follow-up input:
```java
    String str2 = JSON.toJSONString(v01);
    Map<String, Long> mapType = JSON.parseObject(str2, new TypeReference<Map<String, Long>>() {
    }.getType());
```

Generation code:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("large", 1234567890);
    v01.put("small", -123456789);
    String str2 = JSON.toJSONString(v01);
    Map<String, Long> mapType = JSON.parseObject(str2, new TypeReference<Map<String, Long>>() {
    }.getType());
```

Explanation:
The inferred relation between the source input and the follow-up input is that the source input is a `Map<String, Integer>` and the follow-up input is a `Map<String, Long>` obtained by parsing the JSON string obtained from the source input. The source input is created by adding two key-value pairs to an empty `Map<String, Integer>`, where the key is a string and the value is an integer. The follow-up input is created by parsing the JSON string obtained from the source input using the `JSON.parseObject` method, with the type parameter specified as `Map<String, Long>`.

# New input pair4:
```java
    v01.put("special", "@#$%^&*()");
    v01.put("alphanumeric", "abc123");
```

Follow-up input:
```java
    String str2 = JSON.toJSONString(v01);
    Map<String, String> mapType = JSON.parseObject(str2, new TypeReference<Map<String, String>>() {
    }.getType());
```

Generation code:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("special", "@#$%^&*()");
    v01.put("alphanumeric", "abc123");
    String str2 = JSON.toJSONString(v01);
    Map<String, String> mapType = JSON.parseObject(str2, new TypeReference<Map<String, String>>() {
    }.getType());
```

Explanation:
The inferred relation between the source input and the follow-up input is that the source input is a `Map<String, Integer>` and the follow-up input is a `Map<String, String>` obtained by parsing the JSON string obtained from the source input. The source input is created by adding two key-value pairs to an empty `Map<String, Integer>`, where the key is a string and the value is an integer. The follow-up input is created by parsing the JSON string obtained from the source input using the `JSON.parseObject` method, with the type parameter specified as `Map<String, String>`.
