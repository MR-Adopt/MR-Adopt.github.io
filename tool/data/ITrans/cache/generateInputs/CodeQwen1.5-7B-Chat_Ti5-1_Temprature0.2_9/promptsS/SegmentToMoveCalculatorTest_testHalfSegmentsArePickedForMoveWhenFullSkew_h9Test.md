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
TEST INPUT: `tier`,`historicals`


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


# REQUIRED DELIVERABLE
Construct five new values for the test input `tier`,`historicals`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 