package io.arex.inst.runtime.model;

import io.arex.inst.runtime.model.SerializeSkipInfo;
import io.arex.inst.runtime.model.SerializeSkipInfo.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

class SerializeSkipInfoTest_testToString_h4Test4 {

    static SerializeSkipInfo serializeSkipInfo;

    static SerializeSkipInfo serializeSkipInfo2;

    @BeforeAll
    static void setUp() {
        serializeSkipInfo = new SerializeSkipInfo();
        serializeSkipInfo.setFieldName("testFieldName1,testFieldName2");
        serializeSkipInfo.setFullClassName("testFullClassName");
        serializeSkipInfo2 = new SerializeSkipInfo();
        serializeSkipInfo2.setFieldName("testFieldName1,testFieldName2");
        serializeSkipInfo2.setFullClassName("testFullClassName");
    }

    @AfterAll
    static void tearDown() {
        serializeSkipInfo = null;
        serializeSkipInfo2 = null;
    }

    @Test
    void testToString_h4Test4() {
    SerializeSkipInfo serializeSkipInfo = new SerializeSkipInfo();
    serializeSkipInfo.setFieldName("testFieldName1,testFieldName2");
    serializeSkipInfo.setFullClassName("testFullClassName,testFullClassName2");
    SerializeSkipInfo serializeSkipInfo2 = new SerializeSkipInfo();
    serializeSkipInfo2.setFieldName("testFieldName1,testFieldName2");
    serializeSkipInfo2.setFullClassName("testFullClassName,testFullClassName2");
        assertEquals(serializeSkipInfo2.toString(), serializeSkipInfo.toString());
    }
}

