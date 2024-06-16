package com.alibaba.fastjson2.internal.processor.collections;

import com.alibaba.fastjson2.internal.processor.collections.JSONArrayTest_test1;

import com.alibaba.fastjson2.JSON.*;
import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import java.util.List;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class JSONArrayTest_test1_h5Test1_valid {

    @JSONCompiled
    public static class Bean {

        public JSONArray v01;
    }

    @Test
    public void test1_h5Test1() {

        String str = JSON.toJSONString(v01);
        JSONArray v02 = JSON.parseObject(str2, JSONArray.class);
        assertEquals(v01, v02);
    }

    @JSONCompiled(referenceDetect = false)
    public static class Bean1 {

        public JSONArray v01;
    }
}

