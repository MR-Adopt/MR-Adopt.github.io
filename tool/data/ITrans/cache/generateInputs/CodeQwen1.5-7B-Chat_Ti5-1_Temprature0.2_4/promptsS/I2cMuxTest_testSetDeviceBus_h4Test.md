# ORIGINAL TEST CASE
```java
@Test
public void testSetDeviceBus() {
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceBus = "1";
    I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    i2cMux.setDeviceBus(deviceBus);
    assertEquals(deviceBus, i2cMux2.getDeviceBus());
}

```
TEST INPUT: `i2cMux`,`deviceBus`


# METHOD UNDER TEST
```java
/**
 * Sets the I2C Bus the i2cMux is attached to.
 *
 * @param deviceBus
 *          default is "1", range "0" - "7".
 */
@Override
public void setDeviceBus(String deviceBus) {
    setBus(deviceBus);
}

@Override
public String getDeviceBus() {
    return config.bus;
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `i2cMux`,`deviceBus`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceBus = "1";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 