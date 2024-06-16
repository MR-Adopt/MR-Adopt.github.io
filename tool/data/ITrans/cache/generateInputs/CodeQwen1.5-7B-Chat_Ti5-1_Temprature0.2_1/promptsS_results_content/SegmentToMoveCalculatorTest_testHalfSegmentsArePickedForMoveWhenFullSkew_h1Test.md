## New input1:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with two historicals, both of which have the same number of segments. This will cause the method under test to move segments between the two historicals to balance the tier.

## New input2:
```java
    String tier = "tier3";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with three historicals, all of which have the same number of segments. This will cause the method under test to move segments between the historicals to balance the tier.

## New input3:
```java
    String tier = "tier4";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with four historicals, all of which have the same number of segments. This will cause the method under test to move segments between the historicals to balance the tier.

## New input4:
```java
    String tier = "tier5";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS), createServer("E", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with five historicals, all of which have the same number of segments. This will cause the method under test to move segments between the historicals to balance the tier.

## New input5:
```java
    String tier = "tier6";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS), createServer("E", WIKI_SEGMENTS), createServer("F", WIKI_SEGMENTS));
```
Explanation: This input is valid because it creates a tier with six historicals, all of which have the same number of segments. This will cause the method under test to move segments between the historicals to balance the tier.
