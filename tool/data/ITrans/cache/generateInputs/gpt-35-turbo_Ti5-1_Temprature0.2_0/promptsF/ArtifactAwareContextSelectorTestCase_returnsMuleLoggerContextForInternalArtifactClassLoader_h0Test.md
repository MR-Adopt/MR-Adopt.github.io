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
SOURCE INPUT: `fqcn`,`currentContext`,`systemLoader`
FOLLOW UP INPUT: `fqcn2`,`serviceLoader`,`currentContext2`


# METHOD UNDER TEST
```java
@Override
public LoggerContext getContext(String fqcn, ClassLoader classLoader, boolean currentContext, URI configLocation) {
    return cache.getLoggerContext(resolveLoggerContextClassLoader(classLoader));
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    String fqcn = "com.example.MyClass";
    boolean currentContext = true;
    ClassLoader systemLoader = this.getClass().getClassLoader();
```

## New source input1:
```java
    String fqcn = "org.apache.commons.logging.Log";
    boolean currentContext = false;
    ClassLoader systemLoader = this.getClass().getClassLoader();
```

## New source input2:
```java
    String fqcn = "com.example.MyClass";
    boolean currentContext = true;
    ClassLoader systemLoader = Thread.currentThread().getContextClassLoader();
```

## New source input3:
```java
    String fqcn = "com.example.MyClass";
    boolean currentContext = false;
    ClassLoader systemLoader = ClassLoader.getSystemClassLoader();
```

## New source input4:
```java
    String fqcn = "com.example.MyClass";
    boolean currentContext = true;
    ClassLoader systemLoader = null;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    String fqcn = "";
    boolean currentContext = true;
    ClassLoader systemLoader = this.getClass().getClassLoader();
    String fqcn2 = "";
    boolean currentContext2 = true;
    ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], this.getClass().getClassLoader(), mock(ClassLoaderLookupPolicy.class));
    ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.