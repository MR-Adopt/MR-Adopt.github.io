# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return Objects.hashCode(group);
}

```


# TEST CASE
```java
@Test
public void testInFlightRequestKey() {
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 1);
    Assert.assertEquals(requestKey1.hashCode(), requestKey2.hashCode());
}

```
SOURCE INPUT: `requestKey1`
FOLLOW UP INPUT: `requestKey2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 1);
```

## Input pair2:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("", 0, 0);
InFlightRequestKey requestKey2 = new InFlightRequestKey("", 1, 1);
```

## Input pair3:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey(null, 0, 0);
InFlightRequestKey requestKey2 = new InFlightRequestKey(null, 1, 1);
```

## Input pair4:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("anotherGroup", 0, 0);
InFlightRequestKey requestKey2 = new InFlightRequestKey("anotherGroup", 1, 1);
```

## Input pair5:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 1, 0);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 1);
```

## Input pair6:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group", -1, 0);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group", -1, 1);
```

## Input pair7:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group1", 0, 0);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group1", 1, 1);
```

## Input pair8:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 100, 100);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 101, 101);
```

## Input pair9:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group", -1, -1);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group", -2, -2);
```

## Input pair10:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 0, 1);
```

## Input pair11:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group2", 0, 0);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group2", 1, 1);
```

## Input pair12:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 1);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 1);
```

## Input pair13:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group2", 1, 1);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group2", 2, 2);
```

## Input pair14:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group3", 2, 2);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group3", 3, 3);
```

## Input pair15:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 10, 0);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 10, 1);
```

## Input pair16:
```java
InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 10);
InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 10);
```



# OUTPUT FORMAT
```java
public class InFlightRequestFutureTest_testInFlightRequestKey {
    public static InFlightRequestKey inputTransformation_testInFlightRequestKey(InFlightRequestKey requestKey1)  {
        // TODO
        InFlightRequestKey requestKey2 = 
		return requestKey2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.