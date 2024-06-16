# REQUIRED DELIVERABLE
## New input pair0:
```java
    FieldDefinition subject = new FieldDefinition("bar", TokenType.STRING);
    FieldDefinition other3 = new FieldDefinition("bar", TokenType.STRING).deprecate();
```
To satisfy the inferred relation, we can use the same `name` and `type` as `subject` but change the `deprecated` status. The `deprecated` status is the only field that differs between `subject` and `other3`.

## New input pair1:
```java
    FieldDefinition subject = new FieldDefinition("foo", TokenType.INT);
    FieldDefinition other3 = new FieldDefinition("foo", TokenType.INT).deprecate();
```
To satisfy the inferred relation, we can use the same `name` and `type` as `subject` but change the `deprecated` status. The `deprecated` status is the only field that differs between `subject` and `other3`.

## New input pair2:
```java
    FieldDefinition subject = new FieldDefinition("foo", TokenType.STRING).deprecate();
    FieldDefinition other3 = new FieldDefinition("foo", TokenType.STRING).deprecate();
```
To satisfy the inferred relation, we can use the same `name` and `type` as `subject` but change the `deprecated` status. The `deprecated` status is the only field that differs between `subject` and `other3`.

## New input pair3:
```java
    FieldDefinition subject = new FieldDefinition("", TokenType.STRING);
    FieldDefinition other3 = new FieldDefinition("", TokenType.STRING).deprecate();
```
To satisfy the inferred relation, we can use the same `name` and `type` as `subject` but change the `deprecated` status. The `deprecated` status is the only field that differs between `subject` and `other3`.

## New input pair4:
```java
    FieldDefinition subject = new FieldDefinition("foo", null);
    FieldDefinition other3 = new FieldDefinition("foo", null).deprecate();
```
To satisfy the inferred relation, we can use the same `name` and `type` as `subject` but change the `deprecated` status. The `deprecated` status is the only field that differs between `subject` and `other3`.
