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
    public static List<Object> inputTransformation_testNestedSet(Set<Set<Object>> set, String serializer) {
        String json2 = "";
        String typeName2 = "";

        // Transform set into json2
        for (Set<Object> nestedSet : set) {
            if (nestedSet == null) {
                json2 += "null";
            } else {
                json2 += nestedSet.toString();
            }
            json2 += "A@R#E$X";
        }

        // Remove the trailing delimiter
        if (!set.isEmpty()) {
            json2 = json2.substring(0, json2.length() - 7);
        }

        // Transform set into typeName2
        typeName2 += set.getClass().getName();
        for (Set<Object> nestedSet : set) {
            if (nestedSet != null) {
                typeName2 += "-" + nestedSet.getClass().getName();
            }
        }

        List<Object> transformed_inputs = Arrays.asList(json2, typeName2);
        return transformed_inputs;
    }
}