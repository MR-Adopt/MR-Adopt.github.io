# ORIGINAL TEST CASE
```java
@Test
void testGetNewEvents() {
    Filter.FilterEvent mockEvent = new FilterEventMock();
    Filter filter = new Filter();
    filter.add(mockEvent);
    Filter.FilterEvent mockEvent2 = new FilterEventMock();
    Filter filter2 = new Filter();
    filter2.add(mockEvent2);
    Object[] events1 = filter2.getNewEvents();
    assertArrayEquals(new Object[] { mockEvent.getJsonEventObject() }, events1);
}

```
TEST INPUT: `mockEvent`,`filter`


# METHOD UNDER TEST
```java
protected synchronized void add(FilterEvent evt) {
    events.add(evt);
}

public synchronized Object[] getNewEvents() {
    this.accessTime = System.currentTimeMillis();
    Object[] ret = events.stream().skip(processedEvents).map(fe -> fe.getJsonEventObject()).collect(Collectors.toList()).toArray();
    processedEvents = events.size();
    return ret;
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `mockEvent`,`filter`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Filter.FilterEvent mockEvent = new FilterEventMock();
    Filter filter = new Filter();
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 