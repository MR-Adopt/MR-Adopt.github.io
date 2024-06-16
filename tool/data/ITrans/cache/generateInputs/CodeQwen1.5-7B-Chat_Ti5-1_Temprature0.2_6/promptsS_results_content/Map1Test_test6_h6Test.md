## New input1:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(0));
    v01.put("102", BigDecimal.valueOf(0));
```
Explanation: This input is valid because it contains two entries with the key "101" and "102" and their corresponding values are both 0. This is a common scenario where the values are not significant and can be set to 0.

## New input2:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(999999999));
    v01.put("102", BigDecimal.valueOf(999999999));
```
Explanation: This input is valid because it contains two entries with the key "101" and "102" and their corresponding values are both 999999999. This is a common scenario where the values are large and can be set to a large number.

## New input3:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(-1));
    v01.put("102", BigDecimal.valueOf(-1));
```
Explanation: This input is valid because it contains two entries with the key "101" and "102" and their corresponding values are both -1. This is a common scenario where the values are negative and can be set to -1.

## New input4:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(Double.MAX_VALUE));
    v01.put("102", BigDecimal.valueOf(Double.MAX_VALUE));
```
Explanation: This input is valid because it contains two entries with the key "101" and "102" and their corresponding values are both the maximum value that can be represented by a double. This is a common scenario where the values are very large and can be set to the maximum double value.

## New input5:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(Double.MIN_VALUE));
    v01.put("102", BigDecimal.valueOf(Double.MIN_VALUE));
```
Explanation: This input is valid because it contains two entries with the key "101" and "102" and their corresponding values are both the minimum value that can be represented by a double. This is a common scenario where the values are very small and can be set to the minimum double value.
