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

public class DateTest_zonedDateTimeBoundary_h2Test1 {

    private static final DslJson dslJson = new DslJson();

    @Test
    public void zonedDateTimeBoundary_h2Test1() throws IOException {
        DslJson<Object> dslJson = new DslJson<>();
    ZonedDateTime now = ZonedDateTime.parse("2021-02-15T10:20:30.987654321+05:00");
    JsonWriter jw = dslJson.newWriter(34);
    ZonedDateTime[] lts = new ZonedDateTime[2];
    Arrays.fill(lts, now);
    Class<ZonedDateTime[]> manifest = ZonedDateTime[].class;
    byte[] body = { 91, 34, 50, 48, 50, 49, 45, 48, 50, 45, 49, 53, 84, 49, 48, 58, 50, 48, 58, 51, 48, 46, 57, 56, 55, 54, 53, 52, 51, 50, 49, 43, 48, 53, 58, 48, 48, 34, 44, 34, 50, 48, 50, 49, 45, 48, 50, 45, 49, 53, 84, 49, 48, 58, 50, 48, 58, 51, 48, 46, 57, 56, 55, 54, 53, 52, 51, 50, 49, 43, 48, 53, 58, 48, 48, 34, 93, 0, 0 };
    int size = 115;
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

