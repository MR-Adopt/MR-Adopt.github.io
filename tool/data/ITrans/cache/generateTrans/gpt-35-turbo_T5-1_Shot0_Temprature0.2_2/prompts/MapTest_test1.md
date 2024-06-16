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


# TEST CASE
```java
@Test
public void test1() {
    Map<String, Integer> v01 = new HashMap<>();
    v01.put("123", 123);
    v01.put("12x", 123);
    String str = JSON.toJSONString(v01);
    Map<String, Integer> v02 = JSON.parseObject(str, new TypeReference<Map<String, Integer>>() {
    }.getType());
    assertEquals(v01, v02);
}

```
SOURCE INPUT: `v01`
FOLLOW UP INPUT: `str2`,`mapType`


# OTHER INPUT PAIRS 
## Input pair1:
```java
v01.put("123", 123);
v01.put("12x", 123);
```

## Input pair2:
```java
v01.put("123", 123);
v01.put("12x", 123);
String str2 = JSON.toJSONString(v01);
```

## Input pair3:
```java
v01.put("abc", 456);
String str2 = JSON.toJSONString(v01);
```

## Input pair4:
```java
v01.put("", 789);
String str2 = JSON.toJSONString(v01);
```

## Input pair5:
```java
v01.put("789", 789);
v01.put("abc", 123);
String str2 = JSON.toJSONString(v01);
```

## Input pair6:
```java
v01.put("xyz", 0);
String str2 = JSON.toJSONString(v01);
```

## Input pair7:
```java
String str2 = "{\"abc\":456,\"def\":789,\"123\":123,\"12x\":123}";
```

## Input pair8:
```java
String str2 = "{}";
```

## Input pair9:
```java
String str2 = "{\"xyz\":null}";
```

## Input pair10:
```java
String str2 = "{\"789\":-789}";
```

## Input pair11:
```java
String str2 = "{\"1\":1,\"2\":2,\"3\":3,\"4\":4,\"5\":5}";
```

## Input pair12:
```java
v01.put("abc", 456);
v01.put("def", 789);
```

## Input pair13:
```java
v01.put("", 0);
```

## Input pair14:
```java
v01.put("key", -123);
```

## Input pair15:
```java
v01.put("key", Integer.MAX_VALUE);
```

## Input pair16:
```java
v01.put("123", 123);
v01.put("12x", 123);
String str2 = "{\"123\":123,\"12x\":123}";
```

## Input pair17:
```java
v01.put("abc", 456);
String str2 = "{\"abc\":456}";
```

## Input pair18:
```java
v01.put("", 789);
String str2 = "{\"\":789}";
```

## Input pair19:
```java
v01.put("key1", 0);
String str2 = "{\"key1\":0}";
```

## Input pair20:
```java
v01.put("key2", -123);
String str2 = "{\"key2\":-123}";
```

## Input pair21:
```java
v01.put("abc", 456);
v01.put("def", 789);
String str2 = JSON.toJSONString(v01);
```

## Input pair22:
```java
v01.put("", 0);
String str2 = JSON.toJSONString(v01);
```

## Input pair23:
```java
v01.put("abc", 123);
v01.put("def", 456);
v01.put("ghi", 789);
String str2 = JSON.toJSONString(v01);
```

## Input pair24:
```java
v01.put("abc", -123);
v01.put("def", -456);
v01.put("ghi", -789);
String str2 = JSON.toJSONString(v01);
```



# OUTPUT FORMAT
```java
public class MapTest_test1 {
    public static List<Object> inputTransformation_test1(Map<String, Integer> v01)  {
        // TODO
        String str2 = 
		Type mapType = 
		List<Object> transformed_inputs = Arrays.asList(str2, mapType);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.