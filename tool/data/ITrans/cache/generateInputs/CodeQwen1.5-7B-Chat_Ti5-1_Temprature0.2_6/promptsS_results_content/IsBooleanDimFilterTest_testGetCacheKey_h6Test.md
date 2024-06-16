## New input1:
```java
    EqualityFilter f3 = new EqualityFilter("y", ColumnType.STRING, "hello", null);
```
Explanation: This input is valid because it changes the attribute name from "x" to "y". This change does not affect the filter's functionality, as the attribute name is not used in the filter's logic.

## New input2:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.INTEGER, "hello", null);
```
Explanation: This input is valid because it changes the column type from STRING to INTEGER. This change does not affect the filter's functionality, as the column type is not used in the filter's logic.

## New input3:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "world", null);
```
Explanation: This input is valid because it changes the value from "hello" to "world". This change does not affect the filter's functionality, as the value is not used in the filter's logic.

## New input4:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, null, null);
```
Explanation: This input is valid because it changes the value from "hello" to null. This change does not affect the filter's functionality, as the value is not used in the filter's logic.

## New input5:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "hello", "world");
```
Explanation: This input is valid because it changes the filter to use a range instead of a single value. This change does not affect the filter's functionality, as the range is not used in the filter's logic.
