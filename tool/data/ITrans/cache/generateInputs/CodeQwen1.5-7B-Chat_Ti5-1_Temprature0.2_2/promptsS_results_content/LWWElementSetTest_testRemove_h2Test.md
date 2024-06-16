## New input1:
```java
    Element element = new Element("key1", 0, bias);
```
Explanation: This input is valid because the key is a string and the value is an integer. The bias is also provided. This input tests the edge case where the value is zero.

## New input2:
```java
    Element element = new Element("key1", Integer.MAX_VALUE, bias);
```
Explanation: This input is valid because the key is a string and the value is an integer. The bias is also provided. This input tests the edge case where the value is the maximum integer value.

## New input3:
```java
    Element element = new Element("key1", Integer.MIN_VALUE, bias);
```
Explanation: This input is valid because the key is a string and the value is an integer. The bias is also provided. This input tests the edge case where the value is the minimum integer value.

## New input4:
```java
    Element element = new Element("key1", -1, bias);
```
Explanation: This input is valid because the key is a string and the value is an integer. The bias is also provided. This input tests the edge case where the value is negative.

## New input5:
```java
    Element element = new Element("key1", 1, null);
```
Explanation: This input is valid because the key is a string and the value is an integer. The bias is not provided. This input tests the edge case where the bias is null.
