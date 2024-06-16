## New input1:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```
Explanation: In this input, we have two historical servers in the `tier1` tier, both containing the same number of segments. This input is valid as it represents a scenario where there is no skew in terms of segment counts between the historicals.

## New input2:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: In this input, we have three historical servers in the `tier2` tier, all containing the same number of segments. This input is valid as it represents a scenario where there is no skew in terms of segment counts between the historicals.

## New input3:
```java
    String tier = "tier3";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
```
Explanation: In this input, we have four historical servers in the `tier3` tier, all containing the same number of segments. This input is valid as it represents a scenario where there is no skew in terms of segment counts between the historicals.

## New input4:
```java
    String tier = "tier4";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS), createServer("E", WIKI_SEGMENTS));
```
Explanation: In this input, we have five historical servers in the `tier4` tier, all containing the same number of segments. This input is valid as it represents a scenario where there is no skew in terms of segment counts between the historicals.

## New input5:
```java
    String tier = "tier5";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
```
Explanation: In this input, we have two historical servers in the `tier5` tier, where one server has segments and the other server has no segments. This input is valid as it represents a scenario where there is skew in terms of segment counts between the historicals.