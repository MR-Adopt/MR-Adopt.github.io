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
TEST INPUT: `ap`


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


# REQUIRED DELIVERABLE
Construct five new values for the test input `ap`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    ActivityParams ap = new ActivityParams("type1");
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 