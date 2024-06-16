## New input1:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```
Explanation: In this input, we have two historical servers in the tier, both containing the same number of segments. This input is valid as it represents a scenario where there is no skew in terms of segment counts between the historical servers.

## New input2:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: In this input, we have three historical servers in the tier, all containing the same number of segments. This input is valid as it represents a scenario where there is no skew in terms of segment counts between the historical servers.

## New input3:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
```
Explanation: In this input, we have three historical servers in the tier, with one server containing no segments. This input is valid as it represents a scenario where there is skew in terms of segment counts between the historical servers.

## New input4:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
```
Explanation: In this input, we have four historical servers in the tier, all containing the same number of segments. This input is valid as it represents a scenario where there is no skew in terms of segment counts between the historical servers.

## New input5:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", Collections.emptyList()));
```
Explanation: In this input, we have four historical servers in the tier, with one server containing no segments. This input is valid as it represents a scenario where there is skew in terms of segment counts between the historical servers.