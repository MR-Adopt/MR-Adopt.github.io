package com.alibaba.fastjson2.internal.processor.collections;

import com.alibaba.fastjson2.internal.processor.collections.ListTest1_test1;

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

public class ListTest1_test1_h1Test0_valid {

    @JSONCompiled
    public static class Bean {

        public List<Item> v01;
    }

    @Data
    @JSONCompiled
    public static class Item {

        public int id;
    }

    @Test
    public void test1_h1Test0() {
List<String> v01 = new ArrayList<>();
String id = "123";
v01.add(id);
		List<Object> transformed_inputs = ListTest1_test1.inputTransformation_test1(v01);
String str2  = (String) transformed_inputs.get(0);
        String str = JSON.toJSONString(v01);
        List<String> v02 = JSON.parseObject(str, new TypeReference<List<String>>() {
        }.getType());
        assertEquals(v01, v02);
    }

    @JSONCompiled
    public static class Bean1 {

        public List<String> v01;
    }
}

