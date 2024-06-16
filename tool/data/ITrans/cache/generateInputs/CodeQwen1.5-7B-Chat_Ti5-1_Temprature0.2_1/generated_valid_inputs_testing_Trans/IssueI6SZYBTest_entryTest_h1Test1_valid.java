package cn.hutool.json;

import cn.hutool.json.IssueI6SZYBTest_entryTest;

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

public class IssueI6SZYBTest_entryTest_h1Test1_valid {

    @Test
    public void entryTest_h1Test1() {
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("1234567890", Integer.MAX_VALUE);
		List<Object> transformed_inputs = IssueI6SZYBTest_entryTest.inputTransformation_entryTest(pair);
    String jsonString  = (String) transformed_inputs.get(0);
    Class beanClass  = (Class) transformed_inputs.get(1);
        String jsonStr = JSONUtil.toJsonStr(pair);
        final Map.Entry bean = (Entry) JSONUtil.toBean(jsonString, beanClass);
        Assert.assertEquals(pair, bean);
    }
}

