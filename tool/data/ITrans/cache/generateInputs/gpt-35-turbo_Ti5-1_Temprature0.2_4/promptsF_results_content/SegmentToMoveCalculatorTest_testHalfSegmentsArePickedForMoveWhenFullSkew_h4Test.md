## Inferred Relation:
The method `computeNumSegmentsToMoveToBalanceTier` is called to compute the number of segments that need to be moved across the historicals in a tier to attain balance. This method is then called from the method `computeNumSegmentsToMoveInTier` to calculate the number of segments to be picked for moving in the given tier, based on the level of skew between the historicals in the tier.

The relation between the source inputs (`tier`, `historicals`) and the follow-up inputs (`tier2`, `historicals2`, `maxSegmentsToMoveInTier`) is as follows:
- The `tier` and `tier2` values are the same.
- The `historicals` and `historicals2` lists are the same.
- The `maxSegmentsToMoveInTier` value is set to `Integer.MAX_VALUE`.

## New input pair 0:
```java
String tier = "tier1";
List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
String tier2 = "tier1";
List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()));
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Explanation: 
In this new input pair, the `tier` and `tier2` values are set to "tier1". The `historicals` and `historicals2` lists are the same, with historicals "A" and "B" having the same segments. The `maxSegmentsToMoveInTier` value is set to `Integer.MAX_VALUE`, which means there is no limit on the maximum number of segments allowed to be moved in the tier. This input pair satisfies the inferred relation because it follows the same pattern as the original test case.

## New input pair 1:
```java
String tier = "tier1";
List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
String tier2 = "tier1";
List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Explanation: 
In this new input pair, the `tier` and `tier2` values are set to "tier1". The `historicals` and `historicals2` lists are the same, with historicals "A", "B", and "C" having the same segments. The `maxSegmentsToMoveInTier` value is set to `Integer.MAX_VALUE`, which means there is no limit on the maximum number of segments allowed to be moved in the tier. This input pair satisfies the inferred relation because it follows the same pattern as the original test case.

## New input pair 2:
```java
String tier = "tier1";
List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
String tier2 = "tier1";
List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Explanation: 
In this new input pair, the `tier` and `tier2` values are set to "tier1". The `historicals` and `historicals2` lists are the same, with historicals "A", "B", and "C" having the same segments. The `maxSegmentsToMoveInTier` value is set to `Integer.MAX_VALUE`, which means there is no limit on the maximum number of segments allowed to be moved in the tier. This input pair satisfies the inferred relation because it follows the same pattern as the original test case.

## New input pair 3:
```java
String tier = "tier1";
List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", Collections.emptyList()));
String tier2 = "tier1";
List<ServerHolder> historicals2 = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", Collections.emptyList()));
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Explanation: 
In this new input pair, the `tier` and `tier2` values are set to "tier1". The `historicals` and `historicals2` lists are the same, with historicals "A", "B", and "C" having the same segments. The `maxSegmentsToMoveInTier` value is set to `Integer.MAX_VALUE`, which means there is no limit on the maximum number of segments allowed to be moved in the tier. This input pair satisfies the inferred relation because it follows the same pattern as the original test case.

## New input pair 4:
```java
String tier = "tier1";
List<ServerHolder> historicals = Collections.emptyList();
String tier2 = "tier1";
List<ServerHolder> historicals2 = Collections.emptyList();
int maxSegmentsToMoveInTier = Integer.MAX_VALUE;
```
Explanation: 
In this new input pair, the `tier` and `tier2` values are set to "tier1". The `historicals` and `historicals2` lists are empty. The `maxSegmentsToMoveInTier` value is set to `Integer.MAX_VALUE`, which means there is no limit on the maximum number of segments allowed to be moved in the tier. This input pair satisfies the inferred relation because it follows the same pattern as the original test case.