# ORIGINAL TEST CASE
```java
@Test
public void testAuditInfoEquality() {
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "127.0.0.1");
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", "127.0.0.1");
    Assert.assertEquals(auditInfo1.hashCode(), auditInfo2.hashCode());
}

```
SOURCE INPUT: `auditInfo1`
FOLLOW UP INPUT: `auditInfo2`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return Objects.hash(author, identity, comment, ip);
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    AuditInfo auditInfo1 = new AuditInfo(null, "id", "test equality", "127.0.0.1");
```

## New source input1:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", null, "test equality", "127.0.0.1");
```

## New source input2:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", null, "127.0.0.1");
```

## New source input3:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", null);
```

## New source input4:
```java
    AuditInfo auditInfo1 = new AuditInfo("", "id", "test equality", "127.0.0.1");
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    AuditInfo auditInfo1 = new AuditInfo("druid", "id", "test equality", "127.0.0.1");
    AuditInfo auditInfo2 = new AuditInfo("druid", "id", "test equality", "127.0.0.1");
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.