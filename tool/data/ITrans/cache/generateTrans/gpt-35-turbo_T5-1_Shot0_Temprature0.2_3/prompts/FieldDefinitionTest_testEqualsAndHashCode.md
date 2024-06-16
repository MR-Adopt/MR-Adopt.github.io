# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return Objects.hash(name, type, deprecated);
}

```


# TEST CASE
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


# OTHER INPUT PAIRS 
## Input pair1:
```java
FieldDefinition subject = new FieldDefinition("foo", TokenType.STRING);
FieldDefinition other3 = new FieldDefinition("foo", TokenType.STRING).deprecate();
```

## Input pair2:
```java
FieldDefinition subject = new FieldDefinition("", TokenType.STRING);
FieldDefinition other3 = new FieldDefinition("", TokenType.STRING).deprecate();
```

## Input pair3:
```java
FieldDefinition subject = new FieldDefinition("foo", TokenType.INT);
FieldDefinition other3 = new FieldDefinition("foo", TokenType.INT).deprecate();
```

## Input pair4:
```java
FieldDefinition subject = new FieldDefinition("bar", TokenType.INT);
FieldDefinition other3 = new FieldDefinition("bar", TokenType.INT).deprecate();
```



# OUTPUT FORMAT
```java
public class FieldDefinitionTest_testEqualsAndHashCode {
    public static FieldDefinition inputTransformation_testEqualsAndHashCode(FieldDefinition subject)  {
        // TODO
        FieldDefinition other3 = 
		return other3;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.