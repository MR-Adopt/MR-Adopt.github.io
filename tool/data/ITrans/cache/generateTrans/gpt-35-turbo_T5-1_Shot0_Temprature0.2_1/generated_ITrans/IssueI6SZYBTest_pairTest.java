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

public class IssueI6SZYBTest_pairTest {
    public static List<Object> inputTransformation_pairTest(Pair<Integer,Integer> pair)  {
        String jsonString = "{\"key\":" + pair.getLeft() + ",\"value\":" + pair.getRight() + "}";
        Class<Pair> beanClass = Pair.class;
        List<Object> transformed_inputs = Arrays.asList(jsonString, beanClass);
        return transformed_inputs;
    }
}