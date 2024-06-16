package io.vertx.core.json.jackson;

import java.lang.invoke.MethodHandle;
import java.lang.invoke.MethodHandles;
import java.lang.invoke.MethodType;
import java.util.concurrent.CountDownLatch;
import com.fasterxml.jackson.core.util.BufferRecycler;
import org.junit.Assume;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertSame;
import static org.junit.Assert.assertTrue;


import io.vertx.core.json.jackson.HybridJacksonPool;
import io.vertx.core.json.jackson.HybridJacksonPool.*;
import java.util.List;
import java.util.Arrays;

public class HybridJacksonPoolTest_testVirtualThreadPoolWithSingleThread {
    public static HybridJacksonPool.StripedLockFreePool inputTransformation_testVirtualThreadPoolWithSingleThread(HybridJacksonPool.StripedLockFreePool virtualPool)  {
        HybridJacksonPool.StripedLockFreePool virtualPool2 = new HybridJacksonPool.StripedLockFreePool(virtualPool.getCapacity());
        return virtualPool2;
    }
}