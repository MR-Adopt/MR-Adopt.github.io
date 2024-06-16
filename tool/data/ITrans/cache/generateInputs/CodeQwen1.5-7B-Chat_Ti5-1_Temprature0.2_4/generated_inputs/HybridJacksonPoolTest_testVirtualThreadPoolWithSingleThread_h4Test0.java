package io.vertx.core.json.jackson;

import io.vertx.core.json.jackson.HybridJacksonPool;
import io.vertx.core.json.jackson.HybridJacksonPool.*;
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

public class HybridJacksonPoolTest_testVirtualThreadPoolWithSingleThread_h4Test0 {

    @Test
    public void testVirtualThreadPoolWithSingleThread_h4Test0() {
    HybridJacksonPool.StripedLockFreePool virtualPool = new HybridJacksonPool.StripedLockFreePool(0);
    HybridJacksonPool.StripedLockFreePool virtualPool2 = new HybridJacksonPool.StripedLockFreePool(0);
        BufferRecycler pooledResource = virtualPool.acquirePooled();
        virtualPool.releasePooled(pooledResource);
        assertEquals(1, virtualPool.size());
        virtualPool2.releasePooled(pooledResource);
        // The same thread should get the same pooled resource
        assertSame(pooledResource, virtualPool2.acquirePooled());
    }
}

