# ORIGINAL TEST CASE
```java
@Test
public void testAuditInfoEquality() {
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "127.0.0.1");
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", "127.0.0.1");
    Assert.assertEquals(auditInfo1.hashCode(), auditInfo2.hashCode());
}

```
TEST INPUT: `auditInfo1`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return Objects.hash(author, identity, comment, ip);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `auditInfo1`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "127.0.0.1");
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 