# REQUIRED DELIVERABLE
## New input pair0:
```java
    StartupListener startUpListener1 = mock(StartupListener.class);
    StartupListener startUpListener2 = mock(StartupListener.class);
    singleAppDeploymentService.addStartupListener(startUpListener1);
    singleAppDeploymentService.addStartupListener(startUpListener2);
    assertThat(singleAppDeploymentService.getStartupListeners(), hasItems(startUpListener1, startUpListener2));
```

## New input pair1:
```java
    StartupListener startUpListener1 = mock(StartupListener.class);
    StartupListener startUpListener2 = new StartupListener() {
        @Override
        public void onStartup() {
            // Empty implementation
        }
    };
    singleAppDeploymentService.addStartupListener(startUpListener1);
    singleAppDeploymentService.addStartupListener(startUpListener2);
    assertThat(singleAppDeploymentService.getStartupListeners(), hasItems(startUpListener1, startUpListener2));
```

## New input pair2:
```java
    StartupListener startUpListener1 = mock(StartupListener.class);
    StartupListener startUpListener2 = new StartupListener() {
        @Override
        public void onStartup() {
            // Implementation that throws an exception
            throw new RuntimeException("Test exception");
        }
    };
    singleAppDeploymentService.addStartupListener(startUpListener1);
    singleAppDeploymentService.addStartupListener(startUpListener2);
    assertThat(singleAppDeploymentService.getStartupListeners(), hasItems(startUpListener1, startUpListener2));
```

## New input pair3:
```java
    StartupListener startUpListener1 = mock(StartupListener.class);
    StartupListener startUpListener2 = new StartupListener() {
        @Override
        public void onStartup() {
            // Implementation that does nothing
        }
    };
    singleAppDeploymentService.addStartupListener(startUpListener1);
    singleAppDeploymentService.addStartupListener(startUpListener2);
    assertThat(singleAppDeploymentService.getStartupListeners(), hasItems(startUpListener1, startUpListener2));
```

## New input pair4:
```java
    StartupListener startUpListener1 = mock(StartupListener.class);
    StartupListener startUpListener2 = new StartupListener() {
        @Override
        public void onStartup() {
            // Implementation that logs a message
            System.out.println("Startup event received");
        }
    };
    singleAppDeploymentService.addStartupListener(startUpListener1);
    singleAppDeploymentService.addStartupListener(startUpListener2);
    assertThat(singleAppDeploymentService.getStartupListeners(), hasItems(startUpListener1, startUpListener2));
```

Explanation:
The inferred relation between the source input and the follow-up input is that the `addStartupListener` method of the `SingleAppDeploymentService` class adds the source input to the list of startup listeners. The `getStartupListeners` method returns the list of startup listeners. Therefore, the follow-up input adds the source input to the list of startup listeners and then verifies that the list contains both the source input and the follow-up input.
