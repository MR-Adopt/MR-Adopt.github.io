# ORIGINAL TEST CASE
```java
@Test
void testEqualsAndHashCode() {
    FieldDefinition subject = new FieldDefinition("foo", TokenType.STRING);
    var same = new FieldDefinition(NAME, TOKEN_TYPE);
    var other1 = new FieldDefinition(NAME, TokenType.INT);
    var other2 = new FieldDefinition("Bar", TOKEN_TYPE);
    FieldDefinition other3 = new FieldDefinition("foo", TokenType.STRING).deprecate();
    assertNotEquals(other3.hashCode(), subject.hashCode());
}

```
SOURCE INPUT: `subject`
FOLLOW UP INPUT: `other3`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return Objects.hash(name, type, deprecated);
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    FieldDefinition subject = new FieldDefinition("", TokenType.STRING);
```

## New source input1:
```java
    FieldDefinition subject = new FieldDefinition("foo", null);
```

## New source input2:
```java
    FieldDefinition subject = new FieldDefinition("foo", TokenType.STRING).deprecate();
```

## New source input3:
```java
    FieldDefinition subject = new FieldDefinition("foo", TokenType.STRING).setDescription("Description");
```

## New source input4:
```java
    FieldDefinition subject = new FieldDefinition("foo", TokenType.STRING).setDefaultValue("Default");
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    FieldDefinition subject = new FieldDefinition("foo", TokenType.STRING);
    FieldDefinition other3 = new FieldDefinition("foo", TokenType.STRING).deprecate();
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.