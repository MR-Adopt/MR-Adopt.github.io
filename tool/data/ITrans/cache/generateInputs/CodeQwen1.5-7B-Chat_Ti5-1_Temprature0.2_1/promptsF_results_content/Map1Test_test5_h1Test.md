# New input pair0:
```java
    Map<String, Double> v01 = new HashMap<>();
    v01.put("101", 1.5);
    v01.put("102", 2.5);
```
Follow-up input:
```java
    String str2 = JSON.toJSONString(v01, "yyyy-MM-dd HH:mm:ss", null, JSONWriter.Feature.WriteDateUseDateFormat);
    Map<String, Double> mapType = JSON.parseObject(str2, new TypeReference<Map<String, Double>>() {
    }.getType());
```
Explanation:
The inferred relation is that the input `v01` is serialized to a JSON string using the `toJSONString` method with a specified date format and features. The resulting JSON string is then parsed back into a `Map<String, Double>` using the `parseObject` method with the same type reference.

# New input pair1:
```java
    Map<String, Double> v01 = new HashMap<>();
    v01.put("101", 0.0);
    v01.put("102", 0.0);
```
Follow-up input:
```java
    String str2 = JSON.toJSONString(v01, "yyyy-MM-dd HH:mm:ss", null, JSONWriter.Feature.WriteDateUseDateFormat);
    Map<String, Double> mapType = JSON.parseObject(str2, new TypeReference<Map<String, Double>>() {
    }.getType());
```
Explanation:
The inferred relation is that the input `v01` is serialized to a JSON string using the `toJSONString` method with a specified date format and features. The resulting JSON string is then parsed back into a `Map<String, Double>` using the `parseObject` method with the same type reference.

# New input pair2:
```java
    Map<String, Double> v01 = new HashMap<>();
    v01.put("101", -1.5);
    v01.put("102", -2.5);
```
Follow-up input:
```java
    String str2 = JSON.toJSONString(v01, "yyyy-MM-dd HH:mm:ss", null, JSONWriter.Feature.WriteDateUseDateFormat);
    Map<String, Double> mapType = JSON.parseObject(str2, new TypeReference<Map<String, Double>>() {
    }.getType());
```
Explanation:
The inferred relation is that the input `v01` is serialized to a JSON string using the `toJSONString` method with a specified date format and features. The resulting JSON string is then parsed back into a `Map<String, Double>` using the `parseObject` method with the same type reference.

# New input pair3:
```java
    Map<String, Double> v01 = new HashMap<>();
    v01.put("101", Double.MAX_VALUE);
    v01.put("102", Double.MIN_VALUE);
```
Follow-up input:
```java
    String str2 = JSON.toJSONString(v01, "yyyy-MM-dd HH:mm:ss", null, JSONWriter.Feature.WriteDateUseDateFormat);
    Map<String, Double> mapType = JSON.parseObject(str2, new TypeReference<Map<String, Double>>() {
    }.getType());
```
Explanation:
The inferred relation is that the input `v01` is serialized to a JSON string using the `toJSONString` method with a specified date format and features. The resulting JSON string is then parsed back into a `Map<String, Double>` using the `parseObject` method with the same type reference.

# New input pair4:
```java
    Map<String, Double> v01 = new HashMap<>();
    v01.put("101", Double.NaN);
    v01.put("102", Double.NaN);
```
Follow-up input:
```java
    String str2 = JSON.toJSONString(v01, "yyyy-MM-dd HH:mm:ss", null, JSONWriter.Feature.WriteDateUseDateFormat);
    Map<String, Double> mapType = JSON.parseObject(str2, new TypeReference<Map<String, Double>>() {
    }.getType());
```
Explanation:
The inferred relation is that the input `v01` is serialized to a JSON string using the `toJSONString` method with a specified date format and features. The resulting JSON string is then parsed back into a `Map<String, Double>` using the `parseObject` method with the same type reference.
