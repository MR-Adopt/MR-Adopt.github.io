package io.arex.inst.runtime.serializer;

import io.arex.inst.runtime.serializer.SerializerTest_testNestedSet;

import io.arex.inst.runtime.serializer.Serializer;
import io.arex.inst.runtime.serializer.Serializer.*;
import static org.junit.jupiter.api.Assertions.*;
import io.arex.agent.bootstrap.constants.ConfigConstants;
import io.arex.inst.runtime.config.Config;
import io.arex.inst.runtime.config.ConfigBuilder;
import io.arex.inst.runtime.listener.EventProcessorTest.TestJacksonSerializable;
import io.arex.inst.runtime.listener.EventProcessorTest.TestGsonSerializer;
import io.arex.inst.runtime.util.TypeUtil;
import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

class SerializerTest_testNestedSet_h1Test4_valid {

    @BeforeAll
    static void setUp() {
        List<StringSerializable> list = new ArrayList<>(2);
        list.add(new TestJacksonSerializable());
        list.add(new TestGsonSerializer());
        Serializer.builder(list).build();
    }

    @AfterAll
    static void tearDown() {
    }

    @Test
    void testNestedSet_h1Test4() {
Set<Set<Object>> set = new HashSet<>();
set.add(null);
set.add(new HashSet<>());
set.add(null);
set.add(new HashSet<>());
set.add(nestedSet1);
set.add(nestedSet2);
String serializer = "jackson";
		List<Object> transformed_inputs = SerializerTest_testNestedSet.inputTransformation_testNestedSet(set, serializer);
String json2  = (String) transformed_inputs.get(0);
String typeName2  = (String) transformed_inputs.get(1);
        Set<Object> nestedSet1 = new HashSet<>();
        nestedSet1.add("nestedSet1-1");
        nestedSet1.add("nestedSet1-2");
        Set<Object> nestedSet2 = new TreeSet<>();
        nestedSet2.add("nestedSet2-1");
        nestedSet2.add("nestedSet2-2");
        String json = Serializer.serialize(set, serializer);
        Set<Set<Object>> actualResult = Serializer.deserialize(json2, typeName2);
        assertEquals(set, actualResult);
    }
}

