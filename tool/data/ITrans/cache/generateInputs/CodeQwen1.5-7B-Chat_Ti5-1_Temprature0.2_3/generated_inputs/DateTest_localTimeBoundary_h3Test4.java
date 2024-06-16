package com.dslplatform.json;

import com.dslplatform.json.DslJson;
import com.dslplatform.json.DslJson.*;
import com.dslplatform.json.runtime.Settings;
import org.junit.Assert;
import org.junit.Test;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.time.*;
import java.util.Arrays;
import java.util.List;

public class DateTest_localTimeBoundary_h3Test4 {

    private static final DslJson dslJson = new DslJson();

    @Test
    public void localTimeBoundary_h3Test4() throws IOException {
        DslJson<Object> dslJson = new DslJson<>();
    LocalTime now = LocalTime.parse("12:13:14.123456789");
    JsonWriter jw = dslJson.newWriter(20);
    LocalTime[] lts = new LocalTime[3];
    Arrays.fill(lts, now);
    byte[] body = { 91, 34, 49, 50, 58, 49, 51, 58, 49, 52, 46, 49, 50, 51, 52, 53, 54, 55, 56, 57, 34, 44, 34, 49, 50, 58, 49, 51, 58, 49, 52, 46, 49, 50, 51, 52, 53, 54, 55, 56, 57, 34, 44, 34, 49, 50, 58, 49, 51, 58, 49, 52, 46, 49, 50, 51, 52, 53, 54, 55, 56, 57, 34, 93, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    int size = 86;
        dslJson.serialize(jw, lts);
        Class<LocalTime[]> manifest = LocalTime[].class;
        LocalTime[] values = dslJson.deserialize(manifest, body, size);
        Assert.assertArrayEquals(lts, values);
    }

    public static class NineODT {

        public OffsetDateTime at;
    }

    public static class NineOT {

        public OffsetTime at;
    }

    public static class ModelLDT {

        public LocalDateTime now;

        public LocalDateTime date;
    }

    public static class ModelODT {

        public OffsetDateTime now;

        public OffsetDateTime date;
    }

    public static class SqlDate {

        public java.util.Date date;
    }
}

