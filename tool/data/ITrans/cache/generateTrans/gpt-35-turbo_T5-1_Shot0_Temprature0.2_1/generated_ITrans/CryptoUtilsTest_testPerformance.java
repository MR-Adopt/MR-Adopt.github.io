package com.vladmihalcea.hpjp.util;

import com.codahale.metrics.MetricRegistry;
import com.codahale.metrics.Slf4jReporter;
import com.codahale.metrics.Timer;
import com.vladmihalcea.hpjp.spring.transaction.readonly.config.stats.SpringTransactionStatisticsReport;
import org.hibernate.internal.util.collections.BoundedConcurrentHashMap;
import org.junit.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.TimeUnit;
import java.util.stream.LongStream;
import static org.junit.Assert.assertEquals;


import com.vladmihalcea.hpjp.util.CryptoUtils;
import com.vladmihalcea.hpjp.util.CryptoUtils.*;
import java.util.List;
import java.util.Arrays;

public class CryptoUtilsTest_testPerformance {
    public static List<Object> inputTransformation_testPerformance(Long value) {
        String message = CryptoUtils.encrypt(value);
        Class<?> clazz = Long.class;
        List<Object> transformed_inputs = Arrays.asList(message, clazz);
        return transformed_inputs;
    }
}