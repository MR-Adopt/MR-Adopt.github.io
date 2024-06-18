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

public class DateTest_zonedDateTimeBoundary_h4Test3 {

    private static final DslJson dslJson = new DslJson();

    @Test
    public void zonedDateTimeBoundary_h4Test3() throws IOException {
        DslJson<Object> dslJson = new DslJson<>();
    ZonedDateTime now = ZonedDateTime.parse("2022-12-31T23:59:59+00:00");
    JsonWriter jw = dslJson.newWriter(100);
    ZonedDateTime[] lts = new ZonedDateTime[4];
    Arrays.fill(lts, now);
    Class<ZonedDateTime[]> manifest = ZonedDateTime[].class;
    byte[] body = { 91, 34, 50, 48, 50, 50, 45, 49, 50, 45, 51, 49, 84, 50, 51, 58, 53, 57, 58, 53, 57, 43, 48, 48, 58, 48, 48, 34, 44, 34, 50, 48, 50, 50, 45, 49, 50, 45, 51, 49, 84, 50, 51, 58, 53, 57, 58, 53, 57, 43, 48, 48, 58, 48, 48, 34, 44, 34, 50, 48, 50, 50, 45, 49, 50, 45, 51, 49, 84, 50, 51, 58, 53, 57, 58, 53, 57, 43, 48, 48, 58, 48, 48, 34, 44, 34, 50, 48, 50, 50, 45, 49, 50, 45, 51, 49, 84, 50, 51, 58, 53, 57, 58, 53, 57, 43, 48, 48, 58, 48, 48, 34, 93, 0, 0 };
    int size = 161;
        dslJson.serialize(jw, lts);
        ZonedDateTime[] values = dslJson.deserialize(manifest, body, size);
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
