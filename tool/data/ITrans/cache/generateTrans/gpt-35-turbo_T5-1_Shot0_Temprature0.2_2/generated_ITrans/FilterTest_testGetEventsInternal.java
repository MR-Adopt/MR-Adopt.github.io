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
import java.util.List;
import java.util.Arrays;

public class FilterTest_testGetEventsInternal {
    public static Filter inputTransformation_testGetEventsInternal(Filter filter) {
        Filter filter2 = new Filter();
        for (Filter.FilterEvent event : filter.getEventsInternal()) {
            filter2.add(event);
        }
        return filter2;
    }
}