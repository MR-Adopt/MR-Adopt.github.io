/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.paimon.spark;

import org.apache.paimon.spark.utils.ConvertBinaryUtil.*;
import org.apache.paimon.spark.utils.ConvertBinaryUtil;
import org.junit.Assert;
import org.junit.jupiter.api.Test;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.util.Random;
import static org.apache.paimon.spark.utils.ConvertBinaryUtil.convertBytesToLong;
import static org.apache.paimon.spark.utils.ConvertBinaryUtil.convertStringToLong;

/**
 * Test for {@link ConvertBinaryUtil}.
 */
public class ConvertBinaryUtilTest_testConvertToLong_h4Test3 {

    @Test
    public void testConvertToLong_h4Test3() {
    String randomString = " !@#$%^&*()_+-={}[]:\";'<>?,./";
    byte[] randomStringBytes = { 32, 33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 95, 43, 45, 61, 123, 125, 91, 93, 58, 34, 59, 39, 60, 62, 63, 44, 46, 47 };
        Long convertStringValue = convertStringToLong(randomString);
        Long convertBytesValue = convertBytesToLong(randomStringBytes);
        Assert.assertEquals(convertStringValue, convertBytesValue);
    }

    public static String generateRandomString() {
        String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        Random random = new Random();
        int length = random.nextInt(100) + 1;
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < length; i++) {
            int index = random.nextInt(characters.length());
            stringBuilder.append(characters.charAt(index));
        }
        return stringBuilder.toString();
    }
}

