## New input1:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```
Explanation: This input is valid because it tests the scenario where the tier has two servers with the same number of segments. This scenario can occur when the cluster is initially set up with an even distribution of segments across the servers.

## New input2:
```java
    String tier = "tier3";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", Collections.emptyList()), createServer("B", WIKI_SEGMENTS));
```
Explanation: This input is valid because it tests the scenario where the tier has one server with no segments and another server with the same number of segments. This scenario can occur when a server fails or is decommissioned.

## New input3:
```java
    String tier = "tier4";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: This input is valid because it tests the scenario where the tier has three servers with the same number of segments. This scenario can occur when the cluster is initially set up with an uneven distribution of segments across the servers.

## New input4:
```java
    String tier = "tier5";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
```
Explanation: This input is valid because it tests the scenario where the tier has four servers with the same number of segments. This scenario can occur when a server fails or is decommissioned.

## New input5:
```java
    String tier = "tier6";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", Collections.emptyList()));
```
Explanation: This input is valid because it tests the scenario where the tier has four servers with the same number of segments, but one server has no segments. This scenario can occur when a server fails or is decommissioned.
