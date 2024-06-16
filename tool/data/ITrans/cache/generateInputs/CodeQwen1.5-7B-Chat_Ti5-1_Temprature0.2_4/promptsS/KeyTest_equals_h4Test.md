# ORIGINAL TEST CASE
```java
@Test
public void equals() {
    Class<?> type1 = String.class;
    Class<?> type2 = String.class;
    Key<?> key1 = Key.get(type1);
    Key<?> key2 = Key.get(type2);
    Key<Integer> key3 = Key.get(Integer.class);
    Key<Integer> key4 = Key.get(Integer.class, "a");
    Key<Integer> key5 = Key.get(Integer.class, "a");
    Key<Integer> key6 = Key.get(Integer.class, "b");
    Key<String> key7 = Key.get(String.class, "a");
    Key<Integer> key8 = Key.get(Integer.class, "");
    assertTrue(key1.equals(key2));
}

```
TEST INPUT: `type1`


# METHOD UNDER TEST
```java
public static <T> Key<T> get(TypeLiteral<T> typeLiteral, Annotation annotationInstance) {
    return new Key<>(typeLiteral, annotationInstance);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `type1`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Class<?> type1 = String.class;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 