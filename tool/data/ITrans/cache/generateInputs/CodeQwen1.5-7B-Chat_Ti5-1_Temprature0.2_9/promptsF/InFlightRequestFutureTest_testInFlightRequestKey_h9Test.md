# ORIGINAL TEST CASE
```java
@Test
public void testInFlightRequestKey() {
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 1);
    Assert.assertEquals(requestKey1.hashCode(), requestKey2.hashCode());
}

```
SOURCE INPUT: `requestKey1`
FOLLOW UP INPUT: `requestKey2`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return Objects.hashCode(group);
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 1);
```

## New source input1:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 1, 0);
```

## New source input2:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
```

## New source input3:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 1, 1);
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    InFlightRequestKey requestKey1 = new InFlightRequestKey("group", 0, 0);
    InFlightRequestKey requestKey2 = new InFlightRequestKey("group", 1, 1);
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.