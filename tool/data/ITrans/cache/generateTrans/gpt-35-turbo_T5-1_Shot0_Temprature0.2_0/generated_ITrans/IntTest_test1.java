package com.alibaba.fastjson2.internal.processor.primitives;

import com.alibaba.fastjson2.annotation.JSONCompiled;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSON.*;
import java.util.List;
import java.util.Arrays;

public class IntTest_test1 {
    public static List<Object> inputTransformation_test1(Integer v01) {
        String str2 = JSON.toJSONString(v01);
        Class<Integer> clazz = Integer.class;
        List<Object> transformed_inputs = Arrays.asList(str2, clazz);
        return transformed_inputs;
    }
}