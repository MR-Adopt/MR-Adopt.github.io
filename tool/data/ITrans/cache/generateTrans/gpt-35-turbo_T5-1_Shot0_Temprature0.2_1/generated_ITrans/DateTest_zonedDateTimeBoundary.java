package com.dslplatform.json;

import com.dslplatform.json.runtime.Settings;
import org.junit.Assert;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.nio.charset.StandardCharsets;


import com.dslplatform.json.DslJson;
import com.dslplatform.json.DslJson.*;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class DateTest_zonedDateTimeBoundary {
    public static List<Object> inputTransformation_zonedDateTimeBoundary(JsonWriter jw, ZonedDateTime[] lts) throws IOException  {
        Class<ZonedDateTime[]> manifest = ZonedDateTime[].class;
        byte[] body = jw.toByteArray();
        int size = jw.size();
        List<Object> transformed_inputs = Arrays.asList(manifest, body, size);
        return transformed_inputs;
    }
}