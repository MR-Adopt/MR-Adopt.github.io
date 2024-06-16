package com.alibaba.fastjson2.internal.processor.maps;

import com.alibaba.fastjson2.internal.processor.maps.MapTest_test1;

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

public class MapTest_test1_h0Test3_valid {

    @Test
    public void test1_h0Test3() {
        Map<String, Integer> v01 = new HashMap<>();
    v01.put("123", 0);
    v01.put("12x", 0);
        String str = JSON.toJSONString(v01);
        Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
        }.getType());
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

