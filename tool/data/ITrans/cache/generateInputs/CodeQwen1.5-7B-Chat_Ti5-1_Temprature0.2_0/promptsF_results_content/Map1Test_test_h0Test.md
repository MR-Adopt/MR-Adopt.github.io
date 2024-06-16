## New input pair0:
```java
    Map<String, String> v01 = new HashMap<>();
    v01.put("456", "def");
    String str = JSON.toJSONString(v01);
    Map<String, String> v02 = JSON.parseObject(str, new TypeReference<Map<String, String>>() {
    }.getType());
```
Generation code:
```java
    Map<String, String> v01 = new HashMap<>();
    v01.put("456", "def");
    String str = JSON.toJSONString(v01);
    Map<String, String> v02 = JSON.parseObject(str, new TypeReference<Map<String, String>>() {
    }.getType());
```
Explanation: The inferred relation is that the input map `v01` is serialized to a JSON string `str` and then parsed back to a map `v02`. The new source input `v01` is a different map with a different key-value pair, which should still satisfy the relation.

## New input pair1:
```java
    Map<String, String> v01 = new HashMap<>();
    v01.put("123", "xyz");
    String str = JSON.toJSONString(v01);
    Map<String, String> v02 = JSON.parseObject(str, new TypeReference<Map<String, String>>() {
    }.getType());
```
Generation code:
```java
    Map<String, String> v01 = new HashMap<>();
    v01.put("123", "xyz");
    String str = JSON.toJSONString(v01);
    Map<String, String> v02 = JSON.parseObject(str, new TypeReference<Map<String, String>>() {
    }.getType());
```
Explanation: The inferred relation is that the input map `v01` is serialized to a JSON string `str` and then parsed back to a map `v02`. The new source input `v01` is a different map with a different key-value pair, which should still satisfy the relation.

## New input pair2:
```java
    Map<String, String> v01 = new HashMap<>();
    v01.put("789", "ghi");
    v01.put("123", "jkl");
    String str = JSON.toJSONString(v01);
    Map<String, String> v02 = JSON.parseObject(str, new TypeReference<Map<String, String>>() {
    }.getType());
```
Generation code:
```java
    Map<String, String> v01 = new HashMap<>();
    v01.put("789", "ghi");
    v01.put("123", "jkl");
    String str = JSON.toJSONString(v01);
    Map<String, String> v02 = JSON.parseObject(str, new TypeReference<Map<String, String>>() {
    }.getType());
```
Explanation: The inferred relation is that the input map `v01` is serialized to a JSON string `str` and then parsed back to a map `v02`. The new source input `v01` is a different map with a different key-value pair, which should still satisfy the relation.

## New input pair3:
```java
    Map<String, String> v01 = new HashMap<>();
    v01.put("123", "mno");
    v01.put("456", "pqr");
    v01.put("789", "stu");
    String str = JSON.toJSONString(v01);
    Map<String, String> v02 = JSON.parseObject(str, new TypeReference<Map<String, String>>() {
    }.getType());
```
Generation code:
```java
    Map<String, String> v01 = new HashMap<>();
    v01.put("123", "mno");
    v01.put("456", "pqr");
    v01.put("789", "stu");
    String str = JSON.toJSONString(v01);
    Map<String, String> v02 = JSON.parseObject(str, new TypeReference<Map<String, String>>() {
    }.getType());
```
Explanation: The inferred relation is that the input map `v01` is serialized to a JSON string `str` and then parsed back to a map `v02`. The new source input `v01` is a different map with a different key-value pair, which should still satisfy the relation.

## New input pair4:
```java
    Map<String, String> v01 = new HashMap<>();
    v01.put("123", "vwx");
    v01.put("456", "yza");
    v01.put("789", "bcd");
    v01.put("101112", "efg");
    String str = JSON.toJSONString(v01);
    Map<String, String> v02 = JSON.parseObject(str, new TypeReference<Map<String, String>>() {
    }.getType());
```
Generation code:
```java
    Map<String, String> v01 = new HashMap<>();
    v01.put("123", "vwx");
    v01.put("456", "yza");
    v01.put("789", "bcd");
    v01.put("101112", "efg");
    String str = JSON.toJSONString(v01);
    Map<String, String> v02 = JSON.parseObject(str, new TypeReference<Map<String, String>>() {
    }.getType());
```
Explanation: The inferred relation is that the input map `v01` is serialized to a JSON string `str` and then parsed back to a map `v02`. The new source input `v01` is a different map with a different key-value pair, which should still satisfy the relation.
