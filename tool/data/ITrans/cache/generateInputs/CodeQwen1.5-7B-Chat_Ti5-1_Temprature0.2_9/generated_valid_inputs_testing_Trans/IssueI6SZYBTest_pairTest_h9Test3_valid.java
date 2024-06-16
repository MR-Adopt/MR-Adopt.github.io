package cn.hutool.json;

import cn.hutool.json.IssueI6SZYBTest_pairTest;

import cn.hutool.json.JSONUtil;
import cn.hutool.json.JSONUtil.*;
import cn.hutool.core.lang.Pair;
import org.junit.Assert;
import org.junit.Test;
import java.util.AbstractMap;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;

public class IssueI6SZYBTest_pairTest_h9Test3_valid {

    @Test
    public void pairTest_h9Test3() {
    Pair<Integer, Integer> pair = Pair.of(Integer.MIN_VALUE, Integer.MIN_VALUE);
		List<Object> transformed_inputs = IssueI6SZYBTest_pairTest.inputTransformation_pairTest(pair);
    String jsonString  = (String) transformed_inputs.get(0);
    Class<Pair> beanClass  = (Class<Pair>) transformed_inputs.get(1);
        String jsonStr = JSONUtil.toJsonStr(pair);
        final Pair bean = JSONUtil.toBean(jsonString, beanClass);
        Assert.assertEquals(pair, bean);
    }
}

