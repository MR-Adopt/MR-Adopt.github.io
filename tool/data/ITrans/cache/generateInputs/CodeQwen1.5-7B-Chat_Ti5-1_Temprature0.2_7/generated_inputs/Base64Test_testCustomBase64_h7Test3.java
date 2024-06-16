package se.michaelthelin.spotify;

import se.michaelthelin.spotify.Base64;
import se.michaelthelin.spotify.Base64.*;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class Base64Test_testCustomBase64_h7Test3 {

    private static final String BASE_64_TEST_DATA = "Hello World";

    private static final String BASE_64_TEST_DATA_ENCODED = "SGVsbG8gV29ybGQ=";

    @Test
    public void testCustomBase64_h7Test3() {
    byte[] testDataBytes = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
    String input2 = "AAAAAAAAAAAAAA==";
        String encoded = Base64.encode(testDataBytes);
        byte[] decoded = Base64.decode(input2);
        Assertions.assertArrayEquals(testDataBytes, decoded);
    }
}

