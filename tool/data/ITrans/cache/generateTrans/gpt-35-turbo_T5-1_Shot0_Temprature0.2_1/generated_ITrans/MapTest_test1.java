package com.alibaba.fastjson2.internal.processor.maps;

import com.alibaba.fastjson2.JSONWriter;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import com.alibaba.fastjson2.annotation.JSONField;
import lombok.Data;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertSame;


import com.alibaba.fastjson2.JSON.*;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.TypeReference;

import java.lang.reflect.Type;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MapTest_test1 {
    public static List<Object> inputTransformation_test1(Map<String, Integer> v01) {
        String str2 = JSON.toJSONString(v01);
        Type mapType = new TypeReference<Map<String, Integer>>() {}.getType();
        List<Object> transformed_inputs = Arrays.asList(str2, mapType);
        return transformed_inputs;
    }
}