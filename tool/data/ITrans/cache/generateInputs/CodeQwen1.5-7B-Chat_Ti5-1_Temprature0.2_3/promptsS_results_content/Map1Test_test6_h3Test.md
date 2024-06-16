## New input1:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(0));
    v01.put("102", BigDecimal.valueOf(0));
```
Explanation: This input is valid because it contains two entries with the same key "101" and "102", both of which have a value of 0. This is a common scenario in financial calculations, where it is possible to have multiple entries with the same key but different values.

## New input2:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(1000000000));
    v01.put("102", BigDecimal.valueOf(2000000000));
```
Explanation: This input is valid because it contains two entries with different keys "101" and "102", and both of which have a value of 1,000,000,000. This is a common scenario in financial calculations, where it is possible to have multiple entries with different values.

## New input3:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(-101));
    v01.put("102", BigDecimal.valueOf(-102));
```
Explanation: This input is valid because it contains two entries with different keys "101" and "102", and both of which have a negative value. This is a common scenario in financial calculations, where it is possible to have negative values.

## New input4:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(Double.MAX_VALUE));
    v01.put("102", BigDecimal.valueOf(Double.MAX_VALUE));
```
Explanation: This input is valid because it contains two entries with different keys "101" and "102", and both of which have a value of the maximum double value. This is a common scenario in financial calculations, where it is possible to have large values.

## New input5:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(Double.MIN_VALUE));
    v01.put("102", BigDecimal.valueOf(Double.MIN_VALUE));
```
Explanation: This input is valid because it contains two entries with different keys "101" and "102", and both of which have a value of the minimum double value. This is a common scenario in financial calculations, where it is possible to have small values.
