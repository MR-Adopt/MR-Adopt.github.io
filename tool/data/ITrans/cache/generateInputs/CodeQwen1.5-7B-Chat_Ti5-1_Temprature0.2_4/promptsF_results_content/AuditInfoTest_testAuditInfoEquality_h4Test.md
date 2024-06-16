# REQUIRED DELIVERABLE
## New input pair0:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "192.168.1.1");
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", "192.168.1.1");
```
### Explanation:
The inferred relation between the source and follow-up inputs is that the `ip` fields of the `AuditInfo` objects should be equal. The new input pair `auditInfo1` and `auditInfo2` have the same `ip` field value "192.168.1.1", which satisfies the inferred relation.

## New input pair1:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "10.0.0.1");
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", "10.0.0.1");
```
### Explanation:
The inferred relation between the source and follow-up inputs is that the `ip` fields of the `AuditInfo` objects should be equal. The new input pair `auditInfo1` and `auditInfo2` have the same `ip` field value "10.0.0.1", which satisfies the inferred relation.

## New input pair2:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "172.16.0.1");
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", "172.16.0.1");
```
### Explanation:
The inferred relation between the source and follow-up inputs is that the `ip` fields of the `AuditInfo` objects should be equal. The new input pair `auditInfo1` and `auditInfo2` have the same `ip` field value "172.16.0.1", which satisfies the inferred relation.

## New input pair3:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "192.168.0.1");
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", "192.168.0.1");
```
### Explanation:
The inferred relation between the source and follow-up inputs is that the `ip` fields of the `AuditInfo` objects should be equal. The new input pair `auditInfo1` and `auditInfo2` have the same `ip` field value "192.168.0.1", which satisfies the inferred relation.

## New input pair4:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "8.8.8.8");
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", "8.8.8.8");
```
### Explanation:
The inferred relation between the source and follow-up inputs is that the `ip` fields of the `AuditInfo` objects should be equal. The new input pair `auditInfo1` and `auditInfo2` have the same `ip` field value "8.8.8.8", which satisfies the inferred relation.
