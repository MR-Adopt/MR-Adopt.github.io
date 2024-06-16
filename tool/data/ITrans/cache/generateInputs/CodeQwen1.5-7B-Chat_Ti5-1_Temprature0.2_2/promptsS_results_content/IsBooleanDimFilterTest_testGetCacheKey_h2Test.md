## New input1:
```java
    EqualityFilter f3 = new EqualityFilter("y", ColumnType.STRING, "hello", null);
```
Explanation: This input is valid because it changes the attribute name from "x" to "y". This change does not affect the filter's functionality, as the filter is checking for equality with the value "hello" regardless of the attribute name.

## New input2:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.INTEGER, "hello", null);
```
Explanation: This input is valid because it changes the data type from STRING to INTEGER. This change does not affect the filter's functionality, as the filter is checking for equality with the value "hello" regardless of the data type.

## New input3:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "world", null);
```
Explanation: This input is valid because it changes the value being checked from "hello" to "world". This change does not affect the filter's functionality, as the filter is checking for equality with the value "hello" regardless of the value being checked.

## New input4:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, null, null);
```
Explanation: This input is valid because it changes the value being checked from "hello" to null. This change does not affect the filter's functionality, as the filter is checking for equality with the value "hello" regardless of the value being checked.

## New input5:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "hello", "world");
```
Explanation: This input is valid because it adds a filter context to the filter. This change does not affect the filter's functionality, as the filter is checking for equality with the value "hello" regardless of the filter context.
