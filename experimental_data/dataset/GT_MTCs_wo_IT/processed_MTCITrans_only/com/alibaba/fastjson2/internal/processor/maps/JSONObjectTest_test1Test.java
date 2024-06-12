package com.alibaba.fastjson2.internal.processor.maps;

import com.alibaba.fastjson2.JSON.*;

import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSONObject;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class JSONObjectTest_test1Test {
    @JSONCompiled
    public static class Bean {
        public JSONObject v01;
    }

//     @Test
//     public void test1_h() {
//         JSONObject v01 = JSONObject.of("id", 1001);
// 
//         String str = JSON.toJSONString(v01);
//         JSONObject v02 = JSON.parseObject(str, JSONObject.class);
//         assertEquals(v01, v02);
//     }
// 
// //     public static List<Object> inputTransformation_test1(JSONObject v01) {
// //         Class<JSONObject> clazz = JSONObject.class;
// //         String str = JSON.toJSONString(v01);
// //         List<Object> transformed_inputs = Arrays.asList(str, clazz);
// //         return transformed_inputs;
// //     }
// // 
    @Test
    public void test1_IT() {
        JSONObject v01 = JSONObject.of("id", 1001);
        
        List<Object> transformed_inputs = JSONObjectTest_test1.inputTransformation_test1(v01);
        
        String str2 = (String) transformed_inputs.get(0);
        Class<JSONObject> clazz = (Class<JSONObject>) transformed_inputs.get(1);

        String str =  JSON.toJSONString(v01);
        JSONObject v02 = JSON.parseObject(str2, clazz);
        assertEquals(v01, v02);
    }



    @JSONCompiled(referenceDetect = false)
    public static class Bean1 {
        public JSONObject v01;
    }
}