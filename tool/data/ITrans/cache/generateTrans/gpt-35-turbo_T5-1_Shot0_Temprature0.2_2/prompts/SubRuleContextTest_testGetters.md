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


# TEST CASE
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
SOURCE INPUT: `generator`,`NAME`
FOLLOW UP INPUT: `generator2`,`id`


# OTHER INPUT PAIRS 



# OUTPUT FORMAT
```java
public class SubRuleContextTest_testGetters {
    public static List<Object> inputTransformation_testGetters(SubRuleContext.Generator generator, String NAME)  {
        // TODO
        SubRuleContext.Generator generator2 = 
		Double id = 
		List<Object> transformed_inputs = Arrays.asList(generator2, id);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.