package io.arex.inst.runtime.model;

import io.arex.inst.runtime.model.SerializeSkipInfoTest_testHashCode;

import io.arex.inst.runtime.model.SerializeSkipInfo;
import io.arex.inst.runtime.model.SerializeSkipInfo.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

class SerializeSkipInfoTest_testHashCode_h4Test3_valid {

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
    void testHashCode_h4Test3() {
    SerializeSkipInfo serializeSkipInfo = new SerializeSkipInfo();
    serializeSkipInfo.setFieldName("testFieldName1,testFieldName2");
    serializeSkipInfo.setFullClassName("testFullClassName".repeat(1000));
    SerializeSkipInfo serializeSkipInfo2  = SerializeSkipInfoTest_testHashCode.inputTransformation_testHashCode(serializeSkipInfo);
    serializeSkipInfo2.setFieldName("testFieldName1,testFieldName2");
    serializeSkipInfo2.setFullClassName("testFullClassName".repeat(1000));
        assertEquals(serializeSkipInfo2.hashCode(), serializeSkipInfo.hashCode());
    }
}

