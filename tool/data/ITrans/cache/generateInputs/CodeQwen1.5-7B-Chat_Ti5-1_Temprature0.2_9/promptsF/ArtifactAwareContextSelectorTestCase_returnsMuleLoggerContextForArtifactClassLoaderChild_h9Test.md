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
SOURCE INPUT: `fqcn`,`currentContext`,`regionClassLoader`
FOLLOW UP INPUT: `fqcn2`,`childClassLoader`,`currentContext2`


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
    RegionClassLoader regionClassLoader = this.regionClassLoader;
    String fqcn = "com.example.MyClass";
    boolean currentContext = true;
```

## New source input1:
```java
    RegionClassLoader regionClassLoader = null;
    String fqcn = "";
    boolean currentContext = true;
```

## New source input2:
```java
    RegionClassLoader regionClassLoader = this.regionClassLoader;
    String fqcn = "";
    boolean currentContext = false;
```

## New source input3:
```java
    RegionClassLoader regionClassLoader = this.regionClassLoader;
    String fqcn = "com.example.NonExistentClass";
    boolean currentContext = true;
```

## New source input4:
```java
    RegionClassLoader regionClassLoader = this.regionClassLoader;
    String fqcn = "com.example.MyClass";
    boolean currentContext = false;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    RegionClassLoader regionClassLoader = this.regionClassLoader;
    String fqcn = "";
    boolean currentContext = true;
    String fqcn2 = "";
    boolean currentContext2 = true;
    ClassLoader childClassLoader = new URLClassLoader(new URL[0], regionClassLoader);
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.