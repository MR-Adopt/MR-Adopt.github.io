package se.michaelthelin.spotify;

import se.michaelthelin.spotify.Base64;
import se.michaelthelin.spotify.Base64.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class Base64Test_testCustomBase64_GTTest {
  private static final String BASE_64_TEST_DATA = "Hello World";
  private static final String BASE_64_TEST_DATA_ENCODED = "SGVsbG8gV29ybGQ=";

//   @Test
//   public void testCustomBase64_h() {
//     byte[] testDataBytes = BASE_64_TEST_DATA.getBytes();
// 
//     String encoded = Base64.encode(testDataBytes);
//     Assertions.assertEquals(BASE_64_TEST_DATA_ENCODED, encoded);
//     String input2 = "SGVsbG8gV29ybGQ=";
//     byte[] decoded = Base64.decode(input2);
//     Assertions.assertArrayEquals(testDataBytes, decoded);
//   }
// 
  @Test
  public void testCustomBase64_IT() {
    byte[] testDataBytes = BASE_64_TEST_DATA.getBytes();

    String encoded = Base64.encode(testDataBytes);
    Assertions.assertEquals(BASE_64_TEST_DATA_ENCODED, encoded);
    String input2 = Base64Test_testCustomBase64_GT.inputTransformation_testCustomBase64(testDataBytes);
    byte[] decoded = Base64.decode(input2);
    Assertions.assertArrayEquals(testDataBytes, decoded);
  }

//   public static String inputTransformation_testCustomBase64(byte[] testDataBytes) {
//     String encoded = Base64.encode(testDataBytes);
//     return encoded;
//   }
}