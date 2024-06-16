# METHOD UNDER TEST
```java
@Override
public void addStartupListener(StartupListener listener) {
    startupListeners.add(listener);
}

```


# TEST CASE
```java
@Test
public void startupListeners() {
    SingleAppDeploymentService singleAppDeploymentService = getSingleAppDeploymentService();
    StartupListener startUpListener1 = mock(StartupListener.class);
    StartupListener startUpListener2 = mock(StartupListener.class);
    singleAppDeploymentService.addStartupListener(startUpListener1);
    singleAppDeploymentService.addStartupListener(startUpListener2);
    assertThat(singleAppDeploymentService.getStartupListeners(), hasItems(startUpListener1, startUpListener2));
}

```
SOURCE INPUT: `startUpListener1`
FOLLOW UP INPUT: `startUpListener2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
StartupListener startUpListener1 = mock(StartupListener.class);
StartupListener startUpListener2 = mock(StartupListener.class);
```

## Input pair2:
```java
StartupListener startUpListener1 = null;
StartupListener startUpListener2 = null;
```



# OUTPUT FORMAT
```java
public class SingleAppDeploymentServiceTestCase_startupListeners {
    public static StartupListener inputTransformation_startupListeners(StartupListener startUpListener1)  {
        // TODO
        StartupListener startUpListener2 = 
		return startUpListener2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.