package org.ethereum.rpc;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotSame;
import static org.junit.jupiter.api.Assertions.assertTrue;


import org.ethereum.rpc.Filter;
import org.ethereum.rpc.Filter.*;
import org.ethereum.rpc.FilterTest;
import org.ethereum.rpc.FilterTest.*;
import java.util.List;
import java.util.Arrays;

public class FilterTest_testGetNewEvents {
    public static List<Object> inputTransformation_testGetNewEvents(Filter.FilterEvent mockEvent, Filter filter) {
        Filter filter2 = new Filter();
        filter2.add(mockEvent);
        Filter.FilterEvent mockEvent2 = new FilterEventMock();
        filter2.add(mockEvent2);
        List<Object> transformed_inputs = Arrays.asList(mockEvent2, filter2);
        return transformed_inputs;
    }
}