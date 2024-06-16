## New input pair0:
```java
    int totalSegmentsInTier = 10_000;
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
### Explanation:
The inferred relation between the source input and the follow-up input is that the `totalSegmentsInTier` is directly related to the `minSegmentsToMoveInTier` computed by the `computeMinSegmentsToMoveInTier` method. Since the `totalSegmentsInTier` is smaller than the original value, the `minSegmentsToMoveInTier` should also be smaller.

### Code used to generate the follow-up input:
```java
int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
```

## New input pair1:
```java
    int totalSegmentsInTier = 50_000;
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
### Explanation:
The inferred relation between the source input and the follow-up input is that the `totalSegmentsInTier` is directly related to the `minSegmentsToMoveInTier` computed by the `computeMinSegmentsToMoveInTier` method. Since the `totalSegmentsInTier` is larger than the original value, the `minSegmentsToMoveInTier` should also be larger.

### Code used to generate the follow-up input:
```java
int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
```

## New input pair2:
```java
    int totalSegmentsInTier = 30_000;
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
### Explanation:
The inferred relation between the source input and the follow-up input is that the `totalSegmentsInTier` is directly related to the `minSegmentsToMoveInTier` computed by the `computeMinSegmentsToMoveInTier` method. Since the `totalSegmentsInTier` is smaller than the original value, the `minSegmentsToMoveInTier` should also be smaller.

### Code used to generate the follow-up input:
```java
int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
```

## New input pair3:
```java
    int totalSegmentsInTier = 15_000;
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
### Explanation:
The inferred relation between the source input and the follow-up input is that the `totalSegmentsInTier` is directly related to the `minSegmentsToMoveInTier` computed by the `computeMinSegmentsToMoveInTier` method. Since the `totalSegmentsInTier` is smaller than the original value, the `minSegmentsToMoveInTier` should also be smaller.

### Code used to generate the follow-up input:
```java
int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
```

## New input pair4:
```java
    int totalSegmentsInTier = 40_000;
    String tier = "tier1";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
    int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
### Explanation:
The inferred relation between the source input and the follow-up input is that the `totalSegmentsInTier` is directly related to the `minSegmentsToMoveInTier` computed by the `computeMinSegmentsToMoveInTier` method. Since the `totalSegmentsInTier` is larger than the original value, the `minSegmentsToMoveInTier` should also be larger.

### Code used to generate the follow-up input:
```java
int minSegmentsToMove = SegmentToMoveCalculator.computeMinSegmentsToMoveInTier(totalSegmentsInTier);
```
