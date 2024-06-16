package com.alibaba.fastjson2.internal.processor.collections;

import com.alibaba.fastjson2.JSON.*;

import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import lombok.Data;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import com.alibaba.fastjson.TypeReference;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ListTest1_test {
    @Test
    public void test_h() {
        List<Integer> v01 = new ArrayList<>();
        int id = 123;
        v01.add(id);

        String str = JSON.toJSONString(v01);
        List<Integer> v02 = JSON.parseObject(str, new TypeReference<List<Integer>>(){}.getType());
        assertEquals(v01, v02);
    }

    public static List<Object> inputTransformation_test(List<Integer> v01) {
        TypeReference<List<Integer>> typeRef = new TypeReference<List<Integer>>() {};
        String str = JSON.toJSONString(v01);
        List<Object> transformed_inputs = Arrays.asList(str, typeRef.getType());
        return transformed_inputs;
    }

    @Test
    public void test_IT() {
        List<Integer> v01 = new ArrayList<>();
        int id = 123;
        v01.add(id);

        List<Object> transformed_inputs = inputTransformation_test(v01);
        
        String str2 = (String) transformed_inputs.get(0);
        java.lang.reflect.Type listType = (java.lang.reflect.Type) transformed_inputs.get(1); // Type cast to java.lang.reflect.Type

        String str =  JSON.toJSONString(v01);
        List<Integer> v02 = JSON.parseObject(str2, listType);
        assertEquals(v01, v02);
    }

    @JSONCompiled
    public static class Bean {
        public List<Item> v01;
    }

    @Data
    @JSONCompiled
    public static class Item {
        public int id;
    }

    @JSONCompiled
    public static class Bean1 {
        public List<String> v01;
    }
}