package com.alibaba.fastjson2.internal.processor.collections;

import com.alibaba.fastjson2.internal.processor.collections.ListTest1_test;

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

public class ListTest1_test_h8Test4_valid {

    @Test
    public void test_h8Test4() {
    List<Integer> v01 = new ArrayList<>();
    int id = 1234567890;
    v01.add(id);
        String str = JSON.toJSONString(v01);
        List<Integer> v02 = JSON.parseObject(str, new TypeReference<List<Integer>>() {
        }.getType());
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

