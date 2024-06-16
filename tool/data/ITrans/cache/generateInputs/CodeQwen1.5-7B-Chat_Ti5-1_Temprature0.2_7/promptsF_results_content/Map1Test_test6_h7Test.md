# New input pair0:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(0));
    v01.put("102", BigDecimal.valueOf(0));
```
Follow-up input:
```java
    String str2 = JSON.toJSONString(v01);
    Map<String, BigDecimal> mapType = JSON.parseObject(str2, new TypeReference<Map<String, BigDecimal>>() {
    }.getType());
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string `str2` and then parsed back to a `Map<String, BigDecimal>` `mapType`. The new input pair satisfies this relation by using the same `v01` as the source input.

# New input pair1:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(999999999));
    v01.put("102", BigDecimal.valueOf(888888888));
```
Follow-up input:
```java
    String str2 = JSON.toJSONString(v01);
    Map<String, BigDecimal> mapType = JSON.parseObject(str2, new TypeReference<Map<String, BigDecimal>>() {
    }.getType());
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string `str2` and then parsed back to a `Map<String, BigDecimal>` `mapType`. The new input pair satisfies this relation by using the same `v01` as the source input.

# New input pair2:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(-1));
    v01.put("102", BigDecimal.valueOf(-2));
```
Follow-up input:
```java
    String str2 = JSON.toJSONString(v01);
    Map<String, BigDecimal> mapType = JSON.parseObject(str2, new TypeReference<Map<String, BigDecimal>>() {
    }.getType());
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string `str2` and then parsed back to a `Map<String, BigDecimal>` `mapType`. The new input pair satisfies this relation by using the same `v01` as the source input.

# New input pair3:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(Double.MAX_VALUE));
    v01.put("102", BigDecimal.valueOf(Double.MIN_VALUE));
```
Follow-up input:
```java
    String str2 = JSON.toJSONString(v01);
    Map<String, BigDecimal> mapType = JSON.parseObject(str2, new TypeReference<Map<String, BigDecimal>>() {
    }.getType());
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string `str2` and then parsed back to a `Map<String, BigDecimal>` `mapType`. The new input pair satisfies this relation by using the same `v01` as the source input.

# New input pair4:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(Long.MAX_VALUE));
    v01.put("102", BigDecimal.valueOf(Long.MIN_VALUE));
```
Follow-up input:
```java
    String str2 = JSON.toJSONString(v01);
    Map<String, BigDecimal> mapType = JSON.parseObject(str2, new TypeReference<Map<String, BigDecimal>>() {
    }.getType());
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string `str2` and then parsed back to a `Map<String, BigDecimal>` `mapType`. The new input pair satisfies this relation by using the same `v01` as the source input.
