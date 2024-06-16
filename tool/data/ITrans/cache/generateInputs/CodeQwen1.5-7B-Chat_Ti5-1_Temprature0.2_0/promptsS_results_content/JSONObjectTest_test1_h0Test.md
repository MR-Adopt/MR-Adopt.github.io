## New input1:
```java
    JSONObject v01 = JSONObject.of("id", 1001, "name", "John Doe");
```
Explanation: This input includes an additional key-value pair ("name", "John Doe") in the JSONObject. It demonstrates that the method under test can handle objects with multiple key-value pairs.

## New input2:
```java
    JSONObject v01 = JSONObject.of("id", 1001, "age", 30);
```
Explanation: This input includes an additional key-value pair ("age", 30) in the JSONObject. It demonstrates that the method under test can handle objects with different data types as values.

## New input3:
```java
    JSONObject v01 = JSONObject.of("id", 1001, "isActive", true);
```
Explanation: This input includes an additional key-value pair ("isActive", true) in the JSONObject. It demonstrates that the method under test can handle objects with boolean values.

## New input4:
```java
    JSONObject v01 = JSONObject.of("id", 1001, "address", JSONObject.of("street", "123 Main St", "city", "Anytown"));
```
Explanation: This input includes an additional key-value pair ("address", another JSONObject) in the JSONObject. It demonstrates that the method under test can handle nested JSONObjects.

## New input5:
```java
    JSONObject v01 = JSONObject.of("id", 1001, "hobbies", JSONArray.of("reading", "coding"));
```
Explanation: This input includes an additional key-value pair ("hobbies", a JSONArray) in the JSONObject. It demonstrates that the method under test can handle JSONArrays as values.
