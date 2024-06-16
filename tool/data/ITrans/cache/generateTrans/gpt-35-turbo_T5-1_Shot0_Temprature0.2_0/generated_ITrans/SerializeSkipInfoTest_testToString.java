package io.arex.inst.runtime.model;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;


import io.arex.inst.runtime.model.SerializeSkipInfo;
import io.arex.inst.runtime.model.SerializeSkipInfo.*;
import java.util.List;
import java.util.Arrays;

public class SerializeSkipInfoTest_testToString {
    public static SerializeSkipInfo inputTransformation_testToString(SerializeSkipInfo serializeSkipInfo) {
        if (serializeSkipInfo.getFieldName().equals(serializeSkipInfo2.getFieldName()) &&
                serializeSkipInfo.getFullClassName().equals(serializeSkipInfo2.getFullClassName())) {
            return serializeSkipInfo2;
        } else if (!serializeSkipInfo.getFieldName().equals(serializeSkipInfo2.getFieldName()) ||
                !serializeSkipInfo.getFullClassName().equals(serializeSkipInfo2.getFullClassName())) {
            SerializeSkipInfo serializeSkipInfo2 = new SerializeSkipInfo();
            serializeSkipInfo2.setFieldName(serializeSkipInfo2.getFieldName());
            serializeSkipInfo2.setFullClassName(serializeSkipInfo2.getFullClassName());
            return serializeSkipInfo2;
        } else {
            SerializeSkipInfo serializeSkipInfo2 = new SerializeSkipInfo();
            serializeSkipInfo2.setFieldName("");
            serializeSkipInfo2.setFullClassName("");
            return serializeSkipInfo2;
        }
    }
}