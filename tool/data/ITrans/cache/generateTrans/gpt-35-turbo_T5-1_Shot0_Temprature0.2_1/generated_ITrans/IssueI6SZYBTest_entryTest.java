package cn.hutool.json;

import cn.hutool.core.lang.Pair;
import org.junit.Assert;
import org.junit.Test;
import java.util.AbstractMap;
import java.util.Map;


import cn.hutool.json.JSONUtil;
import cn.hutool.json.JSONUtil.*;
import java.util.List;
import java.util.Arrays;

public class IssueI6SZYBTest_entryTest {
    public static List<Object> inputTransformation_entryTest(Map.Entry<String,Integer> pair)  {
        String jsonString = JSONUtil.toJsonStr(pair);
        Class beanClass = AbstractMap.SimpleEntry.class;
        List<Object> transformed_inputs = Arrays.asList(jsonString, beanClass);
        return transformed_inputs;
    }
}