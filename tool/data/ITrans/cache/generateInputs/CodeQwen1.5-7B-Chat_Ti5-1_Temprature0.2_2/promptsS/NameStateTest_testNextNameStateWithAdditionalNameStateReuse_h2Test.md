# ORIGINAL TEST CASE
```java
@Test
public void testNextNameStateWithAdditionalNameStateReuse() {
    NameState nameState = new NameState();
    NameState nextNameState = new NameState();
    String key = "key";
    String key2 = "key";
    NameState nameState2 = nameState;
    nameState.addNextNameState(key, nextNameState);
    assertEquals(nextNameState, nameState2.getNextNameState(key2));
// nameState.removeNextNameState("key");
// assertNull(nameState.getNextNameState("key"));
}

```
TEST INPUT: `key`,`nextNameState`


# METHOD UNDER TEST
```java
void addNextNameState(final String key, final NameState nextNameState) {
    keyToNextNameState.put(key, nextNameState);
}

public NameState getNextNameState(String key) {
    return keyToNextNameState.get(key);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `key`,`nextNameState`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    NameState nextNameState = new NameState();
    String key = "key";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 