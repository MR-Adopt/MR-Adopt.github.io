## New input pair0:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    String tier2 = "tier2";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Generation of follow-up input:
```java
    int segmentsToMoveToFixSkew = SegmentToMoveCalculator.computeNumSegmentsToMoveToBalanceTier(tier, historicals);
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier2, historicals2, maxSegmentsToMoveInTier);
    Assert.assertEquals(segmentsToMoveToFixSkew, segmentsToMove);
```
Explanation:
The inferred relation is that the number of segments to move in the tier is equal to the number of segments to move to fix skew. Since the number of segments to move to fix skew is the same for both input pairs, the new input pair satisfies the inferred relation.

## New input pair1:
```java
    String tier = "tier3";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
    String tier2 = "tier3";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Generation of follow-up input:
```java
    int segmentsToMoveToFixSkew = SegmentToMoveCalculator.computeNumSegmentsToMoveToBalanceTier(tier, historicals);
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier2, historicals2, maxSegmentsToMoveInTier);
    Assert.assertEquals(segmentsToMoveToFixSkew, segmentsToMove);
```
Explanation:
The inferred relation is that the number of segments to move in the tier is equal to the number of segments to move to fix skew. Since the number of segments to move to fix skew is the same for both input pairs, the new input pair satisfies the inferred relation.

## New input pair2:
```java
    String tier = "tier4";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
    String tier2 = "tier4";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Generation of follow-up input:
```java
    int segmentsToMoveToFixSkew = SegmentToMoveCalculator.computeNumSegmentsToMoveToBalanceTier(tier, historicals);
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier2, historicals2, maxSegmentsToMoveInTier);
    Assert.assertEquals(segmentsToMoveToFixSkew, segmentsToMove);
```
Explanation:
The inferred relation is that the number of segments to move in the tier is equal to the number of segments to move to fix skew. Since the number of segments to move to fix skew is the same for both input pairs, the new input pair satisfies the inferred relation.

## New input pair3:
```java
    String tier = "tier5";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
    String tier2 = "tier5";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Generation of follow-up input:
```java
    int segmentsToMoveToFixSkew = SegmentToMoveCalculator.computeNumSegmentsToMoveToBalanceTier(tier, historicals);
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier2, historicals2, maxSegmentsToMoveInTier);
    Assert.assertEquals(segmentsToMoveToFixSkew, segmentsToMove);
```
Explanation:
The inferred relation is that the number of segments to move in the tier is equal to the number of segments to move to fix skew. Since the number of segments to move to fix skew is the same for both input pairs, the new input pair satisfies the inferred relation.

## New input pair4:
```java
    String tier = "tier6";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", Collections.emptyList()));
    String tier2 = "tier6";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", Collections.emptyList()));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Generation of follow-up input:
```java
    int segmentsToMoveToFixSkew = SegmentToMoveCalculator.computeNumSegmentsToMoveToBalanceTier(tier, historicals);
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier2, historicals2, maxSegmentsToMoveInTier);
    Assert.assertEquals(segmentsToMoveToFixSkew, segmentsToMove);
```
Explanation:
The inferred relation is that the number of segments to move in the tier is equal to the number of segments to move to fix skew. Since the number of segments to move to fix skew is the same for both input pairs, the new input pair satisfies the inferred relation.
