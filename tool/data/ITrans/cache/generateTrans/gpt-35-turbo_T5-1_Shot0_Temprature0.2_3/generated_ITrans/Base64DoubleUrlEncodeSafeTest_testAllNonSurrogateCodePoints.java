package org.tsugi.util;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;
import static org.junit.Assert.assertFalse;
import org.junit.Test;
import org.tsugi.util.Base64DoubleUrlEncodeSafe;


import org.tsugi.util.Base64DoubleUrlEncodeSafe.*;
import java.util.List;
import java.util.Arrays;

public class Base64DoubleUrlEncodeSafeTest_testAllNonSurrogateCodePoints {
    public static String inputTransformation_testAllNonSurrogateCodePoints(String input) {
        String encoded = java.util.Base64.getUrlEncoder().encodeToString(input.getBytes());
        String doubleUrlEncoded = java.net.URLEncoder.encode(encoded, "UTF-8");
        String transformedInput = doubleUrlEncoded.replace(Base64DoubleUrlEncodeSafe.CHARACTER_TO_AVOID, Base64DoubleUrlEncodeSafe.REPLACEMENT_CHARACTER);
        return transformedInput;
    }
}