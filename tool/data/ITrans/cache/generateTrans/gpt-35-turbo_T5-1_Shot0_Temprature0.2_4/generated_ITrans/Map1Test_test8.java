package com.alibaba.fastjson2.internal.processor.maps;

import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import java.math.BigDecimal;
import java.math.BigInteger;
import static org.junit.jupiter.api.Assertions.assertEquals;


import com.alibaba.fastjson2.JSON.*;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.TypeReference;

import java.lang.reflect.Type;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

public class Map1Test_test8 {
    public static List<Object> inputTransformation_test8(Map<String, UUID> v01) {
        String str2 = JSON.toJSONString(v01);
        Type mapType = new TypeReference<Map<String, UUID>>() {}.getType();
        List<Object> transformed_inputs = Arrays.asList(str2, mapType);
        return transformed_inputs;
    }
}