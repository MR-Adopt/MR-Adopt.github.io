package org.apache.paimon.spark;

import org.junit.Assert;
import org.junit.jupiter.api.Test;
import java.nio.charset.StandardCharsets;
import java.util.Random;
import static org.apache.paimon.spark.utils.ConvertBinaryUtil.convertBytesToLong;
import static org.apache.paimon.spark.utils.ConvertBinaryUtil.convertStringToLong;


import org.apache.paimon.spark.utils.ConvertBinaryUtil;
import org.apache.paimon.spark.utils.ConvertBinaryUtil.*;
import java.util.List;
import java.util.Arrays;

public class ConvertBinaryUtilTest_testConvertToLong {
    public static byte[] inputTransformation_testConvertToLong(String randomString)  {
        byte[] randomStringBytes = randomString.getBytes();
        return randomStringBytes;
    }
}