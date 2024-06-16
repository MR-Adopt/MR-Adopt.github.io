package cn.hutool.json;

import cn.hutool.core.lang.Pair;
import cn.hutool.core.lang.TypeReference;
import org.junit.Assert;
import org.junit.Test;


import cn.hutool.json.JSONUtil;
import cn.hutool.json.JSONUtil.*;
import java.util.List;
import java.util.Arrays;

public class IssueI7GPGXTest_toBeanTest {
    public static List<Object> inputTransformation_toBeanTest(Pair<String, Boolean> hutoolPair) {
        String jsonString = "{\"key\":\"" + hutoolPair.getKey() + "\",\"value\":" + hutoolPair.getValue() + "}";
        TypeReference<Pair<String, Boolean>> typeReference = new TypeReference<Pair<String, Boolean>>() {};
        boolean ignoreError = false;
        List<Object> transformed_inputs = Arrays.asList(jsonString, typeReference, ignoreError);
        return transformed_inputs;
    }
}