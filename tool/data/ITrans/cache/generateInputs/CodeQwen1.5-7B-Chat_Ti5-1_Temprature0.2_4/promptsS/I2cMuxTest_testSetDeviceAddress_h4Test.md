# ORIGINAL TEST CASE
```java
@Test
public void testSetDeviceAddress() {
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceAddress = "0x70";
    I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    i2cMux.setDeviceAddress(deviceAddress);
    assertEquals(deviceAddress, i2cMux2.getDeviceAddress());
}

```
TEST INPUT: `i2cMux`,`deviceAddress`


# METHOD UNDER TEST
```java
/**
 * Sets the I2C Address of the i2cMux device.
 *
 * @param address
 *          default "0x70" range "0x70" - "0x77"
 */
@Override
public void setDeviceAddress(String address) {
    setAddress(address);
}

@Override
public String getDeviceAddress() {
    return config.address;
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `i2cMux`,`deviceAddress`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceAddress = "0x70";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 