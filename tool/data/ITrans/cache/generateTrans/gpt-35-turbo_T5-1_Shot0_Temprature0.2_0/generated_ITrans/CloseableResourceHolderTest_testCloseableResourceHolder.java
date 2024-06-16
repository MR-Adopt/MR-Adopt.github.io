package org.apache.druid.collections;

import org.junit.Assert;
import org.junit.Test;
import java.io.Closeable;
import java.util.concurrent.atomic.AtomicLong;


import org.apache.druid.collections.ResourceHolder;
import org.apache.druid.collections.ResourceHolder.*;
import java.util.List;
import java.util.Arrays;

public class CloseableResourceHolderTest_testCloseableResourceHolder {
    public static ResourceHolder<Closeable> inputTransformation_testCloseableResourceHolder(Closeable closeable)  {
        ResourceHolder<Closeable> holder2 = ResourceHolder.fromCloseable(closeable);
        return holder2;
    }
}