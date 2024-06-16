## New input1:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```
Explanation: In this input, we have two historical servers in the tier, both containing the same number of segments. This input is valid as it represents a scenario where there is no skew in terms of segment counts between the historicals.

## New input2:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: In this input, we have three historical servers in the tier, all containing the same number of segments. This input is valid as it represents a scenario where there is no skew in terms of segment counts between the historicals.

## New input3:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
```
Explanation: In this input, we have three historical servers in the tier, with one historical server having no segments. This input is valid as it represents a scenario where there is skew in terms of segment counts between the historicals.

## New input4:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", Collections.emptyList()));
```
Explanation: In this input, we have three historical servers in the tier, with one historical server having no segments. This input is valid as it represents a scenario where there is skew in terms of segment counts between the historicals.

## New input5:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Collections.emptyList();
```
Explanation: In this input, there are no historical servers in the tier. This input is valid as it represents a scenario where there are no historicals to balance, resulting in no segments to move.