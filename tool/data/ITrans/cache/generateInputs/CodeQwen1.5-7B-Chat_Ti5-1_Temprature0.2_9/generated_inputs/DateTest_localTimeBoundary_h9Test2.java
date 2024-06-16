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

public class DateTest_localTimeBoundary_h9Test2 {

    private static final DslJson dslJson = new DslJson();

    @Test
    public void localTimeBoundary_h9Test2() throws IOException {
        DslJson<Object> dslJson = new DslJson<>();
    LocalTime now = LocalTime.parse("12:13:14.123456789");
    JsonWriter jw = dslJson.newWriter(20);
    LocalTime[] lts = new LocalTime[2];
    Arrays.fill(lts, now);
    lts[0] = LocalTime.parse("00:00:00.000000000");
    lts[1] = LocalTime.parse("23:59:59.999999999");
    byte[] body = { 91, 34, 48, 48, 58, 48, 48, 58, 48, 48, 46, 48, 48, 48, 48, 48, 48, 48, 48, 48, 34, 44, 34, 50, 51, 58, 51, 57, 58, 51, 57, 46, 51, 57, 57, 57, 57, 57, 57, 57, 57, 34, 93, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    int size = 42;
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

