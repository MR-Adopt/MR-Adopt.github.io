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
SOURCE INPUT: `key`,`nextNameState`
FOLLOW UP INPUT: `key2`,`nameState2`


# METHOD UNDER TEST
```java
void addNextNameState(final String key, final NameState nextNameState) {
    keyToNextNameState.put(key, nextNameState);
}

public NameState getNextNameState(String key) {
    return keyToNextNameState.get(key);
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    NameState nextNameState = new NameState();
    String key = "";
```

## New source input1:
```java
    NameState nextNameState = null;
    String key = "key";
```

## New source input2:
```java
    NameState nextNameState = new NameState();
    String key = "key2";
```

## New source input3:
```java
    NameState nextNameState = new NameState();
    String key = "key";
```

## New source input4:
```java
    NameState nextNameState = new NameState();
    String key = "key";
    nextNameState.addNextNameState("key2", new NameState());
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    NameState nameState = new NameState();
    NameState nextNameState = new NameState();
    String key = "key";
    String key2 = "key";
    NameState nameState2 = nameState;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.