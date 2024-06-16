## New input1:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", Collections.emptyList()));
```
Explanation: In this input, we have a tier named "tier2" with three historicals. The first two historicals have the same number of segments as the original test case, while the third historical has no segments. This scenario simulates a tier with a higher level of skew, where some historicals have more segments than others.

## New input2:
```java
    String tier = "tier3";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", Collections.emptyList()));
```
Explanation: In this input, we have a tier named "tier3" with four historicals. The first three historicals have the same number of segments as the original test case, while the fourth historical has no segments. This scenario simulates a tier with a higher level of skew, where some historicals have more segments than others, and there is an additional historical with no segments.

## New input3:
```java
    String tier = "tier4";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", Collections.emptyList()), createServer("B", Collections.emptyList()));
```
Explanation: In this input, we have a tier named "tier4" with two historicals. Both historicals have no segments. This scenario simulates a tier with no segments to move, as all historicals have no segments.

## New input4:
```java
    String tier = "tier5";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
```
Explanation: In this input, we have a tier named "tier5" with four historicals. All historicals have the same number of segments as the original test case. This scenario simulates a tier with no skew, where all historicals have the same number of segments.

## New input5:
```java
    String tier = "tier6";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS), createServer("E", Collections.emptyList()));
```
Explanation: In this input, we have a tier named "tier6" with five historicals. The first four historicals have the same number of segments as the original test case, while the fifth historical has no segments. This scenario simulates a tier with a higher level of skew, where some historicals have more segments than others, and there is an additional historical with no segments.
