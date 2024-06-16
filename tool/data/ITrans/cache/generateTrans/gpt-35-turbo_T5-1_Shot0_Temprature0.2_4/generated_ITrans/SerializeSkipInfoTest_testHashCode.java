package io.arex.inst.runtime.model;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;


import io.arex.inst.runtime.model.SerializeSkipInfo;
import io.arex.inst.runtime.model.SerializeSkipInfo.*;
import java.util.List;
import java.util.Arrays;

public class SerializeSkipInfoTest_testHashCode {
    public static SerializeSkipInfo inputTransformation_testHashCode(SerializeSkipInfo serializeSkipInfo)  {
        SerializeSkipInfo serializeSkipInfo2 = new SerializeSkipInfo();
        serializeSkipInfo2.setFieldName(serializeSkipInfo.getFieldName());
        serializeSkipInfo2.setFullClassName(serializeSkipInfo.getFullClassName());
        return serializeSkipInfo2;
    }
}