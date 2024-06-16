# REQUIRED DELIVERABLE
## New input pair0:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "192.168.1.1");
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", "192.168.1.1");
```
## Explanation:
The inferred relation is that the hash codes of two `AuditInfo` objects are equal if they have the same author, identity, comment, and IP address. Since the source input `auditInfo1` has a different IP address ("192.168.1.1") than the follow-up input `auditInfo2` ("127.0.0.1"), the hash codes of these two objects will be different. Therefore, the new input pair satisfies the inferred relation.

## New input pair1:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "");
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", "");
```
## Explanation:
The inferred relation is that the hash codes of two `AuditInfo` objects are equal if they have the same author, identity, comment, and IP address. Since the source input `auditInfo1` has an empty string as the IP address ("") than the follow-up input `auditInfo2` (""), the hash codes of these two objects will be different. Therefore, the new input pair satisfies the inferred relation.

## New input pair2:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", null);
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", null);
```
## Explanation:
The inferred relation is that the hash codes of two `AuditInfo` objects are equal if they have the same author, identity, comment, and IP address. Since the source input `auditInfo1` has a null IP address (null) than the follow-up input `auditInfo2` (null), the hash codes of these two objects will be different. Therefore, the new input pair satisfies the inferred relation.

## New input pair3:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "127.0.0.1");
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", "127.0.0.1");
```
## Explanation:
The inferred relation is that the hash codes of two `AuditInfo` objects are equal if they have the same author, identity, comment, and IP address. Since the source input `auditInfo1` has the same IP address ("127.0.0.1") than the follow-up input `auditInfo2` ("127.0.0.1"), the hash codes of these two objects will be the same. Therefore, the new input pair satisfies the inferred relation.
