# ORIGINAL TEST CASE
```java
@Test
public void returnsMuleLoggerContextForInternalArtifactClassLoader() {
    String fqcn = "";
    boolean currentContext = true;
    ClassLoader systemLoader = this.getClass().getClassLoader();
    String fqcn2 = "";
    boolean currentContext2 = true;
    ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], this.getClass().getClassLoader(), mock(ClassLoaderLookupPolicy.class));
    ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
    LoggerContext systemContext = selector.getContext(fqcn, systemLoader, currentContext);
    LoggerContext serviceCtx = selector.getContext(fqcn2, serviceLoader, currentContext2);
    assertThat(serviceCtx, sameInstance(systemContext));
}

```
TEST INPUT: `fqcn`,`currentContext`,`systemLoader`


# METHOD UNDER TEST
```java
@Override
public LoggerContext getContext(String fqcn, ClassLoader classLoader, boolean currentContext, URI configLocation) {
    return cache.getLoggerContext(resolveLoggerContextClassLoader(classLoader));
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `fqcn`,`currentContext`,`systemLoader`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    String fqcn = "";
    boolean currentContext = true;
    ClassLoader systemLoader = this.getClass().getClassLoader();
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 