package com.alibaba.fastjson2.internal.processor.maps;

import com.alibaba.fastjson2.internal.processor.maps.Map1Test_test4;

import com.alibaba.fastjson2.JSON.*;
import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import com.alibaba.fastjson.TypeReference;
import java.lang.reflect.Type;
import java.util.List;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class Map1Test_test4_h5Test1_valid {

    @JSONCompiled
    public static class Bean {

        public Map<String, String> v01;
    }

    @JSONCompiled
    public static class Bean1 {

        public Map<String, Integer> v01;
    }

    @JSONCompiled
    public static class Bean2 {

        public Map<String, Long> v01;
    }

    @JSONCompiled
    public static class Bean3 {

        public Map<String, Boolean> v01;
    }

    @Test
    public void test4_h5Test1() {
    Map<String, Float> v01 = new HashMap<>();
    v01.put("101", 1F);
    v01.put("102", 2F);
    v01.put("103", 3F);
		List<Object> transformed_inputs = Map1Test_test4.inputTransformation_test4(v01);
    String str2  = (String) transformed_inputs.get(0);
        String str = JSON.toJSONString(v01);
        Map<String, Float> v02 = JSON.parseObject(str, new TypeReference<Map<String, Float>>() {
        }.getType());
        assertEquals(v01, v02);
    }

    @JSONCompiled
    public static class Bean4 {

        public Map<String, Float> v01;
    }

    @JSONCompiled
    public static class Bean5 {

        public Map<String, Double> v01;
    }

    @JSONCompiled
    public static class Bean6 {

        public Map<String, BigDecimal> v01;
    }

    @JSONCompiled
    public static class Bean7 {

        public Map<String, BigInteger> v01;
    }

    @JSONCompiled
    public static class Bean8 {

        public Map<String, UUID> v01;
    }
}

