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
        String group = requestKey1.getGroup();
        int sequenceNumber = requestKey1.getSequenceNumber() + 1;
        int requestNumber = requestKey1.getRequestNumber() + 1;
        InFlightRequestKey requestKey2 = new InFlightRequestKey(group, sequenceNumber, requestNumber);
        return requestKey2;
    }
}