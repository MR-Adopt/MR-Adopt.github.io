## New input1:
```java
    String tier = "tier2";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS));
```
Explanation: In this input, the tier is "tier2" and the historicals list contains two servers, "A" and "B". Both servers have the same number of segments as the total number of segments in the WIKI_SEGMENTS list. This scenario simulates a tier with equal disk usage and segment counts per data source, which should result in no segments needing to be moved.

## New input2:
```java
    String tier = "tier3";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: In this input, the tier is "tier3" and the historicals list contains three servers, "A", "B", and "C". All servers have the same number of segments as the total number of segments in the WIKI_SEGMENTS list. This scenario simulates a tier with equal disk usage and segment counts per data source, which should result in no segments needing to be moved.

## New input3:
```java
    String tier = "tier4";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", Collections.emptyList()), createServer("C", WIKI_SEGMENTS));
```
Explanation: In this input, the tier is "tier4" and the historicals list contains three servers, "A", "B", and "C". Server "A" has the same number of segments as the total number of segments in the WIKI_SEGMENTS list, while servers "B" and "C" have no segments. This scenario simulates a tier with unequal disk usage and segment counts per data source, with server "A" having more segments than the others. This should result in segments needing to be moved from server "A" to server "B" or "C".

## New input4:
```java
    String tier = "tier5";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", Collections.emptyList()), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS));
```
Explanation: In this input, the tier is "tier5" and the historicals list contains three servers, "A", "B", and "C". Server "A" has no segments, while servers "B" and "C" have the same number of segments as the total number of segments in the WIKI_SEGMENTS list. This scenario simulates a tier with unequal disk usage and segment counts per data source, with server "B" and "C" having more segments than server "A". This should result in segments needing to be moved from server "B" or "C" to server "A".

## New input5:
```java
    String tier = "tier6";
    List<ServerHolder> historicals = Arrays.asList(createServer("A", WIKI_SEGMENTS), createServer("B", WIKI_SEGMENTS), createServer("C", WIKI_SEGMENTS), createServer("D", WIKI_SEGMENTS));
```
Explanation: In this input, the tier is "tier6" and the historicals list contains four servers, "A", "B", "C", and "D". All servers have the same number of segments as the total number of segments in the WIKI_SEGMENTS list. This scenario simulates a tier with equal disk usage and segment counts per data source, which should result in no segments needing to be moved.
