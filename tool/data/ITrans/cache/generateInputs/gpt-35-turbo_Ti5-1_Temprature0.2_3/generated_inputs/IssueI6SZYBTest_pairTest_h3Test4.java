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

public class IssueI6SZYBTest_pairTest_h3Test4 {

    @Test
    public void pairTest_h3Test4() {
    Pair<Integer, Integer> pair = Pair.of(100, -100);
    String jsonString = "{\"key\":100,\"value\":-100}";
    Class<Pair> beanClass = Pair.class;
        String jsonStr = JSONUtil.toJsonStr(pair);
        final Pair bean = JSONUtil.toBean(jsonString, beanClass);
        Assert.assertEquals(pair, bean);
    }
}

