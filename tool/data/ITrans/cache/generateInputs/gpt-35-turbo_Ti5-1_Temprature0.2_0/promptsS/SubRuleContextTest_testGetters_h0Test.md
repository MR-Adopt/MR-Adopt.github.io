# ORIGINAL TEST CASE
```java
@Test
public void testGetters() {
    SubRuleContext.Generator generator = new SubRuleContext.Generator();
    String NAME = "name";
    SubRuleContext context = generator.generate(NAME);
    Double id = -1.7976931348623157E308;
    SubRuleContext.Generator generator2 = new SubRuleContext.Generator();
    generator2.generate("name");
    assertEquals(NAME, generator2.getNameForGeneratedId(id));
    Set<Double> expectedIds = new HashSet<>();
    expectedIds.add(context.getId());
    assertEquals(expectedIds, generator.getIdsGeneratedForName(NAME));
}

```
TEST INPUT: `generator`,`NAME`


# METHOD UNDER TEST
```java
public SubRuleContext generate(Object ruleName) {
    assert nextId < Double.MAX_VALUE : "SubRuleContext.Generator's nextId reached Double.MAX_VALUE - " + "this required the equivalent of calling generate() at 6 billion TPS for 100 years";
    SubRuleContext subRuleContext = new SubRuleContext(nextId);
    if (!nameToIds.containsKey(ruleName)) {
        nameToIds.put(ruleName, new HashSet<>());
    }
    nameToIds.get(ruleName).add(nextId);
    idToName.put(nextId, ruleName);
    nextId = Math.nextUp(nextId);
    return subRuleContext;
}

public Object getNameForGeneratedId(Double id) {
    return idToName.get(id);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `generator`,`NAME`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    SubRuleContext.Generator generator = new SubRuleContext.Generator();
    String NAME = "name";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 