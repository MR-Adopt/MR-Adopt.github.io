# ORIGINAL TEST CASE
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
TEST INPUT: `value`


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


# REQUIRED DELIVERABLE
Construct five new values for the test input `value`. Each new input should explore valid values. Present the code for constructing each new input in the following format:
## New inputN:
```java
    Long value = random.nextLong(100_000L);
```

Provide the construction code for each of the five new test inputs, and explain why this input is valid. 