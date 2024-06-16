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

public class SerializerTest_testNestedSet {
    public static List<Object> inputTransformation_testNestedSet(Set<Set<Object>> set, String serializer)  {
        String json2 = constructJson(set);
        String typeName2 = constructTypeName(set);
        List<Object> transformed_inputs = Arrays.asList(json2, typeName2);
        return transformed_inputs;
    }
    
    private static String constructJson(Set<Set<Object>> set) {
        StringBuilder jsonBuilder = new StringBuilder();
        for (Set<Object> innerSet : set) {
            if (innerSet == null) {
                jsonBuilder.append("null");
            } else {
                jsonBuilder.append("A@R#E$X[");
                for (Object element : innerSet) {
                    jsonBuilder.append("\"").append(element.toString()).append("\",");
                }
                if (!innerSet.isEmpty()) {
                    jsonBuilder.deleteCharAt(jsonBuilder.length() - 1);
                }
                jsonBuilder.append("]");
            }
        }
        return jsonBuilder.toString();
    }
    
    private static String constructTypeName(Set<Set<Object>> set) {
        StringBuilder typeNameBuilder = new StringBuilder();
        typeNameBuilder.append("java.util.HashSet");
        for (Set<Object> innerSet : set) {
            if (innerSet != null) {
                typeNameBuilder.append("-").append(innerSet.getClass().getName());
            }
        }
        return typeNameBuilder.toString();
    }
}