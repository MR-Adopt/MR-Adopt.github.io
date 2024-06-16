# METHOD UNDER TEST
```java
public static String encrypt(Object message) {
    if (message == null) {
        throw new IllegalArgumentException("Only not-null values can be encrypted!");
    }
    try {
        Cipher cipher = getCipher();
        cipher.init(Cipher.ENCRYPT_MODE, getEncryptionKey());
        String messageValue = (message instanceof String) ? (String) message : String.valueOf(message);
        return Base64.getEncoder().encodeToString(cipher.doFinal(messageValue.getBytes(ENCODING)));
    } catch (Exception e) {
        throw new RuntimeException(e);
    }
}

public static <T> T decrypt(String message, Class<T> clazz) {
    try {
        Cipher cipher = getCipher();
        cipher.init(Cipher.DECRYPT_MODE, getEncryptionKey());
        String decryptedValue = new String(cipher.doFinal(Base64.getDecoder().decode(message)));
        return ReflectionUtils.invokeStaticMethod(ReflectionUtils.getMethodOrNull(clazz, "valueOf", String.class), decryptedValue);
    } catch (Exception e) {
        throw new RuntimeException(e);
    }
}

```


# TEST CASE
```java
@Test
public void testPerformance() {
    Long value = random.nextLong(100_000L);
    long startNanos = System.nanoTime();
    String encryptedValue = CryptoUtils.encrypt(value);
    encryptTimer.update((System.nanoTime() - startNanos), TimeUnit.NANOSECONDS);
    startNanos = System.nanoTime();
    String message = encryptedValue;
    Class<?> clazz = Long.class;
    Long decryptedValue = (Long) CryptoUtils.decrypt(message, clazz);
    decryptTimer.update((System.nanoTime() - startNanos), TimeUnit.NANOSECONDS);
    assertEquals(value.longValue(), decryptedValue.longValue());
}

```
SOURCE INPUT: `value`
FOLLOW UP INPUT: `message`,`clazz`


# OTHER INPUT PAIRS 
## Input pair1:
```java
Long value = random.nextLong(100_000L);
String message = encryptedValue;
Class<?> clazz = Long.class;
```

## Input pair2:
```java
Long value = 0L;
String message = CryptoUtils.encrypt(value);
Class<?> clazz = Long.class;
```

## Input pair3:
```java
Long value = 1L;
String message = CryptoUtils.encrypt(value);
Class<?> clazz = Long.class;
```

## Input pair4:
```java
Long value = -1L;
String message = CryptoUtils.encrypt(value);
Class<?> clazz = Long.class;
```

## Input pair5:
```java
Long value = Long.MAX_VALUE;
String message = CryptoUtils.encrypt(value);
Class<?> clazz = Long.class;
```

## Input pair6:
```java
Long value = Long.MIN_VALUE;
String message = CryptoUtils.encrypt(value);
Class<?> clazz = Long.class;
```

## Input pair7:
```java
Long value = random.nextLong();
String message = CryptoUtils.encrypt(value);
Class<?> clazz = Long.class;
```

## Input pair8:
```java
Long value = 123456789L;
String message = CryptoUtils.encrypt(value);
Class<?> clazz = Long.class;
```

## Input pair9:
```java
Long value = 1234567890L;
String message = CryptoUtils.encrypt(value);
Class<?> clazz = Long.class;
```



# OUTPUT FORMAT
```java
public class CryptoUtilsTest_testPerformance {
    public static List<Object> inputTransformation_testPerformance(Long value)  {
        // TODO
        String message = 
		Class<?> clazz = 
		List<Object> transformed_inputs = Arrays.asList(message, clazz);
		return transformed_inputs;
    }
}
```
Your task is to deduce the relationship between 'SOURCE INPUT' and 'FOLLOW UP INPUT' in the test case, and create a function that transforms 'SOURCE INPUT' into 'FOLLOW UP INPUT'.
The deduced relation and generated transformation function should be applicable to addtional input pairs and other potentail input pairs with similar characteristics.
Generate the transformation function by complementing the above code skeleton in 'OUTPUT FORMAT'.