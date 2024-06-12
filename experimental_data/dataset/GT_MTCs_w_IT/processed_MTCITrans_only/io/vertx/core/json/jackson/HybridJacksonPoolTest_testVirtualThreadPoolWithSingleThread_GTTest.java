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

public class HybridJacksonPoolTest_testVirtualThreadPoolWithSingleThread_GTTest {

//   @Test
//   public void testVirtualThreadPoolWithSingleThread_h() {
//     HybridJacksonPool.StripedLockFreePool virtualPool = new HybridJacksonPool.StripedLockFreePool(4);
//     BufferRecycler pooledResource = virtualPool.acquirePooled(); virtualPool.releasePooled(pooledResource);
//     assertEquals(1, virtualPool.size());
// 
//     HybridJacksonPool.StripedLockFreePool virtualPool2 = new HybridJacksonPool.StripedLockFreePool(4); virtualPool2.releasePooled(pooledResource);
//     // The same thread should get the same pooled resource
//     assertSame(pooledResource, virtualPool2.acquirePooled());
//   }
// 
// //   public static HybridJacksonPool.StripedLockFreePool inputTransformation_testVirtualThreadPoolWithSingleThread(HybridJacksonPool.StripedLockFreePool virtualPool) {
// //     int stripesCount = virtualPool.stackStats().length;
// //     HybridJacksonPool.StripedLockFreePool virtualPool2 = new HybridJacksonPool.StripedLockFreePool(stripesCount);
// //     BufferRecycler pooledResource = virtualPool.acquirePooled();
// //     virtualPool2.releasePooled(pooledResource);
// //     return virtualPool2;
// //   }
// // 
  @Test
  public void testVirtualThreadPoolWithSingleThread_IT() {
    
    HybridJacksonPool.StripedLockFreePool virtualPool = new HybridJacksonPool.StripedLockFreePool(4);
    BufferRecycler pooledResource = virtualPool.acquirePooled();virtualPool.releasePooled(pooledResource);
    assertEquals(1, virtualPool.size());

    HybridJacksonPool.StripedLockFreePool virtualPool2 = HybridJacksonPoolTest_testVirtualThreadPoolWithSingleThread_GT.inputTransformation_testVirtualThreadPoolWithSingleThread(virtualPool);
    // The same thread should get the same pooled resource
    assertSame(pooledResource, virtualPool2.acquirePooled());
  }

}