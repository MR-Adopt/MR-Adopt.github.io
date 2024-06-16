package com.alibaba.fastjson2.internal.processor.maps;

import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.UUID;
import static org.junit.jupiter.api.Assertions.assertEquals;


import com.alibaba.fastjson2.JSON.*;
import java.lang.reflect.Type;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.TypeReference;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Map1Test_test {
    public static List<Object> inputTransformation_test(Map<String, String> v01) {
        String str2 = JSON.toJSONString(v01);
        TypeReference<Map<String, String>> mapType = new TypeReference<Map<String, String>>() {
        };
        List<Object> transformed_inputs = Arrays.asList(str2, mapType);
        return transformed_inputs;
    }
}