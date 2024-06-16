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
SOURCE INPUT: `i2cMux`,`deviceBus`
FOLLOW UP INPUT: `i2cMux2`


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


# NEW SOURCE INPUTS
## New source input0:
```java
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceBus = "0";
```

## New source input1:
```java
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceBus = "7";
```

## New source input2:
```java
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceBus = "3";
```

## New source input3:
```java
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceBus = "2";
```

## New source input4:
```java
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceBus = "8";
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
    String deviceBus = "1";
    I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.