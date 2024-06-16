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


# TEST CASE
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


# OTHER INPUT PAIRS 
## Input pair1:
```java
String randomString = "randomString";
byte[] randomStringBytes = { 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103 };
```

## Input pair2:
```java
String randomString = "";
byte[] randomStringBytes = {};
```

## Input pair3:
```java
String randomString = "1234567890";
byte[] randomStringBytes = { 49, 50, 51, 52, 53, 54, 55, 56, 57, 48 };
```

## Input pair4:
```java
String randomString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
byte[] randomStringBytes = { 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90 };
```

## Input pair5:
```java
String randomString = " !@#$%^&*()_+-={}[]:\";'<>?,./";
byte[] randomStringBytes = { 32, 33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 95, 43, 45, 61, 123, 125, 91, 93, 58, 34, 59, 39, 60, 62, 63, 44, 46, 47 };
```

## Input pair6:
```java
String randomString = "randomStringrandomStringrandomStringrandomStringrandomStringrandomStringrandomStringrandomStringrandomStringrandomString";
byte[] randomStringBytes = { 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103, 83, 116, 114, 105, 110, 103, 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103, 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103, 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103, 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103 };
```

## Input pair7:
```java
String randomString = "   randomString   ";
byte[] randomStringBytes = { 32, 32, 32, 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103, 32, 32, 32 };
```

## Input pair8:
```java
String randomString = "randomString123";
byte[] randomStringBytes = { 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103, 49, 50, 51 };
```

## Input pair9:
```java
String randomString = "randomString!@#$";
byte[] randomStringBytes = { 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103, 33, 64, 35, 36 };
```

## Input pair10:
```java
String randomString = "12345";
byte[] randomStringBytes = { 49, 50, 51, 52, 53 };
```

## Input pair11:
```java
String randomString = " ";
byte[] randomStringBytes = { 32 };
```

## Input pair12:
```java
String randomString = "randomStringrandomStringrandomStringrandomStringrandomStringrandomStringrandomStringrandomStringrandomStringrandomString";
byte[] randomStringBytes = { 114, 97, 110, 100, 111, 109, 83, 116, 114, 105, 110, 103, 83, 116, 114, 105, 110, 103, 83, 116, 114, 105, 110, 103, 83, 116, 114, 105, 110, 103, 83, 116, 114, 105, 110, 103, 83, 116, 114, 105, 110, 103, 83, 116, 114, 105, 110, 103, 83, 116, 114, 105, 110, 103 };
```



# OUTPUT FORMAT
```java
public class ConvertBinaryUtilTest_testConvertToLong {
    public static byte[] inputTransformation_testConvertToLong(String randomString)  {
        // TODO
        byte[] randomStringBytes = 
		return randomStringBytes;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.