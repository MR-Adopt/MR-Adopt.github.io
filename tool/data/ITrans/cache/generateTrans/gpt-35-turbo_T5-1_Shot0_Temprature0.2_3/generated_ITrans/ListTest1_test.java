package com.alibaba.fastjson2.internal.processor.collections;

import com.alibaba.fastjson2.annotation.JSONCompiled;
import lombok.Data;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


import com.alibaba.fastjson2.JSON.*;
import com.alibaba.fastjson.TypeReference;
import java.util.Arrays;

import com.alibaba.fastjson.JSON;
import java.util.ArrayList;
import java.util.List;

public class ListTest1_test {
    public static List<Object> inputTransformation_test(List<Integer> v01) {
        String str2 = JSON.toJSONString(v01);
        java.lang.reflect.Type listType = new com.alibaba.fastjson.TypeReference<List<Integer>>() {}.getType();
        List<Object> transformed_inputs = new ArrayList<>();
        transformed_inputs.add(str2);
        transformed_inputs.add(listType);
        return transformed_inputs;
    }
}