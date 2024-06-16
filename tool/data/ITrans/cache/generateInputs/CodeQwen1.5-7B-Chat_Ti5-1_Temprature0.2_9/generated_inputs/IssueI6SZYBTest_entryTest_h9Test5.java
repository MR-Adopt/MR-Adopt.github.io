package cn.hutool.json;

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

public class IssueI6SZYBTest_entryTest_h9Test5 {

    @Test
    public void entryTest_h9Test5() {
    Map.Entry<String, Integer> pair = new AbstractMap.SimpleEntry<>("key3", null);
    String jsonString = JSONUtil.toJsonStr(pair);
    Class beanClass = AbstractMap.SimpleEntry.class;
        String jsonStr = JSONUtil.toJsonStr(pair);
        final Map.Entry bean = (Entry) JSONUtil.toBean(jsonString, beanClass);
        Assert.assertEquals(pair, bean);
    }
}

