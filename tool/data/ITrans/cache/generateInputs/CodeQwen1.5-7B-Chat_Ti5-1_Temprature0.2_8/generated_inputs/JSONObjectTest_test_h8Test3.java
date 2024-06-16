package com.alibaba.fastjson2.internal.processor.maps;

import com.alibaba.fastjson2.JSON.*;
import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSONObject;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import java.util.List;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class JSONObjectTest_test_h8Test3 {

    @Test
    public void test_h8Test3() {
    JSONObject v01 = JSONObject.of("id", 1001, "name", "John Doe", "age", 25);
        String str = JSON.toJSONString(v01);
        JSONObject v02 = JSON.parseObject(str, JSONObject.class);
        assertEquals(v01, v02);
    }

    @JSONCompiled
    public static class Bean {

        public JSONObject v01;
    }

    @JSONCompiled(referenceDetect = false)
    public static class Bean1 {

        public JSONObject v01;
    }
}

