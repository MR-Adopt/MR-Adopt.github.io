## New input pair0:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("123", 123);
    v01.put("12x", 123);
    String str = JSON.toJSONString(v01);
    Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

Generation code:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("123", 123);
    v01.put("12x", 123);
    String str = JSON.toJSONString(v01);
```

Explanation: The inferred relation is that the input map `v01` is serialized to a JSON string `str` using the `toJSONString` method, and then deserialized back to a map `v02` using the `parseObject` method. The new input pair satisfies this relation by adding the same key-value pair to the map `v01` and then serializing it to a JSON string. The deserialization of the JSON string back to a map `v02` will produce the same map as the original input.

## New input pair1:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("", 0);
    v01.put(" ", 0);
    String str = JSON.toJSONString(v01);
    Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

Generation code:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("", 0);
    v01.put(" ", 0);
    String str = JSON.toJSONString(v01);
```

Explanation: The inferred relation is that the input map `v01` is serialized to a JSON string `str` using the `toJSONString` method, and then deserialized back to a map `v02` using the `parseObject` method. The new input pair satisfies this relation by adding the same key-value pair to the map `v01` and then serializing it to a JSON string. The deserialization of the JSON string back to a map `v02` will produce the same map as the original input.

## New input pair2:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("null", null);
    v01.put("NULL", null);
    String str = JSON.toJSONString(v01);
    Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

Generation code:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("null", null);
    v01.put("NULL", null);
    String str = JSON.toJSONString(v01);
```

Explanation: The inferred relation is that the input map `v01` is serialized to a JSON string `str` using the `toJSONString` method, and then deserialized back to a map `v02` using the `parseObject` method. The new input pair satisfies this relation by adding the same key-value pair to the map `v01` and then serializing it to a JSON string. The deserialization of the JSON string back to a map `v02` will produce the same map as the original input.

## New input pair3:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("123", 123);
    v01.put("123", 123);
    String str = JSON.toJSONString(v01);
    Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

Generation code:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("123", 123);
    v01.put("123", 123);
    String str = JSON.toJSONString(v01);
```

Explanation: The inferred relation is that the input map `v01` is serialized to a JSON string `str` using the `toJSONString` method, and then deserialized back to a map `v02` using the `parseObject` method. The new input pair satisfies this relation by adding the same key-value pair to the map `v01` and then serializing it to a JSON string. The deserialization of the JSON string back to a map `v02` will produce the same map as the original input.

## New input pair4:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("123", 123);
    v01.put("123", 456);
    String str = JSON.toJSONString(v01);
    Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
    }.getType());
```

Generation code:
```java
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("123", 123);
    v01.put("123", 456);
    String str = JSON.toJSONString(v01);
```

Explanation: The inferred relation is that the input map `v01` is serialized to a JSON string `str` using the `toJSONString` method, and then deserialized back to a map `v02` using the `parseObject` method. The new input pair satisfies this relation by adding the same key-value pair to the map `v01` and then serializing it to a JSON string. The deserialization of the JSON string back to a map `v02` will produce the same map as the original input.
