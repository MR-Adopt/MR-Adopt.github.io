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
SOURCE INPUT: `type1`
FOLLOW UP INPUT: `type2`


# METHOD UNDER TEST
```java
public static <T> Key<T> get(TypeLiteral<T> typeLiteral, Annotation annotationInstance) {
    return new Key<>(typeLiteral, annotationInstance);
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    Class<?> type1 = Integer.class;
```

## New source input1:
```java
    Class<?> type1 = List.class;
```

## New source input2:
```java
    Class<?> type1 = Object.class;
```

## New source input3:
```java
    Class<?> type1 = Double.class;
```

## New source input4:
```java
    Class<?> type1 = Map.class;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    Class<?> type1 = String.class;
    Class<?> type2 = String.class;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.