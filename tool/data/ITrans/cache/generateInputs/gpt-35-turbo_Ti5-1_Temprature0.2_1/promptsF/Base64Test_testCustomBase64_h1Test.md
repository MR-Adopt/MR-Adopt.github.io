# ORIGINAL TEST CASE
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


# NEW SOURCE INPUTS
## New source input0:
```java
    byte[] testDataBytes = new byte[]{};
```

## New source input1:
```java
    byte[] testDataBytes = new byte[]{0x00, 0x01, 0x02};
```

## New source input2:
```java
    byte[] testDataBytes = new byte[]{0x7F, (byte) 0x80, (byte) 0xFF};
```

## New source input3:
```java
    byte[] testDataBytes = new byte[]{(byte) 0xFF, (byte) 0xFF, (byte) 0xFF};
```

## New source input4:
```java
    byte[] testDataBytes = new byte[]{(byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00};
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    byte[] testDataBytes = BASE_64_TEST_DATA.getBytes();
    String input2 = "SGVsbG8gV29ybGQ=";
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.