# New input pair0:
```java
    Map<String, Double> v01 = new HashMap<>();
    v01.put("101", 1.5);
    v01.put("102", 2.5);
```

Generated follow-up input:
```java
    String str = JSON.toJSONString(v01);
    Map<String, Double> v02 = JSON.parseObject(str, new TypeReference<Map<String, Double>>() {
    }.getType());
```

Explanation: The inferred relation between the source input and the follow-up input is that the source input is serialized to a JSON string and then parsed back into a map. The new input pair satisfies this relation by providing a different set of values for the map entries.

# New input pair1:
```java
    Map<String, Double> v01 = new HashMap<>();
    v01.put("101", -1D);
    v01.put("102", -2D);
```

Generated follow-up input:
```java
    String str = JSON.toJSONString(v01);
    Map<String, Double> v02 = JSON.parseObject(str, new TypeReference<Map<String, Double>>() {
    }.getType());
```

Explanation: The inferred relation between the source input and the follow-up input is that the source input is serialized to a JSON string and then parsed back into a map. The new input pair satisfies this relation by providing a different set of values for the map entries.

# New input pair2:
```java
    Map<String, Double> v01 = new HashMap<>();
    v01.put("101", 0D);
    v01.put("102", 0D);
```

Generated follow-up input:
```java
    String str = JSON.toJSONString(v01);
    Map<String, Double> v02 = JSON.parseObject(str, new TypeReference<Map<String, Double>>() {
    }.getType());
```

Explanation: The inferred relation between the source input and the follow-up input is that the source input is serialized to a JSON string and then parsed back into a map. The new input pair satisfies this relation by providing a different set of values for the map entries.

# New input pair3:
```java
    Map<String, Double> v01 = new HashMap<>();
    v01.put("101", Double.MAX_VALUE);
    v01.put("102", Double.MIN_VALUE);
```

Generated follow-up input:
```java
    String str = JSON.toJSONString(v01);
    Map<String, Double> v02 = JSON.parseObject(str, new TypeReference<Map<String, Double>>() {
    }.getType());
```

Explanation: The inferred relation between the source input and the follow-up input is that the source input is serialized to a JSON string and then parsed back into a map. The new input pair satisfies this relation by providing a different set of values for the map entries.

# New input pair4:
```java
    Map<String, Double> v01 = new HashMap<>();
    v01.put("101", Double.NaN);
    v01.put("102", Double.NaN);
```

Generated follow-up input:
```java
    String str = JSON.toJSONString(v01);
    Map<String, Double> v02 = JSON.parseObject(str, new TypeReference<Map<String, Double>>() {
    }.getType());
```

Explanation: The inferred relation between the source input and the follow-up input is that the source input is serialized to a JSON string and then parsed back into a map. The new input pair satisfies this relation by providing a different set of values for the map entries.
