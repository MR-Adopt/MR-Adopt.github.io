# ORIGINAL TEST CASE
```java
@Test
void testHashCodeAndEquals() {
    Cost subject = Cost.costOfSeconds(10);
    Cost same = Cost.costOfSeconds(10);
    Cost other = Cost.costOfSeconds(11);
    assertNotEquals(subject.hashCode(), other.hashCode());
}

```
SOURCE INPUT: `subject`
FOLLOW UP INPUT: `other`


# METHOD UNDER TEST
```java
@Override
public int hashCode() {
    return value;
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    Cost subject = Cost.costOfSeconds(0);
```

## New source input1:
```java
    Cost subject = Cost.costOfSeconds(100);
```

## New source input2:
```java
    Cost subject = Cost.costOfSeconds(-10);
```

## New source input3:
```java
    Cost subject = Cost.costOfSeconds(Integer.MAX_VALUE);
```

## New source input4:
```java
    Cost subject = Cost.costOfSeconds(Integer.MIN_VALUE);
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    Cost subject = Cost.costOfSeconds(10);
    Cost other = Cost.costOfSeconds(11);
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.