## New input1:
```java
    int totalSegmentsInTier = 10_000;
```
Explanation: This input is valid because it is less than the minimum value of 20_000. This ensures that the method under test will calculate the minimum number of segments to move, which is 10_000.

## New input2:
```java
    int totalSegmentsInTier = 30_000;
```
Explanation: This input is valid because it is greater than the maximum value of 20_000. This ensures that the method under test will calculate the maximum number of segments to move, which is 30_000.

## New input3:
```java
    int totalSegmentsInTier = 15_000;
```
Explanation: This input is valid because it is in the range of 20_000 to 30_000. This ensures that the method under test will calculate a number of segments to move that falls within the valid range, which is 15_000.

## New input4:
```java
    int totalSegmentsInTier = 25_000;
```
Explanation: This input is valid because it is in the range of 20_000 to 30_000. This ensures that the method under test will calculate a number of segments to move that falls within the valid range, which is 25_000.

## New input5:
```java
    int totalSegmentsInTier = 35_000;
```
Explanation: This input is valid because it is greater than the maximum value of 30_000. This ensures that the method under test will calculate the maximum number of segments to move, which is 35_000.
