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
        String json2 = Serializer.serialize(list, serializer);
        String typeName2 = "java.util.ArrayList-java.util.ArrayList";
        List<Object> transformed_inputs = Arrays.asList(json2, typeName2);
        return transformed_inputs;
    }
}