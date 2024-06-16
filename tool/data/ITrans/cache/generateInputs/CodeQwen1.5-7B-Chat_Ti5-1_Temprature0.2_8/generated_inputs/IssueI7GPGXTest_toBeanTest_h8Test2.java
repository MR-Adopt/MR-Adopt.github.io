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

public class IssueI7GPGXTest_toBeanTest_h8Test2 {

    @Test
    public void toBeanTest_h8Test2() {
    Pair<String, Boolean> hutoolPair = new Pair<>("test3", true);
    String jsonString = "{\"key\":\"test3\",\"value\":true}";
    TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {
    };
    boolean ignoreError = false;
        String a = JSONUtil.toJsonStr(hutoolPair);
        Pair<String, Boolean> pair = JSONUtil.toBean(jsonString, typeReference, ignoreError);
        Assert.assertEquals(hutoolPair, pair);
    }
}

