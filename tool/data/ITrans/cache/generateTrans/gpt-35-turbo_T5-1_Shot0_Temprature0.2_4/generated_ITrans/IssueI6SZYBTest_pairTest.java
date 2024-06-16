package cn.hutool.json;

import org.junit.Assert;
import org.junit.Test;
import java.util.AbstractMap;
import java.util.Map;


import cn.hutool.json.JSONUtil;
import cn.hutool.json.JSONUtil.*;
import java.util.List;
import java.util.Arrays;

import com.alibaba.fastjson.JSON;
import org.apache.commons.lang3.tuple.Pair;

public class IssueI6SZYBTest_pairTest {
    public static List<Object> inputTransformation_pairTest(Pair<Integer,Integer> pair)  {
        String jsonString = JSON.toJSONString(pair);
        Class<Pair> beanClass = Pair.class;
        List<Object> transformed_inputs = Arrays.asList(jsonString, beanClass);
        return transformed_inputs;
    }
}