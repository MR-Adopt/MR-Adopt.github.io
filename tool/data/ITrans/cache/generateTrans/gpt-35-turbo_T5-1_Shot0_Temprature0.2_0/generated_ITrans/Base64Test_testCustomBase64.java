package se.michaelthelin.spotify;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;


import se.michaelthelin.spotify.Base64;
import se.michaelthelin.spotify.Base64.*;
import java.util.List;
import java.util.Arrays;

public class Base64Test_testCustomBase64 {
    public static String inputTransformation_testCustomBase64(byte[] testDataBytes) {
        return Base64.encode(testDataBytes);
    }
}