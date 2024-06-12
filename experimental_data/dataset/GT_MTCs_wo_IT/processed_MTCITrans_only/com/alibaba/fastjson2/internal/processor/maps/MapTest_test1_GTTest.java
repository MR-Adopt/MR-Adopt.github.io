package com.alibaba.fastjson2.internal.processor.maps;

import com.alibaba.fastjson2.JSON.*;

import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSONWriter;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import com.alibaba.fastjson2.annotation.JSONField;
import lombok.Data;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import com.alibaba.fastjson.TypeReference;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertSame;

public class MapTest_test1_GTTest {
//     @Test
//     public void test1_h() {
//         Map<String, Integer> v01 = new HashMap<>();
//         v01.put("123", 123);
//         v01.put("12x", 123);
// 
//         String str = JSON.toJSONString(v01);
//         Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>(){}.getType());
//         assertEquals(v01, v02);
//     }
// 
// //     public static List<Object> inputTransformation_test1(Map<String, Integer> v01) {
// //         TypeReference<Map<String, Integer>> typeRef = new TypeReference<Map<String, Integer>>() {};
// //         String str = JSON.toJSONString(v01);
// //         List<Object> transformed_inputs = Arrays.asList(str, typeRef.getType());
// //         return transformed_inputs;
// //     }
// // 
    @Test
    public void test1_IT() {
        Map<String, Integer> v01 = new HashMap<>();
        v01.put("123", 123);
        v01.put("12x", 123);

        List<Object> transformed_inputs = MapTest_test1_GT.inputTransformation_test1(v01);
        
        String str2 = (String) transformed_inputs.get(0);
        Type mapType = (Type) transformed_inputs.get(1); // Type cast to java.lang.reflect.Type

        String str =  JSON.toJSONString(v01);
        Map<String, Integer> v02 = JSON.parseObject(str2, mapType);
        assertEquals(v01, v02);
    }

    @JSONCompiled
    public static class Bean {
        public Map<String, Item> v01;
    }

    @JSONCompiled(referenceDetect = false)
    public static class Bean1 {
        public Map<String, Item> v01;
    }

    @JSONCompiled
    @Data
    public static class Item {
        public int id;

        public Item() {
        }

        public Item(@JSONField(name = "id") int id) {
            this.id = id;
        }
    }
}