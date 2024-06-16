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

public class DateTest_zonedDateTimeBoundary_h4Test1 {

    private static final DslJson dslJson = new DslJson();

    @Test
    public void zonedDateTimeBoundary_h4Test1() throws IOException {
        DslJson<Object> dslJson = new DslJson<>();
    ZonedDateTime now = ZonedDateTime.parse("2021-05-20T10:30:00+02:00");
    JsonWriter jw = dslJson.newWriter(50);
    ZonedDateTime[] lts = new ZonedDateTime[2];
    lts[0] = now;
    lts[1] = now.plusHours(1);
    Class<ZonedDateTime[]> manifest = ZonedDateTime[].class;
    byte[] body = { 91, 34, 50, 48, 50, 49, 45, 48, 53, 45, 50, 48, 84, 49, 48, 58, 51, 48, 58, 48, 48, 43, 48, 50, 58, 48, 48, 34, 44, 34, 50, 48, 50, 49, 45, 48, 53, 45, 50, 48, 84, 49, 49, 58, 51, 48, 58, 48, 48, 43, 48, 51, 58, 48, 48, 34, 93, 0, 0 };
    int size = 77;
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

