# ORIGINAL TEST CASE
```java
@Test
void equalsEquals() {
    JsonNodePath root = new JsonNodePath(PathType.JSON_POINTER);
    String token1 = "a";
    String token2 = "a";
    JsonNodePath a1 = root.append(token1);
    JsonNodePath a2 = root.append(token2);
    assertEquals(a1, a2);
}

```
TEST INPUT: `token1`


# METHOD UNDER TEST
```java
/**
 * Append the index to the path.
 *
 * @param index the index
 * @return the path
 */
public JsonNodePath append(int index) {
    return new JsonNodePath(this, index);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `token1`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    String token1 = "a";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 