package com.alibaba.fastjson2.internal.processor.collections;

import com.alibaba.fastjson2.JSONArray;
import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSON.*;

import java.util.Arrays;
import java.util.List;

public class JSONArrayTest_test {
    public static List<Object> inputTransformation_test(JSONArray v01) {
        String str2 = JSON.toJSONString(v01);
        Class<JSONArray> clazz = JSONArray.class;
        List<Object> transformed_inputs = Arrays.asList(str2, clazz);
        return transformed_inputs;
    }
}