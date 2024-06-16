# New input pair0:
```java
    Map<String, Boolean> v01 = new HashMap<>();
    v01.put("101", true);
    v01.put("102", false);
```
Follow-up input:
```java
    String str = JSON.toJSONString(v01);
    Map<String, Boolean> v02 = JSON.parseObject(str, new TypeReference<Map<String, Boolean>>() {
    }.getType());
```
Explanation:
The inferred relation between the source input and the follow-up input is that the source input is serialized to a JSON string using the `toJSONString` method and then parsed back to a map using the `parseObject` method. The `toJSONString` method takes a map as input and returns a JSON string, while the `parseObject` method takes a JSON string and a type reference as input and returns a map. Therefore, the follow-up input satisfies the inferred relation by serializing the source input to a JSON string and then parsing the resulting string back to a map.

# New input pair1:
```java
    Map<String, Boolean> v01 = new HashMap<>();
    v01.put("101", false);
    v01.put("102", false);
```
Follow-up input:
```java
    String str = JSON.toJSONString(v01);
    Map<String, Boolean> v02 = JSON.parseObject(str, new TypeReference<Map<String, Boolean>>() {
    }.getType());
```
Explanation:
The inferred relation between the source input and the follow-up input is that the source input is serialized to a JSON string using the `toJSONString` method and then parsed back to a map using the `parseObject` method. The `toJSONString` method takes a map as input and returns a JSON string, while the `parseObject` method takes a JSON string and a type reference as input and returns a map. Therefore, the follow-up input satisfies the inferred relation by serializing the source input to a JSON string and then parsing the resulting string back to a map.

# New input pair2:
```java
    Map<String, Boolean> v01 = new HashMap<>();
    v01.put("101", true);
    v01.put("102", true);
```
Follow-up input:
```java
    String str = JSON.toJSONString(v01);
    Map<String, Boolean> v02 = JSON.parseObject(str, new TypeReference<Map<String, Boolean>>() {
    }.getType());
```
Explanation:
The inferred relation between the source input and the follow-up input is that the source input is serialized to a JSON string using the `toJSONString` method and then parsed back to a map using the `parseObject` method. The `toJSONString` method takes a map as input and returns a JSON string, while the `parseObject` method takes a JSON string and a type reference as input and returns a map. Therefore, the follow-up input satisfies the inferred relation by serializing the source input to a JSON string and then parsing the resulting string back to a map.

# New input pair3:
```java
    Map<String, Boolean> v01 = new HashMap<>();
    v01.put("101", true);
    v01.put("102", false);
    v01.put("103", true);
```
Follow-up input:
```java
    String str = JSON.toJSONString(v01);
    Map<String, Boolean> v02 = JSON.parseObject(str, new TypeReference<Map<String, Boolean>>() {
    }.getType());
```
Explanation:
The inferred relation between the source input and the follow-up input is that the source input is serialized to a JSON string using the `toJSONString` method and then parsed back to a map using the `parseObject` method. The `toJSONString` method takes a map as input and returns a JSON string, while the `parseObject` method takes a JSON string and a type reference as input and returns a map. Therefore, the follow-up input satisfies the inferred relation by serializing the source input to a JSON string and then parsing the resulting string back to a map.

# New input pair4:
```java
    Map<String, Boolean> v01 = new HashMap<>();
    v01.put("101", true);
    v01.put("102", false);
    v01.put("103", true);
    v01.put("104", false);
```
Follow-up input:
```java
    String str = JSON.toJSONString(v01);
    Map<String, Boolean> v02 = JSON.parseObject(str, new TypeReference<Map<String, Boolean>>() {
    }.getType());
```
Explanation:
The inferred relation between the source input and the follow-up input is that the source input is serialized to a JSON string using the `toJSONString` method and then parsed back to a map using the `parseObject` method. The `toJSONString` method takes a map as input and returns a JSON string, while the `parseObject` method takes a JSON string and a type reference as input and returns a map. Therefore, the follow-up input satisfies the inferred relation by serializing the source input to a JSON string and then parsing the resulting string back to a map.
