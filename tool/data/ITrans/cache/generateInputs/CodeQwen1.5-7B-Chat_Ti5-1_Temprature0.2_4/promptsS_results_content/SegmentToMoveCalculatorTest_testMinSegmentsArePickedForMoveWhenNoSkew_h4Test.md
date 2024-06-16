## New input1:
```java
    int totalSegmentsInTier = 10_000;
```
Explanation: This input is valid because it is less than the minimum value of 20,000. This ensures that the method under test will calculate the minimum number of segments to move, which is 10,000.

## New input2:
```java
    int totalSegmentsInTier = 30_000;
```
Explanation: This input is valid because it is greater than the maximum value of 20,000. This ensures that the method under test will calculate the number of segments to move, which is the difference between the total segments and the minimum number of segments to move, which is 10,000.

## New input3:
```java
    int totalSegmentsInTier = 15_000;
```
Explanation: This input is valid because it is equal to the minimum value of 20,000. This ensures that the method under test will calculate the minimum number of segments to move, which is 10,000.

## New input4:
```java
    int totalSegmentsInTier = 25_000;
```
Explanation: This input is valid because it is equal to the maximum value of 20,000. This ensures that the method under test will calculate the number of segments to move, which is the difference between the total segments and the minimum number of segments to move, which is 10,000.

## New input5:
```java
    int totalSegmentsInTier = 12_500;
```
Explanation: This input is valid because it is within the range of 10,000 to 20,000. This ensures that the method under test will calculate the number of segments to move, which is the difference between the total segments and the minimum number of segments to move, which is 10,000.
