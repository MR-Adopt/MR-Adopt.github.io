package com.alibaba.fastjson2.internal.processor.collections;

import com.alibaba.fastjson2.internal.processor.collections.JSONArrayTest_test;

import com.alibaba.fastjson2.JSON.*;
import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import java.util.List;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class JSONArrayTest_test_h3Test3_valid {

    @Test
    public void test_h3Test3() {
    JSONArray v01 = new JSONArray();
    v01.add(BigDecimal.valueOf(123.456));
    v01.add(BigInteger.valueOf(1234567890123456789L));
		List<Object> transformed_inputs = JSONArrayTest_test.inputTransformation_test(v01);
    String str2  = (String) transformed_inputs.get(0);
        String str = JSON.toJSONString(v01);
        JSONArray v02 = JSON.parseObject(str2, JSONArray.class);
        assertEquals(v01, v02);
    }

    @JSONCompiled
    public static class Bean {

        public JSONArray v01;
    }

    @JSONCompiled(referenceDetect = false)
    public static class Bean1 {

        public JSONArray v01;
    }
}

