package cn.hutool.json;

import cn.hutool.core.lang.Pair;
import org.junit.Assert;
import org.junit.Test;


import cn.hutool.json.JSONUtil;
import cn.hutool.json.JSONUtil.*;

import java.util.AbstractMap;
import java.util.Arrays;
import java.util.List;
import java.util.Map;

public class IssueI6SZYBTest_entryTest {
    public static List<Object> inputTransformation_entryTest(Map.Entry<String,Integer> pair)  {
        String jsonString = "{\"" + pair.getKey() + "\":" + pair.getValue() + "}";
        Class beanClass = AbstractMap.SimpleEntry.class;
        List<Object> transformed_inputs = Arrays.asList(jsonString, beanClass);
        return transformed_inputs;
    }
}