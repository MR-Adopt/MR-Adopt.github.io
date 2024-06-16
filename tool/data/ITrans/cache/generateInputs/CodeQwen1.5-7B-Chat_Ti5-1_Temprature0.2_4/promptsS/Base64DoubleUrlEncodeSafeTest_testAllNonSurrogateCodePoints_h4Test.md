# ORIGINAL TEST CASE
```java
@Test
public void testAllNonSurrogateCodePoints() {
    char c;
    int i;
    StringBuffer sb = new StringBuffer();
    for (i = 1; i < 100; i++) {
        c = (char) i;
        sb.append(c);
    }
    String input = sb.toString();
    String encoded = Base64DoubleUrlEncodeSafe.encode(input);
    String encoded2 = "AQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRobHB0eHyAhIiMkJSYnKCkqKywtLi8wMTIzNDU2Nzg5Ojs8PT4_QEFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaW1xdXl9gYWJj";
    String decoded = Base64DoubleUrlEncodeSafe.decode(encoded2);
    assertEquals("Decoding did not produce the original string for input: " + input, input, decoded);
    try {
        String urlEncoded = java.net.URLEncoder.encode(encoded, "UTF-8");
    } catch (java.io.UnsupportedEncodingException e) {
        fail("Unxpected UnsupportedEncodingException for URLEncoder " + encoded);
    }
}

```
TEST INPUT: `input`


# METHOD UNDER TEST
```java
/**
 * Encodes a given string into a Base64-Double-UrlEncode-Safe string.
 *
 * @param data The input string to be encoded.
 * @return The Base64-Double-UrlEncode-Safe encoded string.
 */
public static String encode(String data) {
    if (data == null)
        return null;
    try {
        String encoded = java.util.Base64.getUrlEncoder().encodeToString(data.getBytes("UTF-8"));
        return encoded.replace(CHARACTER_TO_AVOID, REPLACEMENT_CHARACTER);
    } catch (java.io.UnsupportedEncodingException e) {
        // Unlikely
        e.printStackTrace();
        return null;
    }
}

/**
 * Decodes a Base64-Double-UrlEncode-Safe string into its original string representation.
 *
 * @param encoded The Base64-Double-UrlEncode-Safe string to be decoded.
 * @return The decoded original string.
 * @throws java.io.UnsupportedEncodingException If the input string contains invalid characters.
 */
public static String decode(String encoded) {
    if (encoded == null)
        return null;
    return new String(java.util.Base64.getUrlDecoder().decode(encoded.replace(REPLACEMENT_CHARACTER, CHARACTER_TO_AVOID)));
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `input`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    StringBuffer sb = new StringBuffer();
    String input = sb.toString();
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 