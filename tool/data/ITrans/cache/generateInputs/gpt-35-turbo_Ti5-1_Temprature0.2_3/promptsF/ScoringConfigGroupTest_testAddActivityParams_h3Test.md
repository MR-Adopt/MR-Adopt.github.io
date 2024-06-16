# ORIGINAL TEST CASE
```java
@Test
void testAddActivityParams() {
    ScoringConfigGroup c = new ScoringConfigGroup();
    int originalSize = c.getActivityParams().size();
    ActivityParams ap = new ActivityParams("type1");
    String type = "type1";
    c.addActivityParams(ap);
    Assertions.assertEquals(ap, c.getActivityParams(type));
}

```
SOURCE INPUT: `ap`
FOLLOW UP INPUT: `type`


# METHOD UNDER TEST
```java
public void addActivityParams(final ActivityParams params) {
    final ActivityParams previous = this.getActivityParams(params.getActivityType());
    if (previous != null) {
        if (previous.getActivityType().equals(PtConstants.TRANSIT_ACTIVITY_TYPE)) {
            log.error("ERROR: Activity parameters for activity type " + previous.getActivityType() + " were just overwritten. This happens most " + "likely because you defined them in the config file and the Controler overwrites them.  Or the other way " + "round.  pt interaction has problems, but doing what you are doing here will just cause " + "other (less visible) problem. Please take the effort to discuss with the core team " + "what needs to be done.  kai, nov'12");
        } else {
            log.info("activity parameters for activity type " + previous.getActivityType() + " were just overwritten.");
        }
        final boolean removed = removeParameterSet(previous);
        if (!removed)
            throw new RuntimeException("problem replacing activity params ");
    }
    super.addParameterSet(params);
}

public ActivityParams getActivityParams(final String actType) {
    return this.getActivityParamsPerType().get(actType);
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    ActivityParams ap = new ActivityParams("type2");
```

## New source input1:
```java
    ActivityParams ap = new ActivityParams("type3");
```

## New source input2:
```java
    ActivityParams ap = new ActivityParams("type4");
```

## New source input3:
```java
    ActivityParams ap = new ActivityParams("type5");
```

## New source input4:
```java
    ActivityParams ap = new ActivityParams("type6");
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    ActivityParams ap = new ActivityParams("type1");
    String type = "type1";
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.