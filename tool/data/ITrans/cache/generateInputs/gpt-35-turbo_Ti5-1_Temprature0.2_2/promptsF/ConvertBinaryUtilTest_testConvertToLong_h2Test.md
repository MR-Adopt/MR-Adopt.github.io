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
SOURCE INPUT: `randomString`
FOLLOW UP INPUT: `randomStringBytes`


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


# NEW SOURCE INPUTS
## New source input0:
```java
    String randomString = "";
```

## New source input1:
```java
    String randomString = "1234567890";
```

## New source input2:
```java
    String randomString = "   randomString   ";
```

## New source input3:
```java
    String randomString = "randomString123";
```

## New source input4:
```java
    String randomString = "randomString!@#$";
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    String randomString = "randomString";
    byte[] randomStringBytes = { 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103 };
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.