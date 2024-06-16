# ORIGINAL TEST CASE
```java
@Test
public void returnsMuleLoggerContextForArtifactClassLoaderChild() {
    RegionClassLoader regionClassLoader = this.regionClassLoader;
    String fqcn = "";
    boolean currentContext = true;
    String fqcn2 = "";
    boolean currentContext2 = true;
    ClassLoader childClassLoader = new URLClassLoader(new URL[0], regionClassLoader);
    LoggerContext parentCtx = selector.getContext(fqcn, regionClassLoader, currentContext);
    LoggerContext childCtx = selector.getContext(fqcn2, childClassLoader, currentContext2);
    assertThat(childCtx, sameInstance(parentCtx));
}

```
TEST INPUT: `fqcn`,`currentContext`,`regionClassLoader`


# METHOD UNDER TEST
```java
@Override
public LoggerContext getContext(String fqcn, ClassLoader classLoader, boolean currentContext, URI configLocation) {
    return cache.getLoggerContext(resolveLoggerContextClassLoader(classLoader));
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `fqcn`,`currentContext`,`regionClassLoader`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    RegionClassLoader regionClassLoader = this.regionClassLoader;
    String fqcn = "";
    boolean currentContext = true;
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 