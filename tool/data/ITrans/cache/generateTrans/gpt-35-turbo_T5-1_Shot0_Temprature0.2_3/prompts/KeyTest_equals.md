# METHOD UNDER TEST
```java
public static <T> Key<T> get(TypeLiteral<T> typeLiteral, Annotation annotationInstance) {
    return new Key<>(typeLiteral, annotationInstance);
}

```


# TEST CASE
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


# OTHER INPUT PAIRS 
## Input pair1:
```java
Class<?> type1 = String.class;
Class<?> type2 = String.class;
```

## Input pair2:
```java
Class<?> type1 = Integer.class;
Class<?> type2 = Integer.class;
```

## Input pair3:
```java
Class<?> type1 = Double.class;
Class<?> type2 = Double.class;
```

## Input pair4:
```java
Class<?> type1 = List.class;
Class<?> type2 = List.class;
```

## Input pair5:
```java
Class<?> type1 = Object.class;
Class<?> type2 = Object.class;
```

## Input pair6:
```java
Class<?> type1 = Boolean.class;
Class<?> type2 = Boolean.class;
```

## Input pair7:
```java
Class<?> type1 = Map.class;
Class<?> type2 = Map.class;
```



# OUTPUT FORMAT
```java
public class KeyTest_equals {
    public static Class<?> inputTransformation_equals(Class<?> type1)  {
        // TODO
        Class<?> type2 = 
		return type2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.