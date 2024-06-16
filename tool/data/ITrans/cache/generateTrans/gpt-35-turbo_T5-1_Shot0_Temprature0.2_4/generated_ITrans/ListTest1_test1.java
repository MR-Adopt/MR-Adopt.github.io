package com.alibaba.fastjson2.internal.processor.collections;

import com.alibaba.fastjson2.annotation.JSONCompiled;
import lombok.Data;
import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import static org.junit.jupiter.api.Assertions.assertEquals;


import com.alibaba.fastjson2.JSON;
import com.alibaba.fastjson2.JSON.*;
import com.alibaba.fastjson.TypeReference;
import java.util.List;
import java.util.Arrays;

public class ListTest1_test1 {
    public static List<Object> inputTransformation_test1(List<String> v01) {
        String str2 = JSON.toJSONString(v01);
        java.lang.reflect.Type listType = new TypeReference<List<String>>() {}.getType();
        List<Object> transformed_inputs = Arrays.asList(str2, listType);
        return transformed_inputs;
    }
}