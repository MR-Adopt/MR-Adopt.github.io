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
import java.util.List;
import java.util.Arrays;

import java.util.*;

public class SerializerTest_testNestedSet {
    public static List<Object> inputTransformation_testNestedSet(Set<Set<Object>> set, String serializer) {
        String json2 = serialize(set, serializer);
        String typeName2 = getTypeName(set);
        List<Object> transformed_inputs = Arrays.asList(json2, typeName2);
        return transformed_inputs;
    }
    
    private static String serialize(Set<Set<Object>> set, String serializer) {
        StringBuilder jsonBuilder = new StringBuilder();
        jsonBuilder.append("nullA@R#E$X[");
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
            jsonBuilder.append(",");
        }
        if (!set.isEmpty()) {
            jsonBuilder.deleteCharAt(jsonBuilder.length() - 1);
        }
        jsonBuilder.append("]");
        return jsonBuilder.toString();
    }
    
    private static String getTypeName(Set<Set<Object>> set) {
        StringBuilder typeNameBuilder = new StringBuilder();
        typeNameBuilder.append("java.util.HashSet");
        for (Set<Object> innerSet : set) {
            typeNameBuilder.append("-java.util.HashSet");
            for (Object element : innerSet) {
                typeNameBuilder.append(",").append(element.getClass().getName());
            }
        }
        return typeNameBuilder.toString();
    }
}