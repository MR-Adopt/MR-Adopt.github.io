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


# OTHER INPUT PAIRS 
## Input pair1:
```java
String fqcn = "";
boolean currentContext = true;
ClassLoader systemLoader = this.getClass().getClassLoader();
String fqcn2 = "";
boolean currentContext2 = true;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], this.getClass().getClassLoader(), mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair2:
```java
String fqcn = "com.example.MyClass";
boolean currentContext = true;
ClassLoader systemLoader = this.getClass().getClassLoader();
String fqcn2 = "com.example.MyClass";
boolean currentContext2 = true;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], this.getClass().getClassLoader(), mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair3:
```java
String fqcn = "org.apache.commons.logging.Log";
boolean currentContext = false;
ClassLoader systemLoader = this.getClass().getClassLoader();
String fqcn2 = "org.apache.commons.logging.Log";
boolean currentContext2 = false;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], this.getClass().getClassLoader(), mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair4:
```java
String fqcn = "com.example.MyClass";
boolean currentContext = true;
ClassLoader systemLoader = Thread.currentThread().getContextClassLoader();
String fqcn2 = "com.example.MyClass";
boolean currentContext2 = true;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], this.getClass().getClassLoader(), mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair5:
```java
String fqcn = "com.example.MyClass";
boolean currentContext = false;
ClassLoader systemLoader = ClassLoader.getSystemClassLoader();
String fqcn2 = "com.example.MyClass";
boolean currentContext2 = false;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], this.getClass().getClassLoader(), mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair6:
```java
String fqcn = "com.example.MyClass";
boolean currentContext = true;
ClassLoader systemLoader = null;
String fqcn2 = "com.example.MyClass";
boolean currentContext2 = true;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], this.getClass().getClassLoader(), mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair7:
```java
String fqcn = "";
boolean currentContext = false;
ClassLoader systemLoader = this.getClass().getClassLoader().getParent();
String fqcn2 = "";
boolean currentContext2 = false;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], this.getClass().getClassLoader(), mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair8:
```java
String fqcn = "java.util.ArrayList";
boolean currentContext = true;
ClassLoader systemLoader = ClassLoader.getSystemClassLoader();
String fqcn2 = "java.util.ArrayList";
boolean currentContext2 = true;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], ClassLoader.getSystemClassLoader(), mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair9:
```java
String fqcn = "com.example.MyClass";
boolean currentContext = false;
ClassLoader systemLoader = ClassLoader.getSystemClassLoader();
String fqcn2 = "com.example.MyClass";
boolean currentContext2 = false;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], ClassLoader.getSystemClassLoader(), mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair10:
```java
String fqcn = "org.slf4j.Logger";
boolean currentContext = true;
ClassLoader systemLoader = Thread.currentThread().getContextClassLoader();
String fqcn2 = "org.slf4j.Logger";
boolean currentContext2 = true;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], Thread.currentThread().getContextClassLoader(), mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair11:
```java
String fqcn = "java.lang.String";
boolean currentContext = true;
ClassLoader systemLoader = ClassLoader.getSystemClassLoader();
String fqcn2 = "java.lang.String";
boolean currentContext2 = true;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], ClassLoader.getSystemClassLoader(), mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair12:
```java
String fqcn = "org.slf4j.Logger";
boolean currentContext = true;
ClassLoader systemLoader = null;
String fqcn2 = "org.slf4j.Logger";
boolean currentContext2 = true;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], null, mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```

## Input pair13:
```java
String fqcn = "";
boolean currentContext = false;
ClassLoader systemLoader = null;
String fqcn2 = "";
boolean currentContext2 = false;
ArtifactClassLoader serviceClassLoader = new MuleArtifactClassLoader("test", new ApplicationDescriptor("test"), new URL[0], null, mock(ClassLoaderLookupPolicy.class));
ClassLoader serviceLoader = serviceClassLoader.getClassLoader();
```



# OUTPUT FORMAT
```java
public class ArtifactAwareContextSelectorTestCase_returnsMuleLoggerContextForInternalArtifactClassLoader {
    public static List<Object> inputTransformation_returnsMuleLoggerContextForInternalArtifactClassLoader(String fqcn, boolean currentContext, ClassLoader systemLoader)  {
        // TODO
        String fqcn2 = 
		ClassLoader serviceLoader = 
		boolean currentContext2 = 
		List<Object> transformed_inputs = Arrays.asList(fqcn2, serviceLoader, currentContext2);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.