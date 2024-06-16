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
SOURCE INPUT: `value`
FOLLOW UP INPUT: `message`,`clazz`


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


# NEW SOURCE INPUTS
## New source input0:
```java
    Long value = 0L;
```

## New source input1:
```java
    Long value = 1L;
```

## New source input2:
```java
    Long value = -1L;
```

## New source input3:
```java
    Long value = Long.MAX_VALUE;
```

## New source input4:
```java
    Long value = Long.MIN_VALUE;
```



# REQUIRED DELIVERABLE
For each new source input listed under 'NEW SOURCE INPUTS', please construct the corresponding follow-up input that satisfies your inferred relation and pass the assertions in the 'ORIGINAL TEST CASE'. Document the complete code for each new input pair in the format shown below:
## New input pairN:
```java
    Long value = random.nextLong(100_000L);
    String message = encryptedValue;
    Class<?> clazz = Long.class;
```

Additionally, for each new source input, provide the code used to generate the follow-up input along with its associated source input code. Please explain why this new input pair satisfies the inferred relation you have identified.