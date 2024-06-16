package io.arex.inst.runtime.model;

import io.arex.inst.runtime.model.SerializeSkipInfo;
import io.arex.inst.runtime.model.SerializeSkipInfo.*;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

class SerializeSkipInfoTest_testToString_GTTest {
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

//     @Test
//     void testToString_h() {
//         SerializeSkipInfo serializeSkipInfo = new SerializeSkipInfo();
//         serializeSkipInfo.setFieldName("testFieldName1,testFieldName2");
//         serializeSkipInfo.setFullClassName("testFullClassName");
// 
//         SerializeSkipInfo serializeSkipInfo2 = new SerializeSkipInfo();
//         serializeSkipInfo2.setFieldName("testFieldName1,testFieldName2");
//         serializeSkipInfo2.setFullClassName("testFullClassName");
// 
//         assertEquals(serializeSkipInfo2.toString(), serializeSkipInfo.toString());
//     }
// 
// 
// //     public static SerializeSkipInfo inputTransformation_testToString(SerializeSkipInfo serializeSkipInfo) {
// //         SerializeSkipInfo serializeSkipInfo2 = new SerializeSkipInfo();
// //         String fieldName = serializeSkipInfo.getFieldName();
// //         String fullClassName = serializeSkipInfo.getFullClassName();
// // 
// //         serializeSkipInfo2.setFieldName(fieldName);
// //         serializeSkipInfo2.setFullClassName(fullClassName);
// // 
// //         return serializeSkipInfo2;
// //     }
// // 
// // 
    @Test
    void testToString_IT() {
        SerializeSkipInfo serializeSkipInfo = new SerializeSkipInfo();
        serializeSkipInfo.setFieldName("testFieldName1,testFieldName2");
        serializeSkipInfo.setFullClassName("testFullClassName");

        SerializeSkipInfo serializeSkipInfo2 = SerializeSkipInfoTest_testToString_GT.inputTransformation_testToString(serializeSkipInfo);
        assertEquals(serializeSkipInfo2.toString(), serializeSkipInfo.toString());
    }
}