package com.dslplatform.json;

import com.dslplatform.json.runtime.Settings;
import org.junit.Assert;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;


import com.dslplatform.json.DslJson;
import com.dslplatform.json.DslJson.*;
import java.util.List;
import java.util.Arrays;

public class DateTest_localTimeBoundary {
    public static List<Object> inputTransformation_localTimeBoundary(JsonWriter jw, LocalTime[] lts) {
        Class<LocalTime[]> manifest = LocalTime[].class;
        byte[] body = jw.toByteArray();
        int size = body.length;
        List<Object> transformed_inputs = Arrays.asList(manifest, body, size);
        return transformed_inputs;
    }
}