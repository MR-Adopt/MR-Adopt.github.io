# ORIGINAL TEST CASE
```java
@Test
public void testExpressedSymtpom() {
    String name = "pain";
    ExpressedSymptom symptom = new ExpressedSymptom(name);
    String module = "testModule";
    symptom.addressSource(module);
    ExpressedSymptom symptom2 = symptom;
    String module2 = "testModule";
    symptom2.addressSource(module2);
    String cause = "testCause";
    for (long l = 0L; l < 3L; l++) {
        symptom.onSet(module, cause, l, (int) (100 * l), false);
        assertEquals(Long.valueOf(l), symptom2.getSymptomLastUpdatedTime(module2));
    }
}

```
TEST INPUT: `symptom`,`module`


# METHOD UNDER TEST
```java
/**
 * this method updates the data structure wit a symptom being onset from a module.
 */
public void onSet(String module, String cause, long time, int value, Boolean addressed) {
    if (!sources.containsKey(module)) {
        sources.put(module, new SymptomSource(module));
    }
    sources.get(module).addInfo(cause, time, value, addressed);
}

/**
 * Method for retrieving the last time the symptom has been updated from a given module.
 */
public Long getSymptomLastUpdatedTime(String module) {
    Long result = null;
    if (module != null && sources.containsKey(module)) {
        result = sources.get(module).getLastUpdateTime();
    }
    return result;
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `symptom`,`module`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    String name = "pain";
    ExpressedSymptom symptom = new ExpressedSymptom(name);
    String module = "testModule";
    symptom.addressSource(module);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 