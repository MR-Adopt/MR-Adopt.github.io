## New input1:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```
Explanation: This input is valid because it tests the method with a tier that is not being balanced, and has two historicals with the same number of segments. This will ensure that the method will move segments between the two historicals to balance the tier.

## New input2:
```java
    String tier = "tier3";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: This input is valid because it tests the method with a tier that is not being balanced, and has three historicals with the same number of segments. This will ensure that the method will move segments between the three historicals to balance the tier.

## New input3:
```java
    String tier = "tier4";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
```
Explanation: This input is valid because it tests the method with a tier that is not being balanced, and has two historicals with the same number of segments and one historical with no segments. This will ensure that the method will move segments between the two historicals with the same number of segments and one historical with no segments to balance the tier.

## New input4:
```java
    String tier = "tier5";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
```
Explanation: This input is valid because it tests the method with a tier that is not being balanced, and has four historicals with the same number of segments. This will ensure that the method will move segments between the four historicals to balance the tier.

## New input5:
```java
    String tier = "tier6";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", Collections.emptyList()));
```
Explanation: This input is valid because it tests the method with a tier that is not being balanced, and has three historicals with the same number of segments and one historical with no segments. This will ensure that the method will move segments between the three historicals with the same number of segments and one historical with no segments to balance the tier.
