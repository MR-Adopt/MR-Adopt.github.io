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
        // Convert the Map to a JSON string
        String str2 = JSON.toJSONString(v01);

        // Convert the JSON string back to a Map
        Map<String, UUID> mapType = JSON.parseObject(str2, new TypeReference<Map<String, UUID>>() {
        }.getType());

        // Create a map to store the transformed inputs
        Map<String, Object> transformedInputs = new HashMap<>();
        transformedInputs.put("str2", str2);
        transformedInputs.put("mapType", mapType);

        return transformedInputs;
    }
}