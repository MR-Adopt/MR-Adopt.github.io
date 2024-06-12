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

public class IssueI6SZYBTest_pairTest_GT {
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

	@Test
	public void pairTest_IT() {
		Pair<Integer,Integer> pair = Pair.of(1, 2);
		String jsonStr = JSONUtil.toJsonStr(pair);
		Assert.assertEquals("{\"key\":1,\"value\":2}", jsonStr);

		List<Object> follow_up_inputs = inputTransformation_pairTest(pair);
		String jsonString = (String) follow_up_inputs.get(0);
		Class<Pair> beanClass = (Class<Pair>) follow_up_inputs.get(1);
	Pair bean = JSONUtil.toBean(jsonString, beanClass);
		Assert.assertEquals(pair, bean);
	}

	public static List<Object> inputTransformation_pairTest(Pair<Integer,Integer> pair) {
        String jsonString = JSONUtil.toJsonStr(pair);
		Class beanClass = pair.getClass();
		List<Object> follow_up_inputs = Arrays.asList(jsonString, beanClass);
		return follow_up_inputs;
	}

}