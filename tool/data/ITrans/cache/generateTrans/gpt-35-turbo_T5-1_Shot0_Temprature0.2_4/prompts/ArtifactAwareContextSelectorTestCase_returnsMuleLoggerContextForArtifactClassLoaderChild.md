# METHOD UNDER TEST
```java
@Override
public LoggerContext getContext(String fqcn, ClassLoader classLoader, boolean currentContext, URI configLocation) {
    return cache.getLoggerContext(resolveLoggerContextClassLoader(classLoader));
}

```


# TEST CASE
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


# OTHER INPUT PAIRS 
## Input pair1:
```java
RegionClassLoader regionClassLoader = this.regionClassLoader;
String fqcn = "";
boolean currentContext = true;
String fqcn2 = "";
boolean currentContext2 = true;
ClassLoader childClassLoader = new URLClassLoader(new URL[0], regionClassLoader);
```

## Input pair2:
```java
RegionClassLoader regionClassLoader = this.regionClassLoader;
String fqcn = "com.example.MyClass";
boolean currentContext = true;
String fqcn2 = "com.example.MyClass";
boolean currentContext2 = true;
ClassLoader childClassLoader = new URLClassLoader(new URL[0], regionClassLoader);
```

## Input pair3:
```java
RegionClassLoader regionClassLoader = this.regionClassLoader;
String fqcn = "org.apache.commons.logging.Log";
boolean currentContext = false;
String fqcn2 = "org.apache.commons.logging.Log";
boolean currentContext2 = false;
ClassLoader childClassLoader = new URLClassLoader(new URL[0], regionClassLoader);
```

## Input pair4:
```java
RegionClassLoader regionClassLoader = this.regionClassLoader;
String fqcn = "com.example.AnotherClass";
boolean currentContext = true;
String fqcn2 = "com.example.AnotherClass";
boolean currentContext2 = true;
ClassLoader childClassLoader = new URLClassLoader(new URL[0], regionClassLoader);
```

## Input pair5:
```java
RegionClassLoader regionClassLoader = this.regionClassLoader;
String fqcn = "";
boolean currentContext = false;
String fqcn2 = "";
boolean currentContext2 = false;
ClassLoader childClassLoader = new URLClassLoader(new URL[0], regionClassLoader);
```

## Input pair6:
```java
RegionClassLoader regionClassLoader = this.regionClassLoader;
String fqcn = "com.example.Logger";
boolean currentContext = true;
String fqcn2 = "com.example.Logger";
boolean currentContext2 = true;
ClassLoader childClassLoader = new URLClassLoader(new URL[0], regionClassLoader);
```

## Input pair7:
```java
RegionClassLoader regionClassLoader = this.regionClassLoader;
String fqcn = "com.example.Logger";
boolean currentContext = true;
String fqcn2 = "com.example.Logger";
boolean currentContext2 = false;
ClassLoader childClassLoader = new URLClassLoader(new URL[0], regionClassLoader);
```

## Input pair8:
```java
RegionClassLoader regionClassLoader = this.regionClassLoader;
String fqcn = "com.example.MyClass";
boolean currentContext = false;
String fqcn2 = "com.example.MyClass";
boolean currentContext2 = false;
ClassLoader childClassLoader = new URLClassLoader(new URL[0], regionClassLoader);
```



# OUTPUT FORMAT
```java
public class ArtifactAwareContextSelectorTestCase_returnsMuleLoggerContextForArtifactClassLoaderChild {
    public static List<Object> inputTransformation_returnsMuleLoggerContextForArtifactClassLoaderChild(String fqcn, boolean currentContext, RegionClassLoader regionClassLoader)  {
        // TODO
        String fqcn2 = 
		ClassLoader childClassLoader = 
		boolean currentContext2 = 
		List<Object> transformed_inputs = Arrays.asList(fqcn2, childClassLoader, currentContext2);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.