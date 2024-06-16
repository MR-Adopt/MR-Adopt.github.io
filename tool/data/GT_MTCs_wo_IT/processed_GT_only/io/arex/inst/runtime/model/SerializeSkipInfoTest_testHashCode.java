package io.arex.inst.runtime.model;

import io.arex.inst.runtime.model.SerializeSkipInfo;
import io.arex.inst.runtime.model.SerializeSkipInfo.*;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

class SerializeSkipInfoTest_testHashCode {
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
    void testHashCode_h() {
        SerializeSkipInfo serializeSkipInfo = new SerializeSkipInfo();
        serializeSkipInfo.setFieldName("testFieldName1,testFieldName2");
        serializeSkipInfo.setFullClassName("testFullClassName");

        SerializeSkipInfo serializeSkipInfo2 = new SerializeSkipInfo();
        serializeSkipInfo2.setFieldName("testFieldName1,testFieldName2");
        serializeSkipInfo2.setFullClassName("testFullClassName");

        assertEquals(serializeSkipInfo2.hashCode(), serializeSkipInfo.hashCode());
    }


    public static SerializeSkipInfo inputTransformation_testHashCode(SerializeSkipInfo serializeSkipInfo) {
        SerializeSkipInfo serializeSkipInfo2 = new SerializeSkipInfo();
        String fieldName = serializeSkipInfo.getFieldName();
        String fullClassName = serializeSkipInfo.getFullClassName();

        serializeSkipInfo2.setFieldName(fieldName);
        serializeSkipInfo2.setFullClassName(fullClassName);

        return serializeSkipInfo2;
    }


    @Test
    void testHashCode_IT() {
        SerializeSkipInfo serializeSkipInfo = new SerializeSkipInfo();
        serializeSkipInfo.setFieldName("testFieldName1,testFieldName2");
        serializeSkipInfo.setFullClassName("testFullClassName");

        SerializeSkipInfo serializeSkipInfo2 = inputTransformation_testHashCode(serializeSkipInfo);
        assertEquals(serializeSkipInfo2.hashCode(), serializeSkipInfo.hashCode());
    }


}