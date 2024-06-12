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

public class DateTest_zonedDateTimeBoundary_GT {

	private static final DslJson dslJson = new DslJson();

	@Test
	public void zonedDateTimeBoundary_h() throws IOException {
		DslJson<Object> dslJson = new DslJson<>();
		ZonedDateTime now = ZonedDateTime.parse("2020-01-12T12:13:14.123456789-03:30");
		JsonWriter jw = dslJson.newWriter(34);
		ZonedDateTime[] lts = new ZonedDateTime[3];
		Arrays.fill(lts, now);
		dslJson.serialize(jw, lts);
		Class<ZonedDateTime[]> manifest = ZonedDateTime[].class;
		byte[] body = {91,34,50,48,50,48,45,48,49,45,49,50,84,49,50,58,49,51,58,49,52,46,49,50,51,52,53,54,55,56,57,45,48,51,58,51,48,34,44,34,50,48,50,48,45,48,49,45,49,50,84,49,50,58,49,51,58,49,52,46,49,50,51,52,53,54,55,56,57,45,48,51,58,51,48,34,44,34,50,48,50,48,45,48,49,45,49,50,84,49,50,58,49,51,58,49,52,46,49,50,51,52,53,54,55,56,57,45,48,51,58,51,48,34,93,0,0};
		int size = 115;
		ZonedDateTime[] values = dslJson.deserialize(manifest, body, size);
		Assert.assertArrayEquals(lts, values);
	}

	@Test
	public void zonedDateTimeBoundary_IT() throws IOException {
		DslJson<Object> dslJson = new DslJson<>();
		ZonedDateTime now = ZonedDateTime.parse("2020-01-12T12:13:14.123456789-03:30");
		JsonWriter jw = dslJson.newWriter(34);
		ZonedDateTime[] lts = new ZonedDateTime[3];
		Arrays.fill(lts, now);
		dslJson.serialize(jw, lts);
		List<Object> follow_up_inputs = inputTransformation_zonedDateTimeBoundary(jw, lts);
		Class<ZonedDateTime[]> manifest = (Class<ZonedDateTime[]>) follow_up_inputs.get(0);
		byte[] body = (byte[]) follow_up_inputs.get(1);
		int size = (int) follow_up_inputs.get(2);
		ZonedDateTime[] values = dslJson.deserialize(manifest, body, size);
		Assert.assertArrayEquals(lts, values);
	}

	public static List<Object> inputTransformation_zonedDateTimeBoundary(JsonWriter jw, ZonedDateTime[] lts) throws IOException {
		DslJson<Object> dslJson = new DslJson<>();
		dslJson.serialize(jw, lts);

        Class manifest = lts.getClass();
		byte[] body = jw.getByteBuffer();
		int size = jw.size();

        List<Object> follow_up_inputs = Arrays.asList(manifest, body, size);
		return follow_up_inputs;
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