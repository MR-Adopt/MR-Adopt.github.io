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


# TEST CASE
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


# OTHER INPUT PAIRS 
## Input pair1:
```java
String tier = "tier1";
List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
String tier2 = "tier1";
List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```

## Input pair2:
```java
String tier = "tier1";
List<ServerHolder> historicals = Collections.emptyList();
String tier2 = "tier1";
List<ServerHolder> historicals2 = Collections.emptyList();
int maxSegmentsToMoveInTier = 1;
```

## Input pair3:
```java
String tier = "tier2";
List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
String tier2 = "tier2";
List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```

## Input pair4:
```java
String tier = "tier1";
List<ServerHolder> historicals = Arrays.asList(createServer("A", Collections.emptyList()), createServer("B", Collections.emptyList()));
String tier2 = "tier1";
List<ServerHolder> historicals2 = Arrays.asList(createServer("A", Collections.emptyList()), createServer("B", Collections.emptyList()));
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```

## Input pair5:
```java
String tier = "tier1";
List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", Collections.emptyList()));
String tier2 = "tier1";
List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", Collections.emptyList()));
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```

## Input pair6:
```java
String tier = "tier5";
List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
String tier2 = "tier5";
List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```

## Input pair7:
```java
String tier = "tier1";
List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
String tier2 = "tier1";
List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```

## Input pair8:
```java
String tier = "tier2";
List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", Collections.emptyList()));
String tier2 = "tier2";
List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", Collections.emptyList()));
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```

## Input pair9:
```java
String tier = "tier1";
List<ServerHolder> historicals = Collections.emptyList();
String tier2 = "tier1";
List<ServerHolder> historicals2 = Collections.emptyList();
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```



# OUTPUT FORMAT
```java
public class SegmentToMoveCalculatorTest_testHalfSegmentsArePickedForMoveWhenFullSkew {
    public static List<Object> inputTransformation_testHalfSegmentsArePickedForMoveWhenFullSkew(String tier, List<ServerHolder> historicals)  {
        // TODO
        String tier2 = 
		List<ServerHolder> historicals2 = 
		int maxSegmentsToMoveInTier = 
		List<Object> transformed_inputs = Arrays.asList(tier2, historicals2, maxSegmentsToMoveInTier);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.