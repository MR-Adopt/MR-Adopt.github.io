## New input1:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```
This input is valid because it represents a scenario where there are two historical servers in the tier, both having the same number of segments. This will help test the case where there is no skew between the historicals.

## New input2:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
This input is valid because it represents a scenario where there are three historical servers in the tier, all having the same number of segments. This will help test the case where there is no skew between multiple historicals.

## New input3:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
```
This input is valid because it represents a scenario where there are three historical servers in the tier, but one of them has no segments. This will help test the case where there is skew between the historicals due to the absence of segments in one of them.

## New input4:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
```
This input is valid because it represents a scenario where there are four historical servers in the tier, all having the same number of segments. This will help test the case where there is no skew between multiple historicals.

## New input5:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Collections.emptyList();
```
This input is valid because it represents a scenario where there are no historical servers in the tier. This will help test the case where there are no historicals and the method should return 0.