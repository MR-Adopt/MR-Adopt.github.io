package io.arex.inst.runtime.serializer;

import io.arex.agent.bootstrap.constants.ConfigConstants;
import io.arex.inst.runtime.config.Config;
import io.arex.inst.runtime.config.ConfigBuilder;
import io.arex.inst.runtime.listener.EventProcessorTest.TestJacksonSerializable;
import io.arex.inst.runtime.listener.EventProcessorTest.TestGsonSerializer;
import io.arex.inst.runtime.util.TypeUtil;
import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;
import java.util.TreeSet;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;


import io.arex.inst.runtime.serializer.Serializer;
import io.arex.inst.runtime.serializer.Serializer.*;
import java.util.List;
import java.util.Arrays;

public class SerializerTest_testNestedList {
    public static List<Object> inputTransformation_testNestedList(List<List<Object>> list, String serializer) {
        StringBuilder jsonBuilder = new StringBuilder();
        StringBuilder typeNameBuilder = new StringBuilder();

        for (List<Object> innerList : list) {
            if (innerList == null) {
                jsonBuilder.append("null");
            } else {
                jsonBuilder.append(innerList.toString());
            }
            jsonBuilder.append("A@R#E$X");
            
            typeNameBuilder.append(innerList.getClass().getName());
            typeNameBuilder.append("-");
        }

        String json2 = jsonBuilder.toString();
        String typeName2 = typeNameBuilder.toString();

        // Remove the trailing delimiter from the strings
        json2 = json2.substring(0, json2.length() - "A@R#E$X".length());
        typeName2 = typeName2.substring(0, typeName2.length() - 1);

        List<Object> transformedInputs = Arrays.asList(json2, typeName2);
        return transformedInputs;
    }
}