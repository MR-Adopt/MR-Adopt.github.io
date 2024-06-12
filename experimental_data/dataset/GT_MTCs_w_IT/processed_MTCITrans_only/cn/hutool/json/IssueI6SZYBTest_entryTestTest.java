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

public class IssueI6SZYBTest_entryTestTest {
// 	@Test
// 	public void entryTest_h() {
// 		Map.Entry<String,Integer> pair = new AbstractMap.SimpleEntry<>("1", 2);
// 		String jsonStr = JSONUtil.toJsonStr(pair);
// 		Assert.assertEquals("{\"1\":2}", jsonStr);
// 
// 		String jsonString = "{\"1\":2}";
// 		Class beanClass = AbstractMap.SimpleEntry.class;
// 	Map.Entry bean = (Entry) JSONUtil.toBean(jsonString,beanClass);
// 		Assert.assertEquals(pair, bean);
// 	}
// 
	@Test
	public void entryTest_IT() {
		Map.Entry<String,Integer> pair = new AbstractMap.SimpleEntry<>("1", 2);
		String jsonStr = JSONUtil.toJsonStr(pair);
		Assert.assertEquals("{\"1\":2}", jsonStr);

		List<Object> follow_up_inputs = IssueI6SZYBTest_entryTest.inputTransformation_entryTest(pair);
		String jsonString = (String) follow_up_inputs.get(0);
		Class beanClass = (Class) follow_up_inputs.get(1);
	Map.Entry bean = (Entry) JSONUtil.toBean(jsonString, beanClass);
		Assert.assertEquals(pair, bean);
	}

// 	public static List<Object> inputTransformation_entryTest(Map.Entry<String,Integer> pair) {
//         String jsonString = JSONUtil.toJsonStr(pair);
// 		Class beanClass = pair.getClass();
// 		List<Object> follow_up_inputs = Arrays.asList(jsonString, beanClass);
// 		return follow_up_inputs;
// 	}
}