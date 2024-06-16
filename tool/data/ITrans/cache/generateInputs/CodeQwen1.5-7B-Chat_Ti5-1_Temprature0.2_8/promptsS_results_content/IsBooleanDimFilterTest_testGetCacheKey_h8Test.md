## New input1:
```java
    EqualityFilter f3 = new EqualityFilter("y", ColumnType.STRING, "hello", null);
```
Explanation: This input is valid because it changes the attribute name from "x" to "y", which is a different attribute.

## New input2:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.INTEGER, "hello", null);
```
Explanation: This input is valid because it changes the data type from STRING to INTEGER, which is a different data type.

## New input3:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "world", null);
```
Explanation: This input is valid because it changes the value from "hello" to "world", which is a different value.

## New input4:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "hello", "en");
```
Explanation: This input is valid because it adds a language parameter to the filter, which is a different scenario.

## New input5:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "hello", "fr");
```
Explanation: This input is valid because it adds a different language parameter to the filter, which is a different scenario.
