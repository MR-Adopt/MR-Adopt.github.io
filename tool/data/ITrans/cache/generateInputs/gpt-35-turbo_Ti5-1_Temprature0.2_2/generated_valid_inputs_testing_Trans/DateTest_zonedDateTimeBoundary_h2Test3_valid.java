package com.dslplatform.json;

import com.dslplatform.json.DateTest_zonedDateTimeBoundary;

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

public class DateTest_zonedDateTimeBoundary_h2Test3_valid {

    private static final DslJson dslJson = new DslJson();

    @Test
    public void zonedDateTimeBoundary_h2Test3() throws IOException {
        DslJson<Object> dslJson = new DslJson<>();
    ZonedDateTime now = ZonedDateTime.parse("2023-04-25T08:45:00.000000000-07:00");
    JsonWriter jw = dslJson.newWriter(34);
    ZonedDateTime[] lts = new ZonedDateTime[4];
    Arrays.fill(lts, now);
		List<Object> transformed_inputs = DateTest_zonedDateTimeBoundary.inputTransformation_zonedDateTimeBoundary(jw, lts);
    Class<ZonedDateTime[]> manifest  = (Class<ZonedDateTime[]>) transformed_inputs.get(0);
    byte[] body  = (byte[]) transformed_inputs.get(1);
    int size  = (int) transformed_inputs.get(2);
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
