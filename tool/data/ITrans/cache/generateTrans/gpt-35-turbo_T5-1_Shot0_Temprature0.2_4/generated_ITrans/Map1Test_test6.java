package com.alibaba.fastjson2.internal.processor.maps;

import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import java.math.BigInteger;
import java.util.UUID;
import static org.junit.jupiter.api.Assertions.assertEquals;


import com.alibaba.fastjson2.JSON.*;
import java.lang.reflect.Type;
import java.util.Arrays;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.TypeReference;

import java.math.BigDecimal;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Map1Test_test6 {
    public static List<Object> inputTransformation_test6(Map<String, BigDecimal> v01) {
        String str2 = JSON.toJSONString(v01);
        TypeReference<Map<String, BigDecimal>> mapType = new TypeReference<Map<String, BigDecimal>>() {
        };
        Map<String, BigDecimal> v02 = JSON.parseObject(str2, mapType.getType());
        List<Object> transformed_inputs = Arrays.asList(str2, mapType);
        return transformed_inputs;
    }
}