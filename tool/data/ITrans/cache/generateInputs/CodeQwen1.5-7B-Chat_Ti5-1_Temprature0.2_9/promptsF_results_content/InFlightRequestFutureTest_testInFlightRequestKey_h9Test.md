# REQUIRED DELIVERABLE
## New input pair0:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 0, 0);
```
### Code used to generate follow-up input:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 0, 0);
```
### Explanation:
The inferred relation between the source input and follow-up input is that the hash codes of the two InFlightRequestKeys should be equal. Since the group is the only field that is being considered in the hashCode method, if the group is the same for both requestKey1 and requestKey2, their hash codes should also be the same. Therefore, the new source input pair satisfies the inferred relation.

## New input pair1:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 1, 1);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 1);
```
### Code used to generate follow-up input:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 1, 1);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 1);
```
### Explanation:
The inferred relation between the source input and follow-up input is that the hash codes of the two InFlightRequestKeys should be equal. Since the group is the only field that is being considered in the hashCode method, if the group is the same for both requestKey1 and requestKey2, their hash codes should also be the same. Therefore, the new source input pair satisfies the inferred relation.

## New input pair2:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 1);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 0, 1);
```
### Code used to generate follow-up input:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 1);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 0, 1);
```
### Explanation:
The inferred relation between the source input and follow-up input is that the hash codes of the two InFlightRequestKeys should be equal. Since the group is the only field that is being considered in the hashCode method, if the group is the same for both requestKey1 and requestKey2, their hash codes should also be the same. Therefore, the new source input pair satisfies the inferred relation.

## New input pair3:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 1, 0);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 0);
```
### Code used to generate follow-up input:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 1, 0);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 0);
```
### Explanation:
The inferred relation between the source input and follow-up input is that the hash codes of the two InFlightRequestKeys should be equal. Since the group is the only field that is being considered in the hashCode method, if the group is the same for both requestKey1 and requestKey2, their hash codes should also be the same. Therefore, the new source input pair satisfies the inferred relation.
