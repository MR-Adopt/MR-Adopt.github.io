## New input pair0:
```java
    JSONObject v01 = JSONObject.of("name", "John Doe");
    String str = JSON.toJSONString(v01);
    JSONObject v02 = JSON.parseObject(str, JSONObject.class);
```

Generation code:
```java
    JSONObject v01 = JSONObject.of("name", "John Doe");
    String str = JSON.toJSONString(v01);
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string and then parsed back to a `JSONObject`. The new input pair satisfies this relation by providing a `JSONObject` with a single key-value pair `"name": "John Doe"`.

## New input pair1:
```java
    JSONObject v01 = JSONObject.of("age", 30);
    String str = JSON.toJSONString(v01);
    JSONObject v02 = JSON.parseObject(str, JSONObject.class);
```

Generation code:
```java
    JSONObject v01 = JSONObject.of("age", 30);
    String str = JSON.toJSONString(v01);
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string and then parsed back to a `JSONObject`. The new input pair satisfies this relation by providing a `JSONObject` with a single key-value pair `"age": 30`.

## New input pair2:
```java
    JSONObject v01 = JSONObject.of("isStudent", true);
    String str = JSON.toJSONString(v01);
    JSONObject v02 = JSON.parseObject(str, JSONObject.class);
```

Generation code:
```java
    JSONObject v01 = JSONObject.of("isStudent", true);
    String str = JSON.toJSONString(v01);
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string and then parsed back to a `JSONObject`. The new input pair satisfies this relation by providing a `JSONObject` with a single key-value pair `"isStudent": true`.

## New input pair3:
```java
    JSONObject v01 = JSONObject.of("address", JSONObject.of("street", "123 Main St", "city", "New York", "state", "NY", "zip", "10001"));
    String str = JSON.toJSONString(v01);
    JSONObject v02 = JSON.parseObject(str, JSONObject.class);
```

Generation code:
```java
    JSONObject v01 = JSONObject.of("address", JSONObject.of("street", "123 Main St", "city", "New York", "state", "NY", "zip", "10001"));
    String str = JSON.toJSONString(v01);
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string and then parsed back to a `JSONObject`. The new input pair satisfies this relation by providing a `JSONObject` with a single key-value pair `"address": {"street": "123 Main St", "city": "New York", "state": "NY", "zip": "10001"}`.

## New input pair4:
```java
    JSONObject v01 = JSONObject.of("hobbies", Arrays.asList("reading", "coding", "traveling"));
    String str = JSON.toJSONString(v01);
    JSONObject v02 = JSON.parseObject(str, JSONObject.class);
```

Generation code:
```java
    JSONObject v01 = JSONObject.of("hobbies", Arrays.asList("reading", "coding", "traveling"));
    String str = JSON.toJSONString(v01);
```
Explanation: The inferred relation is that the input `v01` is serialized to a JSON string and then parsed back to a `JSONObject`. The new input pair satisfies this relation by providing a `JSONObject` with a single key-value pair `"hobbies": ["reading", "coding", "traveling"]`.
