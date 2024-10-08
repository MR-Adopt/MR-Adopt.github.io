package com.alibaba.fastjson2.internal.processor.collections;

import com.alibaba.fastjson2.JSON.*;

import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class JSONArrayTest_test1_GT {
    @JSONCompiled
    public static class Bean {
        public JSONArray v01;
    }

    @Test
    public void test1_h() {
        JSONArray v01 = new JSONArray();
        String str2 = JSON.toJSONString(v01);

        String str = JSON.toJSONString(v01);
        JSONArray v02 = JSON.parseObject(str2, JSONArray.class);
        assertEquals(v01, v02);
    }

    public static List<Object> inputTransformation_test1(JSONArray v01) {
        Class<JSONArray> clazz = JSONArray.class;
        String str = JSON.toJSONString(v01);
        List<Object> transformed_inputs = Arrays.asList(str, clazz);
        return transformed_inputs;
    }

    @Test
    public void test1_IT() {
        JSONArray v01 = new JSONArray();
        
        List<Object> transformed_inputs = inputTransformation_test1(v01);
        
        String str2 = (String) transformed_inputs.get(0);
        Class<JSONArray> clazz = (Class<JSONArray>) transformed_inputs.get(1);

        String str =  JSON.toJSONString(v01);
        JSONArray v02 = JSON.parseObject(str2, clazz);
        assertEquals(v01, v02);
    }

    @JSONCompiled(referenceDetect = false)
    public static class Bean1 {
        public JSONArray v01;
    }
}