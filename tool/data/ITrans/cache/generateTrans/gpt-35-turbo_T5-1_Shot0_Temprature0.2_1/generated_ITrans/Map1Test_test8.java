package com.alibaba.fastjson2.internal.processor.maps;

import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import java.math.BigDecimal;
import java.math.BigInteger;
import static org.junit.jupiter.api.Assertions.assertEquals;


import com.alibaba.fastjson2.JSON.*;
import java.lang.reflect.Type;
import java.util.List;
import java.util.Arrays;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.TypeReference;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

public class Map1Test_test8 {
    public static Map<String, Object> inputTransformation_test8(Map<String, UUID> v01) {
        String str2 = JSON.toJSONString(v01);
        TypeReference<Map<String, UUID>> mapType = new TypeReference<Map<String, UUID>>() {
        };
        Map<String, Object> transformed_inputs = new HashMap<>();
        transformed_inputs.put("str2", str2);
        transformed_inputs.put("mapType", mapType);
        return transformed_inputs;
    }
}