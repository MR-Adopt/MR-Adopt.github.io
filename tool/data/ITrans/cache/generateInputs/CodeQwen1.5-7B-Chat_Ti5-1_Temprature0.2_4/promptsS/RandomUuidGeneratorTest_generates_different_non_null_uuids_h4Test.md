# ORIGINAL TEST CASE
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
TEST INPUT: `generator`


# METHOD UNDER TEST
```java
UUID generateId();

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `generator`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    UuidGenerator generator = new RandomUuidGenerator();
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 