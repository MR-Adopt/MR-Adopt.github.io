# ORIGINAL TEST CASE
```java
@Test
public void testMinSegmentsArePickedForMoveWhenNoSkew() {
    int totalSegmentsInTier = 20_000;
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", SegmentToMoveCalculatorTest.WIKI_SEGMENTS), createServer("B", SegmentToMoveCalculatorTest.WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
    int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
    // Find segmentsToMove with no limit on maxSegmentsToMove
    int segmentsToMove = SegmentToMoveCalculator.computeNumSegmentsToMoveInTier(tier, historicals, maxSegmentsToMoveInTier);
    // System.out.println("minSegmentsToMove: " + minSegmentsToMove);
    // System.out.println("segmentsToMove: " + segmentsToMove);
    Assert.assertEquals(minSegmentsToMove, segmentsToMove);
}

```
TEST INPUT: `totalSegmentsInTier`


# METHOD UNDER TEST
```java
/**
 * Calculates the minimum number of segments that should be considered for
 * moving in a tier, so that the cluster is always balancing itself.
 * <p>
 * This value must be calculated separately for every tier.
 *
 * @param totalSegmentsInTier Total number of all replicas of all segments
 *                            loaded or queued across all historicals in the tier.
 * @return {@code minSegmentsToMoveInTier} in the range
 * [{@link #MIN_SEGMENTS_TO_MOVE}, {@code ~0.15% of totalSegmentsInTier}].
 */
public static int computeMinSegmentsToMoveInTier(int totalSegmentsInTier) {
    // Divide by 2^14 and multiply by 100 so that the value increases
    // in steps of 100 for every 2^16 = ~65k segments
    int upperBound = (totalSegmentsInTier >> 16) * 100;
    int lowerBound = Math.min(MIN_SEGMENTS_TO_MOVE, totalSegmentsInTier);
    return Math.max(lowerBound, upperBound);
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
Construct five new values for the test input `totalSegmentsInTier`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    int totalSegmentsInTier = 20_000;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 