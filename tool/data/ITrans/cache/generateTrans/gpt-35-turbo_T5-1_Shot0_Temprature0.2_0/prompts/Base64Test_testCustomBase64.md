# METHOD UNDER TEST
```java
public static String encode(byte[] data) {
    char[] tbl = Arrays.copyOf(ENCODE_TABLE_BASE, ENCODE_TABLE_BASE.length);
    StringBuilder buffer = new StringBuilder();
    int pad = 0;
    for (int i = 0; i < data.length; i += 3) {
        int b = ((data[i] & 0xFF) << 16) & 0xFFFFFF;
        if (i + 1 < data.length) {
            b |= (data[i + 1] & 0xFF) << 8;
        } else {
            pad++;
        }
        if (i + 2 < data.length) {
            b |= (data[i + 2] & 0xFF);
        } else {
            pad++;
        }
        for (int j = 0; j < 4 - pad; j++) {
            int c = (b & 0xFC0000) >> 18;
            buffer.append(tbl[c]);
            b <<= 6;
        }
    }
    for (int j = 0; j < pad; j++) {
        buffer.append("=");
    }
    return buffer.toString();
}

public static byte[] decode(String data) {
    int[] tbl = Arrays.copyOf(DECODE_TABLE_BASE, DECODE_TABLE_BASE.length);
    byte[] bytes = data.getBytes();
    ByteArrayOutputStream buffer = new ByteArrayOutputStream();
    for (int i = 0; i < bytes.length; ) {
        int b;
        if (tbl[bytes[i]] != -1) {
            b = (tbl[bytes[i]] & 0xFF) << 18;
        } else // skip unknown characters
        {
            i++;
            continue;
        }
        int num = 0;
        if (i + 1 < bytes.length && tbl[bytes[i + 1]] != -1) {
            b = b | ((tbl[bytes[i + 1]] & 0xFF) << 12);
            num++;
        }
        if (i + 2 < bytes.length && tbl[bytes[i + 2]] != -1) {
            b = b | ((tbl[bytes[i + 2]] & 0xFF) << 6);
            num++;
        }
        if (i + 3 < bytes.length && tbl[bytes[i + 3]] != -1) {
            b = b | (tbl[bytes[i + 3]] & 0xFF);
            num++;
        }
        while (num > 0) {
            int c = (b & 0xFF0000) >> 16;
            buffer.write((char) c);
            b <<= 8;
            num--;
        }
        i += 4;
    }
    return buffer.toByteArray();
}

```


# TEST CASE
```java
@Test
public void testCustomBase64() {
    byte[] testDataBytes = BASE_64_TEST_DATA.getBytes();
    String encoded = Base64.encode(testDataBytes);
    String input2 = "SGVsbG8gV29ybGQ=";
    byte[] decoded = Base64.decode(input2);
    Assertions.assertArrayEquals(testDataBytes, decoded);
}

```
SOURCE INPUT: `testDataBytes`
FOLLOW UP INPUT: `input2`


# OTHER INPUT PAIRS 
## Input pair1:
```java
byte[] testDataBytes = BASE_64_TEST_DATA.getBytes();
String input2 = "SGVsbG8gV29ybGQ=";
```

## Input pair2:
```java
byte[] testDataBytes = new byte[]{(byte) 0x01, (byte) 0x02, (byte) 0x03};
String input2 = "AQID";
```

## Input pair3:
```java
byte[] testDataBytes = new byte[]{};
String input2 = "";
```

## Input pair4:
```java
byte[] testDataBytes = new byte[]{0x00, 0x01, 0x02};
String input2 = "AAEC";
```

## Input pair5:
```java
byte[] testDataBytes = new byte[]{0x00, 0x00, 0x00, 0x00};
String input2 = "AAAAAA==";
```

## Input pair6:
```java
byte[] testDataBytes = new byte[]{0x01, 0x02, 0x03, 0x04, 0x05};
String input2 = "AQIDBAU=";
```

## Input pair7:
```java
byte[] testDataBytes = new byte[]{0x7F, (byte) 0xFF};
String input2 = "f/8=";
```



# OUTPUT FORMAT
```java
public class Base64Test_testCustomBase64 {
    public static String inputTransformation_testCustomBase64(byte[] testDataBytes)  {
        // TODO
        String input2 = 
		return input2;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.