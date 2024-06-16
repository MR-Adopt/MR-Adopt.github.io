package org.apache.rocketmq.tieredstore.common;

import java.util.ArrayList;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import org.apache.commons.lang3.tuple.Pair;
import org.junit.Assert;
import org.junit.Test;


import org.apache.rocketmq.tieredstore.common.InFlightRequestKey;
import org.apache.rocketmq.tieredstore.common.InFlightRequestKey.*;
import org.apache.rocketmq.tieredstore.common.InFlightRequestFuture;
import org.apache.rocketmq.tieredstore.common.InFlightRequestFuture.*;
import java.util.List;
import java.util.Arrays;

public class InFlightRequestFutureTest_testInFlightRequestKey {
    public static InFlightRequestKey inputTransformation_testInFlightRequestKey(InFlightRequestKey requestKey1)  {
        InFlightRequestKey requestKey2 = new InFlightRequestKey(requestKey1.getGroup(), requestKey1.getSomeValue(), requestKey1.getAnotherValue());
        return requestKey2;
    }
}