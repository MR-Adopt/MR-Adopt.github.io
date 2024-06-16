package se.michaelthelin.spotify;

import se.michaelthelin.spotify.Base64;
import se.michaelthelin.spotify.Base64.*;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class Base64Test_testCustomBase64_h1Test3 {

    private static final String BASE_64_TEST_DATA = "Hello World";

    private static final String BASE_64_TEST_DATA_ENCODED = "SGVsbG8gV29ybGQ=";

    @Test
    public void testCustomBase64_h1Test3() {
    byte[] testDataBytes = {30, 31, 32, 33, 34, 35, 36, 37, 38, 39};
    String input2 = "MzAyMzQ1Njc4OTM=";
        String encoded = Base64.encode(testDataBytes);
        byte[] decoded = Base64.decode(input2);
        Assertions.assertArrayEquals(testDataBytes, decoded);
    }
}

