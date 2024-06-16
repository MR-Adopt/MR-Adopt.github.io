package se.michaelthelin.spotify;

import se.michaelthelin.spotify.Base64Test_testCustomBase64;

import se.michaelthelin.spotify.Base64;
import se.michaelthelin.spotify.Base64.*;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class Base64Test_testCustomBase64_h3Test0_valid {

    private static final String BASE_64_TEST_DATA = "Hello World";

    private static final String BASE_64_TEST_DATA_ENCODED = "SGVsbG8gV29ybGQ=";

    @Test
    public void testCustomBase64_h3Test0() {
    byte[] testDataBytes = new byte[]{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    String input2  = Base64Test_testCustomBase64.inputTransformation_testCustomBase64(testDataBytes);
        String encoded = Base64.encode(testDataBytes);
        byte[] decoded = Base64.decode(input2);
        Assertions.assertArrayEquals(testDataBytes, decoded);
    }
}

