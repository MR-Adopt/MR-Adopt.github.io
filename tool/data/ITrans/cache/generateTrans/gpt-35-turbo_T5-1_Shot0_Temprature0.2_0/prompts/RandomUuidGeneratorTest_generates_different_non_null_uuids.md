# METHOD UNDER TEST
```java
UUID generateId();

```


# TEST CASE
```java
@Test
void generates_different_non_null_uuids() {
    // Given
    UuidGenerator generator = new RandomUuidGenerator();
    UuidGenerator generator2 = new RandomUuidGenerator();
    UUID uuid1 = generator.generateId();
    // When
    UUID uuid2 = generator2.generateId();
    // Then
    assertNotEquals(uuid1, uuid2);
}

```
SOURCE INPUT: `generator`
FOLLOW UP INPUT: `generator2`


# OTHER INPUT PAIRS 



# OUTPUT FORMAT
```java
public class RandomUuidGeneratorTest_generates_different_non_null_uuids {
    public static UuidGenerator inputTransformation_generates_different_non_null_uuids(UuidGenerator generator)  {
        // TODO
        UuidGenerator generator2 = 
		return generator2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.