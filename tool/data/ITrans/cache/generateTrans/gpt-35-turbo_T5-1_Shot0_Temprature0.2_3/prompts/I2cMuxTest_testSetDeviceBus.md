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


# TEST CASE
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


# OTHER INPUT PAIRS 
## Input pair1:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "1";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair2:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "0";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
i2cMux.setDeviceBus(deviceBus);
```

## Input pair3:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "7";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
i2cMux.setDeviceBus(deviceBus);
```

## Input pair4:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "3";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
i2cMux.setDeviceBus(deviceBus);
```

## Input pair5:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "5";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
i2cMux.setDeviceBus(deviceBus);
```

## Input pair6:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "2";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
i2cMux.setDeviceBus(deviceBus);
```

## Input pair7:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "0";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair8:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "7";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair9:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "3";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair10:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "5";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair11:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "2";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
```

## Input pair12:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "0";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
i2cMux.setDeviceBus(deviceBus);
i2cMux2.setDeviceBus(deviceBus);
```

## Input pair13:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "7";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
i2cMux.setDeviceBus(deviceBus);
i2cMux2.setDeviceBus(deviceBus);
```

## Input pair14:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "3";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
i2cMux.setDeviceBus(deviceBus);
i2cMux2.setDeviceBus(deviceBus);
```

## Input pair15:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "5";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
i2cMux.setDeviceBus(deviceBus);
i2cMux2.setDeviceBus(deviceBus);
```

## Input pair16:
```java
I2cMux i2cMux = (I2cMux) Runtime.start("i2cMux", "I2cMux");
String deviceBus = "2";
I2cMux i2cMux2 = (I2cMux) Runtime.start("i2cMux", "I2cMux");
i2cMux.setDeviceBus(deviceBus);
i2cMux2.setDeviceBus(deviceBus);
```



# OUTPUT FORMAT
```java
public class I2cMuxTest_testSetDeviceBus {
    public static I2cMux inputTransformation_testSetDeviceBus(I2cMux i2cMux, String deviceBus)  {
        // TODO
        I2cMux i2cMux2 = 
		return i2cMux2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.