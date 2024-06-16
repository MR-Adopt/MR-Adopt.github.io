package com.vladmihalcea.hpjp.util;

import com.vladmihalcea.hpjp.util.CryptoUtilsTest_testPerformanceUsingCache;

import com.vladmihalcea.hpjp.util.CryptoUtils;
import com.vladmihalcea.hpjp.util.CryptoUtils.*;
import com.codahale.metrics.MetricRegistry;
import com.codahale.metrics.Slf4jReporter;
import com.codahale.metrics.Timer;
import com.vladmihalcea.hpjp.spring.transaction.readonly.config.stats.SpringTransactionStatisticsReport;
import org.hibernate.internal.util.collections.BoundedConcurrentHashMap;
import org.junit.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.TimeUnit;
import java.util.stream.LongStream;
import static org.junit.Assert.assertEquals;

/**
 * @author  Vlad Mihalcea
 */
public final class CryptoUtilsTest_testPerformanceUsingCache_h5Test1_valid {

    public static Logger LOGGER = LoggerFactory.getLogger(SpringTransactionStatisticsReport.class);

    private MetricRegistry metricRegistry = new MetricRegistry();

    private Slf4jReporter logReporter = Slf4jReporter.forRegistry(metricRegistry).outputTo(LOGGER).convertDurationsTo(TimeUnit.MICROSECONDS).build();

    private final Timer encryptTimer = metricRegistry.timer("encryptTimer");

    private final Timer decryptTimer = metricRegistry.timer("decryptTimer");

    private final ThreadLocalRandom random = ThreadLocalRandom.current();

    private int MAX_COUNT = 100_000;

    private final BoundedConcurrentHashMap<Long, String> encryptCache = new BoundedConcurrentHashMap<>(100_000, 20, BoundedConcurrentHashMap.Eviction.LIRS);

    private final BoundedConcurrentHashMap<String, Long> decryptCache = new BoundedConcurrentHashMap<>(100_000, 20, BoundedConcurrentHashMap.Eviction.LIRS);

    private int encryptCallCount = 0;

    private int decryptCallCount = 0;

    @Test
    public void testPerformanceUsingCache_h5Test1() {
    Long value = 5L;
    String encryptedValue = encryptCache.get(value);
		List<Object> transformed_inputs = CryptoUtilsTest_testPerformanceUsingCache.inputTransformation_testPerformanceUsingCache(value);
    String message  = (String) transformed_inputs.get(0);
    Class<?> clazz  = (Class<?>) transformed_inputs.get(1);
        long startNanos = System.nanoTime();
        if (encryptedValue == null) {
            encryptCallCount++;
            encryptedValue = CryptoUtils.encrypt(value);
            encryptCache.put(value, encryptedValue);
        }
        encryptTimer.update((System.nanoTime() - startNanos), TimeUnit.NANOSECONDS);
        startNanos = System.nanoTime();
        Long decryptedValue = decryptCache.get(encryptedValue);
        if (decryptedValue == null) {
            decryptCallCount++;
            decryptedValue = (Long) CryptoUtils.decrypt(message, clazz);
            decryptCache.put(encryptedValue, decryptedValue);
        }
        decryptTimer.update((System.nanoTime() - startNanos), TimeUnit.NANOSECONDS);
        assertEquals(value.longValue(), decryptedValue.longValue());
    }

    private void warmUp() {
        LongStream.rangeClosed(1, MAX_COUNT / 10).forEach(i -> {
            Long value = random.nextLong();
            String encryptedValue = CryptoUtils.encrypt(value);
            Long decryptedValue = CryptoUtils.decrypt(encryptedValue, Long.class);
            assertEquals(value.longValue(), decryptedValue.longValue());
        });
    }
}

