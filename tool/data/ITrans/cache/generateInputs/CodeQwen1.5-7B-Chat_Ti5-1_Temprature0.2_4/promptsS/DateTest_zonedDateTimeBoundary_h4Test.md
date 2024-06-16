# ORIGINAL TEST CASE
```java
@Test
public void zonedDateTimeBoundary() throws IOException {
    DslJson<Object> dslJson = new DslJson<>();
    ZonedDateTime now = ZonedDateTime.parse("2020-01-12T12:13:14.123456789-03:30");
    JsonWriter jw = dslJson.newWriter(34);
    ZonedDateTime[] lts = new ZonedDateTime[3];
    Arrays.fill(lts, now);
    dslJson.serialize(jw, lts);
    Class<ZonedDateTime[]> manifest = ZonedDateTime[].class;
    byte[] body = { 91, 34, 50, 48, 50, 48, 45, 48, 49, 45, 49, 50, 84, 49, 50, 58, 49, 51, 58, 49, 52, 46, 49, 50, 51, 52, 53, 54, 55, 56, 57, 45, 48, 51, 58, 51, 48, 34, 44, 34, 50, 48, 50, 48, 45, 48, 49, 45, 49, 50, 84, 49, 50, 58, 49, 51, 58, 49, 52, 46, 49, 50, 51, 52, 53, 54, 55, 56, 57, 45, 48, 51, 58, 51, 48, 34, 44, 34, 50, 48, 50, 48, 45, 48, 49, 45, 49, 50, 84, 49, 50, 58, 49, 51, 58, 49, 52, 46, 49, 50, 51, 52, 53, 54, 55, 56, 57, 45, 48, 51, 58, 51, 48, 34, 93, 0, 0 };
    int size = 115;
    ZonedDateTime[] values = dslJson.deserialize(manifest, body, size);
    Assert.assertArrayEquals(lts, values);
}

```
TEST INPUT: `jw`,`lts`


# METHOD UNDER TEST
```java
/**
 * Main serialization API.
 * Convert object instance into JSON.
 * <p>
 * JsonWriter contains a growable byte[] where JSON will be serialized.
 * After serialization JsonWriter can be copied into OutputStream or it's byte[] can be obtained
 * <p>
 * For best performance reuse `JsonWriter` or even better call `JsonWriter.WriteObject` directly
 *
 * @param writer where to write resulting JSON
 * @param value  object instance to serialize
 * @throws IOException error when unable to serialize instance
 */
public final void serialize(final JsonWriter writer, @Nullable final Object value) throws IOException {
    if (writer == null) {
        throw new IllegalArgumentException("writer can't be null");
    }
    if (value == null) {
        writer.writeNull();
        return;
    }
    final Class<?> manifest = value.getClass();
    if (!serialize(writer, manifest, value)) {
        if (fallback == null) {
            throw new ConfigurationException("Unable to serialize provided object. Failed to find serializer for: " + manifest);
        }
        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        fallback.serialize(value, stream);
        writer.writeAscii(stream.toByteArray());
    }
}

/**
 * Deserialize API for working with streams.
 * Deserialize provided stream input into target object.
 * This method reuses thread local reader for processing JSON input.
 * <p>
 * Since JSON is often though of as a series of char,
 * most libraries will convert inputs into a sequence of chars and do processing on them.
 * <p>
 * When working on InputStream DslJson will process JSON in chunks of byte[] inputs.
 * <p>
 *
 * @param manifest target type
 * @param stream   input JSON
 * @return deserialized instance
 * @throws IOException error during deserialization
 */
@Nullable
public Object deserialize(final Type manifest, final InputStream stream) throws IOException {
    if (manifest instanceof Class<?>) {
        return deserialize((Class<?>) manifest, stream);
    }
    if (manifest == null) {
        throw new IllegalArgumentException("manifest can't be null");
    }
    if (stream == null) {
        throw new IllegalArgumentException("stream can't be null");
    }
    final JsonReader json = localReader.get().process(stream);
    try {
        json.getNextToken();
        final Object result = deserializeWith(manifest, json);
        if (result != unknownValue)
            return result;
        if (fallback != null) {
            return fallback.deserialize(context, manifest, new RereadStream(json.buffer, stream));
        }
        throw new ConfigurationException("Unable to find reader for provided type: " + manifest + " and fallback serialization is not registered.\n" + "Try initializing DslJson with custom fallback in case of unsupported objects or register specified type using registerReader into " + getClass());
    } finally {
        json.reset();
    }
}

```


# REQUIRED DELIVERABLE
Construct five new values for the test input `jw`,`lts`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    ZonedDateTime now = ZonedDateTime.parse("2020-01-12T12:13:14.123456789-03:30");
    JsonWriter jw = dslJson.newWriter(34);
    ZonedDateTime[] lts = new ZonedDateTime[3];
    Arrays.fill(lts, now);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 