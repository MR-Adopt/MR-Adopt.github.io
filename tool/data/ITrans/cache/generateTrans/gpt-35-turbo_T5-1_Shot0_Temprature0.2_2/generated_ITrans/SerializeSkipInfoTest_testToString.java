package io.arex.inst.runtime.model;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;


import io.arex.inst.runtime.model.SerializeSkipInfo;
import io.arex.inst.runtime.model.SerializeSkipInfo.*;
import java.util.List;
import java.util.Arrays;

public class SerializeSkipInfoTest_testToString {
    public static SerializeSkipInfo inputTransformation_testToString(SerializeSkipInfo serializeSkipInfo)  {
        SerializeSkipInfo serializeSkipInfo2 = new SerializeSkipInfo();
        serializeSkipInfo2.setFieldName(concatenateValues(serializeSkipInfo.getFieldName()));
        serializeSkipInfo2.setFullClassName(concatenateValues(serializeSkipInfo.getFullClassName()));
        return serializeSkipInfo2;
    }
    
    private static String concatenateValues(String value) {
        if (value == null) {
            return null;
        }
        String[] values = value.split(",");
        StringBuilder sb = new StringBuilder();
        for (String val : values) {
            if (!val.isEmpty()) {
                sb.append(val).append(",");
            }
        }
        if (sb.length() > 0) {
            sb.deleteCharAt(sb.length() - 1);
        }
        return sb.toString();
    }
}