## New input pair0:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("123", 123);
    v01.put("12x", 123);
    String str = JSON.toJSONString(v01);
    Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

### Explanation:
The inferred relation between the source input and follow-up input is that the source input is a `Map<String, Integer>` and the follow-up input is a `Map<String, Integer>` after parsing the JSON string.

### Code to generate follow-up input:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("123", 123);
    v01.put("12x", 123);
    String str = JSON.toJSONString(v01);
    Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

## New input pair1:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("empty", "");
    v01.put("null", null);
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```

### Explanation:
The inferred relation between the source input and follow-up input is that the source input is a `Map<String, Object>` and the follow-up input is a `Map<String, Object>` after parsing the JSON string.

### Code to generate follow-up input:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("empty", "");
    v01.put("null", null);
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```

## New input pair2:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("large", 1234567890);
    v01.put("small", -123456789);
    String str = JSON.toJSONString(v01);
    Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

### Explanation:
The inferred relation between the source input and follow-up input is that the source input is a `Map<String, Integer>` and the follow-up input is a `Map<String, Integer>` after parsing the JSON string.

### Code to generate follow-up input:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("large", 1234567890);
    v01.put("small", -123456789);
    String str = JSON.toJSONString(v01);
    Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

## New input pair3:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("double", 123.456);
    v01.put("float", -123.456f);
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```

### Explanation:
The inferred relation between the source input and follow-up input is that the source input is a `Map<String, Object>` and the follow-up input is a `Map<String, Object>` after parsing the JSON string.

### Code to generate follow-up input:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("double", 123.456);
    v01.put("float", -123.456f);
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```

## New input pair4:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("boolean", true);
    v01.put("array", new int[]{1, 2, 3});
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```

### Explanation:
The inferred relation between the source input and follow-up input is that the source input is a `Map<String, Object>` and the follow-up input is a `Map<String, Object>` after parsing the JSON string.

### Code to generate follow-up input:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("boolean", true);
    v01.put("array", new int[]{1, 2, 3});
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```
