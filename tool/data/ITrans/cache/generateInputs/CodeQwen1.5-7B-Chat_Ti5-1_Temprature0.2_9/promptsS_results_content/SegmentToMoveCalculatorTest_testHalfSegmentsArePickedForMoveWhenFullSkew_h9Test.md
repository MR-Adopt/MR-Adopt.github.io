## New input1:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with two servers, both of which have the same number of segments. This will cause the method to move segments between the servers to balance the tier, as both servers have the same number of segments.

## New input2:
```java
    String tier = "tier3";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", Collections.emptyList()), createServer("B", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with one server with no segments and one server with the same number of segments as the other server. This will cause the method to move segments from the server with no segments to the server with the same number of segments, as the tier is not balanced.

## New input3:
```java
    String tier = "tier4";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with three servers, all of which have the same number of segments. This will cause the method to move segments between the servers to balance the tier, as all servers have the same number of segments.

## New input4:
```java
    String tier = "tier5";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", Collections.emptyList()));
```
Explanation: This input is valid because it creates a tier with two servers with the same number of segments and one server with no segments. This will cause the method to move segments from the server with no segments to the server with the same number of segments, as the tier is not balanced.

## New input5:
```java
    String tier = "tier6";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with four servers, all of which have the same number of segments. This will cause the method to move segments between the servers to balance the tier, as all servers have the same number of segments.
