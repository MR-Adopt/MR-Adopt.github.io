## New input1:
```java
    Filter.FilterEvent mockEvent = new FilterEventMock("Event1", "Type1", "Description1");
    Filter filter = new Filter();
```
Explanation: This input creates a new `FilterEvent` object with a unique event name, type, and description. This ensures that the `getNewEvents` method will return the new event when called.

## New input2:
```java
    Filter.FilterEvent mockEvent = new FilterEventMock(null, "Type1", "Description1");
    Filter filter = new Filter();
```
Explanation: This input creates a new `FilterEvent` object with a null event name. This ensures that the `getNewEvents` method will still return the event when called, as the method handles null event names gracefully.

## New input3:
```java
    Filter.FilterEvent mockEvent = new FilterEventMock("Event1", null, "Description1");
    Filter filter = new Filter();
```
Explanation: This input creates a new `FilterEvent` object with a null event type. This ensures that the `getNewEvents` method will still return the event when called, as the method handles null event types gracefully.

## New input4:
```java
    Filter.FilterEvent mockEvent = new FilterEventMock("Event1", "Type1", null);
    Filter filter = new Filter();
```
Explanation: This input creates a new `FilterEvent` object with a null event description. This ensures that the `getNewEvents` method will still return the event when called, as the method handles null event descriptions gracefully.

## New input5:
```java
    Filter.FilterEvent mockEvent = new FilterEventMock("Event1", "Type1", "Description1");
    Filter filter = new Filter();
    filter.add(mockEvent);
    Filter.FilterEvent mockEvent2 = new FilterEventMock("Event2", "Type2", "Description2");
```
Explanation: This input creates a new `FilterEvent` object and adds it to the `filter` before creating a second `FilterEvent` object. This ensures that the `getNewEvents` method will return the second event when called, as the first event has already been processed.
