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
        SerializeSkipInfo serializeSkipInfo2 = new SerializeSkipInfo();
        if (serializeSkipInfo.getFieldName().equals(serializeSkipInfo.getFullClassName())) {
            serializeSkipInfo2.setFieldName(serializeSkipInfo.getFieldName());
            serializeSkipInfo2.setFullClassName(serializeSkipInfo.getFullClassName());
        } else if (serializeSkipInfo.getFieldName().isEmpty() || serializeSkipInfo.getFieldName() == null) {
            serializeSkipInfo2.setFieldName("");
            serializeSkipInfo2.setFullClassName(serializeSkipInfo.getFullClassName());
        } else if (serializeSkipInfo.getFullClassName().isEmpty() || serializeSkipInfo.getFullClassName() == null) {
            serializeSkipInfo2.setFieldName(serializeSkipInfo.getFieldName());
            serializeSkipInfo2.setFullClassName("");
        } else {
            serializeSkipInfo2.setFieldName(serializeSkipInfo.getFieldName());
            serializeSkipInfo2.setFullClassName(serializeSkipInfo.getFullClassName());
        }
        return serializeSkipInfo2;
    }
}