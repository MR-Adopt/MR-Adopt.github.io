package io.arex.inst.runtime.serializer;

import io.arex.inst.runtime.serializer.SerializerTest_testNestedList;

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

class SerializerTest_testNestedList_h6Test3_valid {

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
    void testNestedList_h6Test3() {
List<List<Object>> list = new ArrayList<>();
list.add(null);
list.add(new ArrayList<>());
list.add(nestedList1);
list.add(nestedList2);
String serializer = "jackson";
		List<Object> transformed_inputs = SerializerTest_testNestedList.inputTransformation_testNestedList(list, serializer);
String json2  = (String) transformed_inputs.get(0);
String typeName2  = (String) transformed_inputs.get(1);
        List<Object> nestedList1 = new ArrayList<>();
        nestedList1.add("nestList1-1");
        nestedList1.add("nestList1-2");
        List<Object> nestedList2 = new LinkedList<>();
        nestedList2.add("nestList2-1");
        nestedList2.add("nestList2-2");
        String json = Serializer.serialize(list, serializer);
        List<List<Object>> actualResult = Serializer.deserialize(json2, typeName2);
        assertEquals(list, actualResult);
        // empty list
        String emptyListTypeName = TypeUtil.getName(new ArrayList<>());
        List<Object> emptyList = Serializer.deserialize("[]", emptyListTypeName);
    }
}

