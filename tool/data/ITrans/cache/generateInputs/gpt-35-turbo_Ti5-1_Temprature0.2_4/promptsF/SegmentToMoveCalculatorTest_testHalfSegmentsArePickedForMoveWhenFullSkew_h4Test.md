# ORIGINAL TEST CASE
```java
@Test
public void testHalfSegmentsArePickedForMoveWhenFullSkew() {
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
    String tier2 = "tier1";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
    int segmentsToMoveToFixSkew = SegmentToMoveCalculator.computeNumSegmentsToMoveToBalanceTier(tier, historicals);
    // Find segmentsToMove with no limit on maxSegmentsToMove
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier2, historicals2, maxSegmentsToMoveInTier);
    Assert.assertEquals(segmentsToMoveToFixSkew, segmentsToMove);
}

```
SOURCE INPUT: `tier`,`historicals`
FOLLOW UP INPUT: `tier2`,`historicals2`,`maxSegmentsToMoveInTier`


# METHOD UNDER TEST
```java
/**
 * Computes the number of segments that need to be moved across the historicals
 * in a tier to attain balance in terms of disk usage and segment counts per
 * data source.
 *
 * @param tier        Name of the tier used only for logging purposes
 * @param historicals List of historicals in the tier
 */
public static int computeNumSegmentsToMoveToBalanceTier(String tier, List<ServerHolder> historicals) {
    if (historicals.isEmpty()) {
        return 0;
    }
    return Math.max(computeSegmentsToMoveToBalanceCountsPerDatasource(tier, historicals), computeSegmentsToMoveToBalanceDiskUsage(tier, historicals));
}

/**
 * Calculates the number of segments to be picked for moving in the given tier,
 * based on the level of skew between the historicals in the tier.
 *
 * @param tier                    Name of tier used for logging purposes
 * @param historicals             Active historicals in tier
 * @param maxSegmentsToMoveInTier Maximum number of segments allowed to be moved
 *                                in the tier.
 * @return Number of segments to move in the tier in the range
 * [{@link #MIN_SEGMENTS_TO_MOVE}, {@code maxSegmentsToMoveInTier}].
 */
public static int computeNumSegmentsToMoveInTier(String tier, List<ServerHolder> historicals, int maxSegmentsToMoveInTier) {
    final int totalSegments = historicals.stream().mapToInt(server -> server.getProjectedSegments().getTotalSegmentCount()).sum();
    // Move at least some segments to ensure that the cluster is always balancing itself
    final int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegments);
    final int segmentsToMoveToFixDeviation = SegmentToMoveCalculator.computeNumSegmentsToMoveToBalanceTier(tier, historicals);
    log.info("Need to move [%,d] segments in tier[%s] to attain balance. Allowed values are [min=%d, max=%d].", segmentsToMoveToFixDeviation, tier, minSegmentsToMove, maxSegmentsToMoveInTier);
    final int activeSegmentsToMove = Math.max(minSegmentsToMove, segmentsToMoveToFixDeviation);
    return Math.min(activeSegmentsToMove, maxSegmentsToMoveInTier);
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```

## New source input1:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```

## New source input2:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
```

## New source input3:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", Collections.emptyList()));
```

## New source input4:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Collections.emptyList();
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
    String tier2 = "tier1";
    List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.