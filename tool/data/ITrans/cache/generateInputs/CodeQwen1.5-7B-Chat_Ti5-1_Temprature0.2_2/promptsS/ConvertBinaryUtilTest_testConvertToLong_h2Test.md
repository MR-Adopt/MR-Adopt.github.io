# ORIGINAL TEST CASE
```java
@Test
public void testConvertToLong() {
    String randomString = "randomString";
    byte[] randomStringBytes = { 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103 };
    Long convertStringValue = convertStringToLong(randomString);
    Long convertBytesValue = convertBytesToLong(randomStringBytes);
    Assert.assertEquals(convertStringValue, convertBytesValue);
}

```
TEST INPUT: `randomString`


# METHOD UNDER TEST
```java
public static Long convertStringToLong(String data) {
    byte[] bytes = utf8To8Byte(data);
    return convertBytesToLong(bytes);
}

public static long convertBytesToLong(byte[] bytes) {
    byte[] paddedBytes = paddingTo8Byte(bytes);
    long temp = 0L;
    for (int i = 7; i >= 0; i--) {
        temp = temp | (((long) paddedBytes[i] & 0xff) << (7 - i) * 8);
    }
    return temp;
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `randomString`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    String randomString = "randomString";
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 