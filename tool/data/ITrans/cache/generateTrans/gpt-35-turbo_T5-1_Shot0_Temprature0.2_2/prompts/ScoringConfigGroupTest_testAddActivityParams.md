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


# TEST CASE
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


# OTHER INPUT PAIRS 
## Input pair1:
```java
ActivityParams ap = new ActivityParams("type1");
String type = "type1";
```

## Input pair2:
```java
ActivityParams ap = new ActivityParams("type2");
String type = ap.getActivityType();
```

## Input pair3:
```java
ActivityParams ap = new ActivityParams("type3");
String type = ap.getActivityType();
```

## Input pair4:
```java
ActivityParams ap = new ActivityParams("type4");
String type = ap.getActivityType();
```

## Input pair5:
```java
ActivityParams ap = new ActivityParams("type5");
String type = ap.getActivityType();
```

## Input pair6:
```java
ActivityParams ap = new ActivityParams("type6");
String type = ap.getActivityType();
```

## Input pair7:
```java
ActivityParams ap = new ActivityParams("type2");
String type = "type2";
```

## Input pair8:
```java
ActivityParams ap = new ActivityParams("type3");
String type = "type3";
```

## Input pair9:
```java
ActivityParams ap = new ActivityParams("type4");
String type = "type4";
```

## Input pair10:
```java
ActivityParams ap = new ActivityParams("type5");
String type = "type5";
```

## Input pair11:
```java
ActivityParams ap = new ActivityParams("type6");
String type = "type6";
```



# OUTPUT FORMAT
```java
public class ScoringConfigGroupTest_testAddActivityParams {
    public static String inputTransformation_testAddActivityParams(ActivityParams ap)  {
        // TODO
        String type = 
		return type;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.