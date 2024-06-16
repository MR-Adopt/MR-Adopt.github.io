package org.apache.druid.msq.exec;

import org.apache.druid.msq.indexing.error.MSQException;
import org.apache.druid.msq.indexing.error.NotEnoughTemporaryStorageFault;
import org.junit.Assert;
import org.junit.Test;


import org.apache.druid.msq.exec.WorkerStorageParameters;
import org.apache.druid.msq.exec.WorkerStorageParameters.*;
import java.util.List;
import java.util.Arrays;

public class WorkerStorageParametersTest_test_WorkerStorageParameter_createInstance {
    public static List<Object> inputTransformation_test_WorkerStorageParameter_createInstance(long l)  {
        long l2 = l * 2;
        boolean b = true;
        List<Object> transformed_inputs = Arrays.asList(l2, b);
        return transformed_inputs;
    }
}