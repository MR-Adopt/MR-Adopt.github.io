## New input1:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(0));
    v01.put("102", BigDecimal.valueOf(0));
```
Explanation: This input is valid because it contains two key-value pairs with the values set to 0. This is a common scenario where the values are not significant and can be considered as default values.

## New input2:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(999999999));
    v01.put("102", BigDecimal.valueOf(888888888));
```
Explanation: This input is valid because it contains two key-value pairs with very large values. This is a common scenario where the values are large and can be considered as out-of-bound values.

## New input3:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(-1));
    v01.put("102", BigDecimal.valueOf(-2));
```
Explanation: This input is valid because it contains two key-value pairs with negative values. This is a common scenario where the values are negative and can be considered as invalid or error values.

## New input4:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(Double.MAX_VALUE));
    v01.put("102", BigDecimal.valueOf(Double.MIN_VALUE));
```
Explanation: This input is valid because it contains two key-value pairs with the maximum and minimum double values. This is a common scenario where the values are extreme and can be considered as boundary values.

## New input5:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(Long.MAX_VALUE));
    v01.put("102", BigDecimal.valueOf(Long.MIN_VALUE));
```
Explanation: This input is valid because it contains two key-value pairs with the maximum and minimum long values. This is a common scenario where the values are extreme and can be considered as boundary values.
