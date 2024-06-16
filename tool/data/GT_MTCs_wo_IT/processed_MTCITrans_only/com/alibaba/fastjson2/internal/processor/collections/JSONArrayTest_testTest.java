package com.alibaba.fastjson2.internal.processor.collections;

import com.alibaba.fastjson2.JSON.*;

import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class JSONArrayTest_testTest {
    @Test
    public void test_h_pre() {
        Bean bean = new Bean();
        bean.v01 = new JSONArray();
        // Class<?> clazz = Bean.class;
        Class<Bean> clazz = (Class<Bean>) Bean.class;
        String str2 = JSON.toJSONString(bean);

        String str = JSON.toJSONString(bean);
        Bean bean1 = JSON.parseObject(str2, clazz);
        assertEquals(bean.v01, bean1.v01);
    }

//     @Test
//     public void test_h() {
//         JSONArray v01 = new JSONArray();
//         String str2 = JSON.toJSONString(v01);
// 
//         String str = JSON.toJSONString(v01);
//         JSONArray v02 = JSON.parseObject(str2, JSONArray.class);
//         assertEquals(v01, v02);
//     }
// 
// //     public static List<Object> inputTransformation_test(JSONArray v01) {
// //         Class<JSONArray> clazz = JSONArray.class;
// //         String str = JSON.toJSONString(v01);
// //         List<Object> transformed_inputs = Arrays.asList(str, clazz);
// //         return transformed_inputs;
// //     }
// // 
// // 
    @Test
    public void test_IT() {
        JSONArray v01 = new JSONArray();
        
        List<Object> transformed_inputs = JSONArrayTest_test.inputTransformation_test(v01);
        
        String str2 = (String) transformed_inputs.get(0);
        Class<JSONArray> clazz = (Class<JSONArray>) transformed_inputs.get(1);

        String str =  JSON.toJSONString(v01);
        JSONArray v02 = JSON.parseObject(str2, clazz);
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