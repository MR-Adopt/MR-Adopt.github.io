# ORIGINAL TEST CASE
```java
@Test
void hashCodeEquals() {
    JsonNodePath root = new JsonNodePath(PathType.JSON_POINTER);
    JsonNodePath a1 = root.append("a");
    JsonNodePath a2 = root.append("a");
    assertEquals(a1.hashCode(), a2.hashCode());
}

```
TEST INPUT: `a1`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return Objects.hash(parent, pathSegment, pathSegmentIndex, type);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `a1`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    JsonNodePath root = new JsonNodePath(PathType.JSON_POINTER);
    JsonNodePath a1 = root.append("a");
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 