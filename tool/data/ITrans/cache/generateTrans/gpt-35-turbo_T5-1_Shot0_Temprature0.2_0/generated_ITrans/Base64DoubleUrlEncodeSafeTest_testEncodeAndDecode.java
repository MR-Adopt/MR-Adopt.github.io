package org.tsugi.util;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;
import static org.junit.Assert.assertFalse;
import org.junit.Test;
import org.tsugi.util.Base64DoubleUrlEncodeSafe;


import org.tsugi.util.Base64DoubleUrlEncodeSafe.*;
import java.util.List;
import java.util.Arrays;

public class Base64DoubleUrlEncodeSafeTest_testEncodeAndDecode {
    public static String inputTransformation_testEncodeAndDecode(String input) throws java.io.UnsupportedEncodingException  {
        String encoded2 = Base64DoubleUrlEncodeSafe.encode(input);
        return encoded2;
    }
}