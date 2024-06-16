package com.alibaba.fastjson2.internal.processor.collections;

import com.alibaba.fastjson2.JSON.*;
import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import java.util.List;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class JSONArrayTest_test_h4Test4 {

    @Test
    public void test_h4Test4() {
    JSONArray v01 = new JSONArray();
    v01.add(BigDecimal.valueOf(123.456));
    String str2 = JSON.toJSONString(v01);
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
