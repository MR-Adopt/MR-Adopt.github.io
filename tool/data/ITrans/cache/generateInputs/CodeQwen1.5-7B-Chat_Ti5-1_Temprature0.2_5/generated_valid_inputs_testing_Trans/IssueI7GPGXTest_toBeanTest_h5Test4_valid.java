/*
 * Copyright (c) 2023 looly(loolly@aliyun.com)
 * Hutool is licensed under Mulan PSL v2.
 * You can use this software according to the terms and conditions of the Mulan PSL v2.
 * You may obtain a copy of Mulan PSL v2 at:
 *          http://license.coscl.org.cn/MulanPSL2
 * THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
 * EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
 * MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
 * See the Mulan PSL v2 for more details.
 */
package cn.hutool.json;

import cn.hutool.json.IssueI7GPGXTest_toBeanTest;

import cn.hutool.json.JSONUtil;
import cn.hutool.json.JSONUtil.*;
import cn.hutool.core.lang.Pair;
import cn.hutool.core.lang.TypeReference;
import java.lang.ProcessBuilder.Redirect.Type;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import org.junit.Assert;
import org.junit.Test;

public class IssueI7GPGXTest_toBeanTest_h5Test4_valid {

    @Test
    public void toBeanTest_h5Test4() {
    Pair<String, Boolean> hutoolPair = new Pair<>("", true);
		List<Object> transformed_inputs = IssueI7GPGXTest_toBeanTest.inputTransformation_toBeanTest(hutoolPair);
    String jsonString  = (String) transformed_inputs.get(0);
    TypeReference<Pair<String, Boolean>> typeReference  = (TypeReference<Pair<String, Boolean>>) transformed_inputs.get(1);
    boolean ignoreError  = (boolean) transformed_inputs.get(2);
        String a = JSONUtil.toJsonStr(hutoolPair);
        Pair<String, Boolean> pair = JSONUtil.toBean(jsonString, typeReference, ignoreError);
        Assert.assertEquals(hutoolPair, pair);
    }
}

