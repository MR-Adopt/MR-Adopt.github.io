# ORIGINAL TEST CASE
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
TEST INPUT: `startUpListener1`


# METHOD UNDER TEST
```java
@Override
public void addStartupListener(StartupListener listener) {
    startupListeners.add(listener);
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `startUpListener1`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    StartupListener startUpListener1 = mock(StartupListener.class);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 