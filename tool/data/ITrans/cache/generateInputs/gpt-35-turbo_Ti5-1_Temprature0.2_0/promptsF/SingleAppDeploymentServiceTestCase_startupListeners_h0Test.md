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
SOURCE INPUT: `startUpListener1`
FOLLOW UP INPUT: `startUpListener2`


# METHOD UNDER TEST
```java
@Override
public void addStartupListener(StartupListener listener) {
    startupListeners.add(listener);
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
    StartupListener startUpListener1 = mock(StartupListener.class);
```

## New source input1:
```java
    StartupListener startUpListener1 = new StartupListener() {
        @Override
        public void onStartup() {
            // Custom implementation for onStartup method
        }
```

## New source input2:
```java
    StartupListener startUpListener1 = null;
```

## New source input3:
```java
    StartupListener startUpListener1 = new StartupListener() {
        @Override
        public void onStartup() {
            throw new RuntimeException("Error during startup");
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    StartupListener startUpListener1 = mock(StartupListener.class);
    StartupListener startUpListener2 = mock(StartupListener.class);
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.