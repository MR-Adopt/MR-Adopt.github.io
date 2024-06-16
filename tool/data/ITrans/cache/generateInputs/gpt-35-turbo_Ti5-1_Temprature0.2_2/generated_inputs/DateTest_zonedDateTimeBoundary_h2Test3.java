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

public class DateTest_zonedDateTimeBoundary_h2Test3 {

    private static final DslJson dslJson = new DslJson();

    @Test
    public void zonedDateTimeBoundary_h2Test3() throws IOException {
        DslJson<Object> dslJson = new DslJson<>();
    ZonedDateTime now = ZonedDateTime.parse("2023-04-25T08:45:00.000000000-07:00");
    JsonWriter jw = dslJson.newWriter(34);
    ZonedDateTime[] lts = new ZonedDateTime[4];
    Arrays.fill(lts, now);
    Class<ZonedDateTime[]> manifest = ZonedDateTime[].class;
    byte[] body = { 91, 34, 50, 48, 50, 51, 45, 48, 52, 45, 50, 53, 84, 48, 56, 58, 52, 53, 58, 48, 48, 46, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 45, 48, 55, 58, 48, 48, 34, 44, 34, 50, 48, 50, 51, 45, 48, 52, 45, 50, 53, 84, 48, 56, 58, 52, 53, 58, 48, 48, 46, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 45, 48, 55, 58, 48, 48, 34, 44, 34, 50, 48, 50, 51, 45, 48, 52, 45, 50, 53, 84, 48, 56, 58, 52, 53, 58, 48, 48, 46, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 45, 48, 55, 58, 48, 48, 34, 44, 34, 50, 48, 50, 51, 45, 48, 52, 45, 50, 53, 84, 48, 56, 58, 52, 53, 58, 48, 48, 46, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 45, 48, 55, 58, 48, 48, 34, 93, 0, 0 };
    int size = 259;
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

