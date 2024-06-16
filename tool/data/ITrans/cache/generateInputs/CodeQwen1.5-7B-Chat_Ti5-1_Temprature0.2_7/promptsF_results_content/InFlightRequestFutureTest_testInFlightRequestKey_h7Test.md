# REQUIRED DELIVERABLE
## New input pair0:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 1);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 0, 1);
```
### Explanation:
The inferred relation between the source input and follow-up input is that the hash codes of the two `InFlightRequestKey` objects should be equal. Since the only difference between the source and follow-up inputs is the value of the second parameter (0 -> 1), the hash codes should also be equal.

## New input pair1:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 1, 0);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 0);
```
### Explanation:
The inferred relation between the source input and follow-up input is that the hash codes of the two `InFlightRequestKey` objects should be equal. Since the only difference between the source and follow-up inputs is the value of the third parameter (0 -> 1), the hash codes should also be equal.

## New input pair2:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 0, 0);
```
### Explanation:
The inferred relation between the source input and follow-up input is that the hash codes of the two `InFlightRequestKey` objects should be equal. Since the only difference between the source and follow-up inputs is the value of the second parameter (0 -> 0), the hash codes should also be equal.

## New input pair3:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group1", 0, 0);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group1", 0, 0);
```
### Explanation:
The inferred relation between the source input and follow-up input is that the hash codes of the two `InFlightRequestKey` objects should be equal. Since the only difference between the source and follow-up inputs is the value of the first parameter ("group" -> "group1"), the hash codes should also be equal.

## New input pair4:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", Integer.MAX_VALUE, Integer.MAX_VALUE);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", Integer.MAX_VALUE, Integer.MAX_VALUE);
```
### Explanation:
The inferred relation between the source input and follow-up input is that the hash codes of the two `InFlightRequestKey` objects should be equal. Since the only difference between the source and follow-up inputs is the value of the second and third parameters (0 -> Integer.MAX_VALUE), the hash codes should also be equal.
