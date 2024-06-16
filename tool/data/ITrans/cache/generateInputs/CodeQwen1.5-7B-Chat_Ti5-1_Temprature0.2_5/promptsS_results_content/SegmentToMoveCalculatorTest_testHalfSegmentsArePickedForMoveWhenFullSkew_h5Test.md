## New input1:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates two servers in the tier "tier1", with server "A" having segments and server "B" having no segments. This scenario simulates a tier with a balanced number of segments across both servers.

## New input2:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", Collections.emptyList()), createServer("B", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates two servers in the tier "tier1", with server "A" having no segments and server "B" having segments. This scenario simulates a tier with an imbalanced number of segments, with server "B" having more segments than server "A".

## New input3:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates three servers in the tier "tier1", with server "A", "B", and "C" each having segments. This scenario simulates a tier with a large number of servers, each having a balanced number of segments.

## New input4:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", Collections.emptyList()));
```
Explanation: This input is valid because it creates three servers in the tier "tier1", with server "A", "B", and "C" each having segments and server "C" having no segments. This scenario simulates a tier with an imbalanced number of segments, with server "A" and "B" having more segments than server "C".

## New input5:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", Collections.emptyList()), createServer("B", Collections.emptyList()));
```
Explanation: This input is valid because it creates two servers in the tier "tier1", with server "A" and "B" each having no segments. This scenario simulates a tier with no segments across both servers.
