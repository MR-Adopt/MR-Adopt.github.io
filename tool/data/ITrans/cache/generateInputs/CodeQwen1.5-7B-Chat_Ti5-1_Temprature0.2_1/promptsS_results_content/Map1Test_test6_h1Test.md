## New input1:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(0));
    v01.put("102", BigDecimal.valueOf(0));
```
Explanation: This input is valid because it contains two key-value pairs with the same key "101" and "102" and the corresponding values are both 0. This is a common scenario in financial calculations and can be used to test the program's handling of zero values.

## New input2:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(999999999999999999L));
    v01.put("102", BigDecimal.valueOf(888888888888888888L));
```
Explanation: This input is valid because it contains two key-value pairs with the same key "101" and "102" and the corresponding values are both very large numbers. This is a common scenario in financial calculations and can be used to test the program's handling of large numbers.

## New input3:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(-101));
    v01.put("102", BigDecimal.valueOf(-102));
```
Explanation: This input is valid because it contains two key-value pairs with the same key "101" and "102" and the corresponding values are both negative numbers. This is a common scenario in financial calculations and can be used to test the program's handling of negative numbers.

## New input4:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(Double.MAX_VALUE));
    v01.put("102", BigDecimal.valueOf(Double.MIN_VALUE));
```
Explanation: This input is valid because it contains two key-value pairs with the same key "101" and "102" and the corresponding values are both the maximum and minimum double values. This is a common scenario in financial calculations and can be used to test the program's handling of extreme double values.

## New input5:
```java
    Map<String, BigDecimal> v01 = new HashMap<>();
    v01.put("101", BigDecimal.valueOf(0));
    v01.put("102", BigDecimal.valueOf(0));
    v01.put("103", BigDecimal.valueOf(0));
```
Explanation: This input is valid because it contains three key-value pairs with the same key "101" and "102" and the corresponding values are both 0. This is a common scenario in financial calculations and can be used to test the program's handling of multiple zero values.
