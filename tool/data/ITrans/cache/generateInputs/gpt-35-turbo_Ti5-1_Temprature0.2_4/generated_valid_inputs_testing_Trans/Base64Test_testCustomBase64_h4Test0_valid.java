package se.michaelthelin.spotify;

import se.michaelthelin.spotify.Base64Test_testCustomBase64;

import se.michaelthelin.spotify.Base64;
import se.michaelthelin.spotify.Base64.*;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class Base64Test_testCustomBase64_h4Test0_valid {

    private static final String BASE_64_TEST_DATA = "Hello World";

    private static final String BASE_64_TEST_DATA_ENCODED = "SGVsbG8gV29ybGQ=";

    @Test
    public void testCustomBase64_h4Test0() {
    byte[] testDataBytes = BASE_64_TEST_DATA.getBytes();
    String input2  = Base64Test_testCustomBase64.inputTransformation_testCustomBase64(testDataBytes);
        String encoded = Base64.encode(testDataBytes);
        byte[] decoded = Base64.decode(input2);
        Assertions.assertArrayEquals(testDataBytes, decoded);
    }
}

