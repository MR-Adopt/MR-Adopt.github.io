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

public class IssueI6SZYBTest_pairTest_hTest {
	@Test
	public void pairTest_h() {
		Pair<Integer,Integer> pair = Pair.of(1, 2);
		String jsonStr = JSONUtil.toJsonStr(pair);
		Assert.assertEquals("{\"key\":1,\"value\":2}", jsonStr);
	
		String jsonString = "{\"key\":1,\"value\":2}";
		Class<Pair> beanClass = Pair.class;
	Pair bean = JSONUtil.toBean(jsonString, beanClass);
		Assert.assertEquals(pair, bean);
	}

}