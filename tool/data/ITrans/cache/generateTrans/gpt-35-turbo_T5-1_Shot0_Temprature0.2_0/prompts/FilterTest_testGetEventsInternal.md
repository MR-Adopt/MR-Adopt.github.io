# METHOD UNDER TEST
```java
@VisibleForTesting
List<FilterEvent> getEventsInternal() {
    return new ArrayList<>(events);
}

```


# TEST CASE
```java
@Test
void testGetEventsInternal() {
    Filter.FilterEvent mockEvent1 = new FilterEventMock();
    Filter.FilterEvent mockEvent2 = new FilterEventMock();
    Filter filter = new Filter();
    filter.add(mockEvent1);
    filter.add(mockEvent2);
    // get the internal events list and make sure it's a copy of the original list
    List<Filter.FilterEvent> events = filter.getEventsInternal();
    Filter filter2 = new Filter();
    filter2.add(mockEvent1);
    filter2.add(mockEvent2);
    filter2.getEventsInternal();
    assertNotSame(events, filter2.getEventsInternal());
}

```
SOURCE INPUT: `filter`
FOLLOW UP INPUT: `filter2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
Filter filter = new Filter();
filter.add(mockEvent1);
filter.add(mockEvent2);
Filter filter2 = new Filter();
filter2.add(mockEvent1);
filter2.add(mockEvent2);
```

## Input pair2:
```java
Filter filter = new Filter();
filter.add(mockEvent1);
filter.add(mockEvent2);
filter.add(mockEvent1);
Filter filter2 = new Filter();
filter2.add(mockEvent1);
filter2.add(mockEvent2);
filter2.add(mockEvent1);
```

## Input pair3:
```java
Filter filter = new Filter();
filter.add(mockEvent1);
filter.add(mockEvent2);
filter.add(new FilterEventMock());
Filter filter2 = new Filter();
filter2.add(mockEvent1);
filter2.add(mockEvent2);
filter2.add(new FilterEventMock());
```

## Input pair4:
```java
Filter filter = new Filter();
Filter filter2 = new Filter();
```

## Input pair5:
```java
Filter filter = new Filter();
filter.add(mockEvent1);
Filter filter2 = new Filter();
filter2.add(mockEvent1);
```

## Input pair6:
```java
Filter filter = new Filter();
filter.add(mockEvent2);
Filter filter2 = new Filter();
filter2.add(mockEvent2);
```

## Input pair7:
```java
Filter filter = new Filter();
filter.add(mockEvent2);
filter.add(mockEvent1);
filter.add(mockEvent2);
Filter filter2 = new Filter();
filter2.add(mockEvent2);
filter2.add(mockEvent1);
filter2.add(mockEvent2);
```



# OUTPUT FORMAT
```java
public class FilterTest_testGetEventsInternal {
    public static Filter inputTransformation_testGetEventsInternal(Filter filter)  {
        // TODO
        Filter filter2 = 
		return filter2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.