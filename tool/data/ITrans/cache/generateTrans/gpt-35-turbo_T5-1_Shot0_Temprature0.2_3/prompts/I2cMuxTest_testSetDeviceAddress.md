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


# TEST CASE
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
SOURCE INPUT: `i2cMux`,`deviceAddress`
FOLLOW UP INPUT: `i2cMux2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceAddress = "0x70";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair2:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceAddress = "0x71";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair3:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceAddress = "0x75";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair4:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceAddress = "0x77";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair5:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceAddress = "0x6F";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair6:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceAddress = "0x80";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair7:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceAddress = "0x70";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
i2cMux.setDeviceAddress(deviceAddress);
```

## Input pair8:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceAddress = "0x70";
I2cMux i2cMux2 = i2cMux;
```

## Input pair9:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceAddress = "0x72";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair10:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceAddress = "0x73";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair11:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceAddress = "0x74";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```



# OUTPUT FORMAT
```java
public class I2cMuxTest_testSetDeviceAddress {
    public static I2cMux inputTransformation_testSetDeviceAddress(I2cMux i2cMux, String deviceAddress)  {
        // TODO
        I2cMux i2cMux2 = 
		return i2cMux2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.