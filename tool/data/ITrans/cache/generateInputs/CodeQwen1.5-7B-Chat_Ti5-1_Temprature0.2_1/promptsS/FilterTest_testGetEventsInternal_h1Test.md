# ORIGINAL TEST CASE
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
TEST INPUT: `filter`


# METHOD UNDER TEST
```java
@VisibleForTesting
List<FilterEvent> getEventsInternal() {
    return new ArrayList<>(events);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `filter`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Filter filter = new Filter();
    filter.add(mockEvent1);
    filter.add(mockEvent2);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 