package com.alibaba.fastjson2.internal.processor.maps;

import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;
import java.util.UUID;
import static org.junit.jupiter.api.Assertions.assertEquals;


import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSON.*;
import com.alibaba.fastjson.TypeReference;
import java.lang.reflect.Type;
import java.util.List;
import java.util.Arrays;

public class Map1Test_test1 {
    public static List<Object> inputTransformation_test1(Map<String, Integer> v01) {
        String str2 = JSON.toJSONString(v01);
        Type mapType = new TypeReference<Map<String, Integer>>() {}.getType();
        List<Object> transformed_inputs = Arrays.asList(str2, mapType);
        return transformed_inputs;
    }
}