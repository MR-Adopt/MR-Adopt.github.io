package se.michaelthelin.spotify;

import se.michaelthelin.spotify.Base64;
import se.michaelthelin.spotify.Base64.*;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class Base64Test_testCustomBase64_h4Test2 {

    private static final String BASE_64_TEST_DATA = "Hello World";

    private static final String BASE_64_TEST_DATA_ENCODED = "SGVsbG8gV29ybGQ=";

    @Test
    public void testCustomBase64_h4Test2() {
    byte[] testDataBytes = new byte[]{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    String input2 = "AAAAAAAAAAAAAAAAAAAAAA==";
        String encoded = Base64.encode(testDataBytes);
        byte[] decoded = Base64.decode(input2);
        Assertions.assertArrayEquals(testDataBytes, decoded);
    }
}

