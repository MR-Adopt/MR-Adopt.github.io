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
        
        if (serializeSkipInfo.getFieldName().equals(serializeSkipInfo.getFullClassName())) {
            // Case 1: Same fieldName and fullClassName values
            serializeSkipInfo2 = serializeSkipInfo;
        } else {
            // Case 2: Different fieldName and fullClassName values
            serializeSkipInfo2.setFieldName(serializeSkipInfo.getFieldName());
            serializeSkipInfo2.setFullClassName(serializeSkipInfo.getFullClassName());
        }
        
        if (serializeSkipInfo.getFieldName().isEmpty()) {
            // Case 3: Empty fieldName value
            serializeSkipInfo2.setFieldName("");
        }
        
        if (serializeSkipInfo.getFullClassName().isEmpty()) {
            // Case 4: Empty fullClassName value
            serializeSkipInfo2.setFullClassName("");
        }
        
        return serializeSkipInfo2;
    }
}