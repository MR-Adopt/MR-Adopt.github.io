# ORIGINAL TEST CASE
```java
@Test
public void test1() {
    JSONArray v01 = new JSONArray();
    String str2 = JSON.toJSONString(v01);
    String str = JSON.toJSONString(v01);
    JSONArray v02 = JSON.parseObject(str2, JSONArray.class);
    assertEquals(v01, v02);
}

```
SOURCE INPUT: `v01`
FOLLOW UP INPUT: `str2`,`clazz`


# METHOD UNDER TEST
```java
/**
 * Serializes the specified object to the json string
 *
 * @param object the specified object will be serialized
 * @param format the specified date format
 * @param filters the specified filters is applied to serialization
 * @param features the specified features is applied to serialization
 * @return {@link String} that is not null
 * @throws JSONException If a serialization error occurs
 */
static String toJSONString(Object object, String format, Filter[] filters, JSONWriter.Feature... features) {
    final JSONWriter.Context context = new JSONWriter.Context(JSONFactory.defaultObjectWriterProvider, features);
    if (format != null && !format.isEmpty()) {
        context.setDateFormat(format);
    }
    if (filters != null && filters.length != 0) {
        context.configFilter(filters);
    }
    try (JSONWriter writer = JSONWriter.of(context)) {
        if (object == null) {
            writer.writeNull();
        } else {
            writer.rootObject = object;
            writer.path = JSONWriter.Path.ROOT;
            Class<?> valueClass = object.getClass();
            ObjectWriter<?> objectWriter = context.getObjectWriter(valueClass, valueClass);
            objectWriter.write(writer, object, null, null, 0);
        }
        return writer.toString();
    }
}

/**
 * Parses the json reader through the specified delimiter as
 * {@link T} objects and call the specified consumer to consume it
 *
 * @param input the specified reader to be parsed
 * @param type the specified actual class of {@link T}
 * @param delimiter the specified delimiter for the stream
 * @param consumer the specified consumer is called multiple times
 * @throws JSONException If an I/O error or parsing error occurs
 * @throws NullPointerException If the specified reader is null
 * @since 2.0.2
 */
@SuppressWarnings("unchecked")
static <T> void parseObject(Reader input, char delimiter, Type type, Consumer<T> consumer) {
    final int cacheIndex = System.identityHashCode(Thread.currentThread()) & (CACHE_ITEMS.length - 1);
    final CacheItem cacheItem = CACHE_ITEMS[cacheIndex];
    char[] chars = CHARS_UPDATER.getAndSet(cacheItem, null);
    if (chars == null) {
        chars = new char[8192];
    }
    int offset = 0, start = 0, end;
    ObjectReader<? extends T> objectReader = null;
    final JSONReader.Context context = JSONFactory.createReadContext();
    try {
        while (true) {
            int n = input.read(chars, offset, chars.length - offset);
            if (n == -1) {
                break;
            }
            int k = offset;
            offset += n;
            boolean dispose = false;
            for (; k < offset; ++k) {
                if (chars[k] == delimiter) {
                    end = k;
                    JSONReader jsonReader = JSONReader.of(chars, start, end - start, context);
                    if (objectReader == null) {
                        objectReader = context.getObjectReader(type);
                    }
                    consumer.accept(objectReader.readObject(jsonReader, type, null, 0));
                    start = end + 1;
                    dispose = true;
                }
            }
            if (offset == chars.length) {
                if (dispose) {
                    int len = chars.length - start;
                    System.arraycopy(chars, start, chars, 0, len);
                    start = 0;
                    offset = len;
                } else {
                    chars = Arrays.copyOf(chars, chars.length + 8192);
                }
            }
        }
    } catch (IOException e) {
        throw new JSONException("JSON#parseObject cannot parse the 'Reader' to '" + type + "'", e);
    } finally {
        CHARS_UPDATER.lazySet(cacheItem, chars);
    }
}

```


# NEW SOURCE INPUTS
## New source input0:
```java
JSONArray v01 = new JSONArray();
v01.add("Hello");
```

## New source input1:
```java
JSONArray v01 = new JSONArray();
v01.add(123);
```

## New source input2:
```java
JSONArray v01 = new JSONArray();
v01.add(true);
```

## New source input3:
```java
JSONArray v01 = new JSONArray();
v01.add(3.14);
```

## New source input4:
```java
JSONArray v01 = new JSONArray();
JSONObject obj = new JSONObject();
obj.put("name", "John");
obj.put("age", 30);
v01.add(obj);
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    JSONArray v01 = new JSONArray();
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.