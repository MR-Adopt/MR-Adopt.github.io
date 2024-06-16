## New input pair0:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    String tier2 = "tier2";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
The inferred relation is that the number of segments to move in tier is the same as the number of segments to move to fix skew. Since the number of segments to move to fix skew is the same as the number of segments to move in tier, the number of segments to move in tier is also the same as the number of segments to move to fix skew. Therefore, the new source input pair satisfies the inferred relation.

## New input pair1:
```java
    String tier = "tier3";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", Collections.emptyList()), createServer("B", WIKI_SEGMENTS));
    String tier2 = "tier3";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", Collections.emptyList()), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
The inferred relation is that the number of segments to move in tier is the same as the number of segments to move to fix skew. Since the number of segments to move to fix skew is the same as the number of segments to move in tier, the number of segments to move in tier is also the same as the number of segments to move to fix skew. Therefore, the new source input pair satisfies the inferred relation.

## New input pair2:
```java
    String tier = "tier4";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
    String tier2 = "tier4";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
The inferred relation is that the number of segments to move in tier is the same as the number of segments to move to fix skew. Since the number of segments to move to fix skew is the same as the number of segments to move in tier, the number of segments to move in tier is also the same as the number of segments to move to fix skew. Therefore, the new source input pair satisfies the inferred relation.

## New input pair3:
```java
    String tier = "tier5";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", Collections.emptyList()));
    String tier2 = "tier5";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", Collections.emptyList()));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
The inferred relation is that the number of segments to move in tier is the same as the number of segments to move to fix skew. Since the number of segments to move to fix skew is the same as the number of segments to move in tier, the number of segments to move in tier is also the same as the number of segments to move to fix skew. Therefore, the new source input pair satisfies the inferred relation.

## New input pair4:
```java
    String tier = "tier6";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
    String tier2 = "tier6";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
The inferred relation is that the number of segments to move in tier is the same as the number of segments to move to fix skew. Since the number of segments to move to fix skew is the same as the number of segments to move in tier, the number of segments to move in tier is also the same as the number of segments to move to fix skew. Therefore, the new source input pair satisfies the inferred relation.
