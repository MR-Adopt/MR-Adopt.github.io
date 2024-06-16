## New input1:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with two historicals, each having the same number of segments as the original tier. This scenario simulates a tier that is already balanced in terms of segment counts per data source.

## New input2:
```java
    String tier = "tier3";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with three historicals, each having the same number of segments as the original tier. This scenario simulates a tier that is already balanced in terms of segment counts per data source.

## New input3:
```java
    String tier = "tier4";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with two historicals, one of which has no segments. This scenario simulates a tier that is highly skewed towards one historical, with the other two having no segments.

## New input4:
```java
    String tier = "tier5";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", Collections.emptyList()), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with two historicals, one of which has no segments. This scenario simulates a tier that is highly skewed towards one historical, with the other two having segments.

## New input5:
```java
    String tier = "tier6";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with four historicals, each having the same number of segments as the original tier. This scenario simulates a tier that is already balanced in terms of segment counts per data source.
