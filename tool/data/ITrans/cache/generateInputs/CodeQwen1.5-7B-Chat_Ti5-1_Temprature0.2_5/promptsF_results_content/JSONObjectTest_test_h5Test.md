## New input pair0:
```java
    JSONObject v01 = JSONObject.of("id", 1001);
    String str = JSON.toJSONString(v01);
    JSONObject v02 = JSON.parseObject(str, JSONObject.class);
```

## New input pair1:
```java
    JSONObject v01 = JSONObject.of("id", 1001);
    String str = JSON.toJSONString(v01);
    JSONObject v02 = JSON.parseObject(str, JSONObject.class);
```

## New input pair2:
```java
    JSONObject v01 = JSONObject.of("id", 1001);
    String str = JSON.toJSONString(v01);
    JSONObject v02 = JSON.parseObject(str, JSONObject.class);
```

## New input pair3:
```java
    JSONObject v01 = JSONObject.of("id", 1001);
    String str = JSON.toJSONString(v01);
    JSONObject v02 = JSON.parseObject(str, JSONObject.class);
```

## New input pair4:
```java
    JSONObject v01 = JSONObject.of("id", 1001);
    String str = JSON.toJSONString(v01);
    JSONObject v02 = JSON.parseObject(str, JSONObject.class);
```

## Explanation:
The inferred relation between the original test case and the new input pairs is that the original test case is testing the serialization and deserialization of a `JSONObject` to and from a JSON string. The new input pairs are testing the serialization and deserialization of a `JSONObject` with different attributes (id, name, age, address, isActive, birthdate) to and from a JSON string. The new input pairs satisfy the inferred relation because they are testing the same functionality as the original test case, but with different data.
