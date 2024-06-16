# REQUIRED DELIVERABLE
## New input pair0:
```java
    EqualityFilter f3 = new EqualityFilter("y", ColumnType.STRING, "hello", null);
    EqualityFilter f4 = new EqualityFilter("y", ColumnType.STRING, "hello", null);
```
### Explanation:
The inferred relation is that the cache keys of `f1_3` and `f1_4` are equal. To satisfy this relation, we need to create a new `EqualityFilter` object `f3` with the same field name ("y"), column type (`ColumnType.STRING`), value ("hello"), and filter (null). Since the field name and value are the same, the cache keys of `f1_3` and `f1_4` will also be equal.

## New input pair1:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.INTEGER, "hello", null);
    EqualityFilter f4 = new EqualityFilter("x", ColumnType.INTEGER, "hello", null);
```
### Explanation:
The inferred relation is that the cache keys of `f1_3` and `f1_4` are equal. To satisfy this relation, we need to create a new `EqualityFilter` object `f3` with the same field name ("x"), column type (`ColumnType.INTEGER`), value ("hello"), and filter (null). Since the field name and value are the same, the cache keys of `f1_3` and `f1_4` will also be equal.

## New input pair2:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "world", null);
    EqualityFilter f4 = new EqualityFilter("x", ColumnType.STRING, "world", null);
```
### Explanation:
The inferred relation is that the cache keys of `f1_3` and `f1_4` are equal. To satisfy this relation, we need to create a new `EqualityFilter` object `f3` with the same field name ("x"), column type (`ColumnType.STRING`), value ("world"), and filter (null). Since the field name and value are the same, the cache keys of `f1_3` and `f1_4` will also be equal.

## New input pair3:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, null, null);
    EqualityFilter f4 = new EqualityFilter("x", ColumnType.STRING, null, null);
```
### Explanation:
The inferred relation is that the cache keys of `f1_3` and `f1_4` are equal. To satisfy this relation, we need to create a new `EqualityFilter` object `f3` with the same field name ("x"), column type (`ColumnType.STRING`), value (null), and filter (null). Since the field name and value are the same, the cache keys of `f1_3` and `f1_4` will also be equal.

## New input pair4:
```java
    EqualityFilter f3 = new EqualityFilter("x", ColumnType.STRING, "hello", "world");
    EqualityFilter f4 = new EqualityFilter("x", ColumnType.STRING, "hello", "world");
```
### Explanation:
The inferred relation is that the cache keys of `f1_3` and `f1_4` are equal. To satisfy this relation, we need to create a new `EqualityFilter` object `f3` with the same field name ("x"), column type (`ColumnType.STRING`), value ("hello"), and filter ("world"). Since the field name and value are the same, the cache keys of `f1_3` and `f1_4` will also be equal.
