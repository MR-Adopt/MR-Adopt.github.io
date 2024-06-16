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
        String json2 = serializeSet(set);
        String typeName2 = generateTypeName(set);
        List<Object> transformed_inputs = Arrays.asList(json2, typeName2);
        return transformed_inputs;
    }
    
    private static String serializeSet(Set<Set<Object>> set) {
        StringBuilder sb = new StringBuilder();
        for (Set<Object> innerSet : set) {
            if (innerSet == null) {
                sb.append("null");
            } else {
                sb.append(innerSet.toString());
            }
            sb.append("A@R#E$X");
        }
        return sb.toString();
    }
    
    private static String generateTypeName(Set<Set<Object>> set) {
        StringBuilder sb = new StringBuilder();
        sb.append("java.util.HashSet");
        for (Object innerObject : set) {
            if (innerObject instanceof Set) {
                sb.append("-java.util.HashSet");
            } else {
                sb.append(",").append(innerObject.getClass().getName());
            }
        }
        return sb.toString();
    }
}