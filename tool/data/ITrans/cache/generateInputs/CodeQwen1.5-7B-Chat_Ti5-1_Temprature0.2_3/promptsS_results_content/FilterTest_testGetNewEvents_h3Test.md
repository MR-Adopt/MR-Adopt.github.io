## New input1:
```java
    Filter.FilterEvent mockEvent = new FilterEventMock("Event1", "2022-01-01", "Category1");
    Filter filter = new Filter();
```
Explanation: This input is valid because it creates a `FilterEvent` with a unique event name, date, and category. This ensures that the event is not a duplicate of the original event and that the filter can handle a variety of event types.

## New input2:
```java
    Filter.FilterEvent mockEvent = new FilterEventMock("Event2", "2022-12-31", "Category2");
    Filter filter = new Filter();
```
Explanation: This input is valid because it creates a `FilterEvent` with a unique event name, date, and category. This ensures that the event is not a duplicate of the original event and that the filter can handle a variety of event types.

## New input3:
```java
    Filter.FilterEvent mockEvent = new FilterEventMock("Event3", "2022-06-15", "Category3");
    Filter filter = new Filter();
```
Explanation: This input is valid because it creates a `FilterEvent` with a unique event name, date, and category. This ensures that the event is not a duplicate of the original event and that the filter can handle a variety of event types.

## New input4:
```java
    Filter.FilterEvent mockEvent = new FilterEventMock("Event4", "2022-01-01", "Category1");
    Filter filter = new Filter();
```
Explanation: This input is valid because it creates a `FilterEvent` with the same event name, date, and category as the original event. This ensures that the filter can handle duplicate events and that the filter's behavior does not change when duplicate events are added.

## New input5:
```java
    Filter.FilterEvent mockEvent = new FilterEventMock("Event5", "2022-01-01", "");
    Filter filter = new Filter();
```
Explanation: This input is valid because it creates a `FilterEvent` with an empty category. This ensures that the filter can handle events with no category and that the filter's behavior does not change when events with no category are added.
