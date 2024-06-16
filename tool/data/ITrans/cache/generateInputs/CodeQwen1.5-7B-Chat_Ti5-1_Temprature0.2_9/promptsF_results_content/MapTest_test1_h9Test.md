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
    Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
    }.getType());
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string `str` and then parsed back to a map `v02`. The new input pair satisfies this relation by using the same `v01` as the source input and the same `TypeReference` as the follow-up input.

## New input pair1:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("empty", "");
    v01.put("null", null);
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```
Generation code:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("empty", "");
    v01.put("null", null);
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string `str` and then parsed back to a map `v02`. The new input pair satisfies this relation by using the same `v01` as the source input and the same `TypeReference` as the follow-up input.

## New input pair2:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("largeKey", 12345678901234567890L);
    v01.put("smallKey", 123);
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```
Generation code:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("largeKey", 12345678901234567890L);
    v01.put("smallKey", 123);
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string `str` and then parsed back to a map `v02`. The new input pair satisfies this relation by using the same `v01` as the source input and the same `TypeReference` as the follow-up input.

## New input pair3:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("negativeKey", -123);
    v01.put("positiveKey", 123);
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```
Generation code:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("negativeKey", -123);
    v01.put("positiveKey", 123);
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string `str` and then parsed back to a map `v02`. The new input pair satisfies this relation by using the same `v01` as the source input and the same `TypeReference` as the follow-up input.

## New input pair4:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("specialKey", "@#$%^&*()");
    v01.put("normalKey", "123");
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```
Generation code:
```java
    Map<String, Object> v01 = new HashMap<>();
    v01.put("specialKey", "@#$%^&*()");
    v01.put("normalKey", "123");
    String str = JSON.toJSONString(v01);
    Map<String, Object> v02 = JSON.parseObject(str, new TypeReference<Map<String, Object>>() {
    }.getType());
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string `str` and then parsed back to a map `v02`. The new input pair satisfies this relation by using the same `v01` as the source input and the same `TypeReference` as the follow-up input.
