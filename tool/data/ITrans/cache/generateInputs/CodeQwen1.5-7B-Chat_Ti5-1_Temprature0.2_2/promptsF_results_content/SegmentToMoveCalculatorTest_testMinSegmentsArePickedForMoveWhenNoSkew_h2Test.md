## New input pair0:
```java
    int totalSegmentsInTier = 10_000;
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Follow-up input:
```java
    int totalSegmentsInTier = 10_000;
    int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier, historicals, maxSegmentsToMoveInTier);
    Assert.assertEquals(minSegmentsToMove, segmentsToMove);
```
Explanation:
The inferred relation is that the minimum number of segments to move in a tier is equal to the number of segments to move in the tier when there is no skew. Since the total number of segments in the tier is 10,000, the minimum number of segments to move is also 10,000. Therefore, the follow-up input satisfies the inferred relation.

## New input pair1:
```java
    int totalSegmentsInTier = 30_000;
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Follow-up input:
```java
    int totalSegmentsInTier = 30_000;
    int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier, historicals, maxSegmentsToMoveInTier);
    Assert.assertEquals(minSegmentsToMove, segmentsToMove);
```
Explanation:
The inferred relation is that the minimum number of segments to move in a tier is equal to the number of segments to move in the tier when there is no skew. Since the total number of segments in the tier is 30,000, the minimum number of segments to move is also 30,000. Therefore, the follow-up input satisfies the inferred relation.

## New input pair2:
```java
    int totalSegmentsInTier = 15_000;
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Follow-up input:
```java
    int totalSegmentsInTier = 15_000;
    int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier, historicals, maxSegmentsToMoveInTier);
    Assert.assertEquals(minSegmentsToMove, segmentsToMove);
```
Explanation:
The inferred relation is that the minimum number of segments to move in a tier is equal to the number of segments to move in the tier when there is no skew. Since the total number of segments in the tier is 15,000, the minimum number of segments to move is also 15,000. Therefore, the follow-up input satisfies the inferred relation.

## New input pair3:
```java
    int totalSegmentsInTier = 25_000;
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Follow-up input:
```java
    int totalSegmentsInTier = 25_000;
    int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier, historicals, maxSegmentsToMoveInTier);
    Assert.assertEquals(minSegmentsToMove, segmentsToMove);
```
Explanation:
The inferred relation is that the minimum number of segments to move in a tier is equal to the number of segments to move in the tier when there is no skew. Since the total number of segments in the tier is 25,000, the minimum number of segments to move is also 25,000. Therefore, the follow-up input satisfies the inferred relation.

## New input pair4:
```java
    int totalSegmentsInTier = 35_000;
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Follow-up input:
```java
    int totalSegmentsInTier = 35_000;
    int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier, historicals, maxSegmentsToMoveInTier);
    Assert.assertEquals(minSegmentsToMove, segmentsToMove);
```
Explanation:
The inferred relation is that the minimum number of segments to move in a tier is equal to the number of segments to move in the tier when there is no skew. Since the total number of segments in the tier is 35,000, the minimum number of segments to move is also 35,000. Therefore, the follow-up input satisfies the inferred relation.
