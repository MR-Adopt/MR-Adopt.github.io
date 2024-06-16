/*
 * This file is part of RskJ
 * Copyright (C) 2023 RSK Labs Ltd.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */
package org.ethereum.rpc;

import org.ethereum.rpc.Filter;
import org.ethereum.rpc.Filter.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import java.util.List;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotSame;
import static org.junit.jupiter.api.Assertions.assertTrue;

class FilterTest_testGetEventsInternal_h0Test1 {

    Filter filter;

    @BeforeEach
    void setUp() {
        filter = new Filter();
    }

    @Test
    void testGetEventsInternal_h0Test1() {
        Filter.FilterEvent mockEvent1 = new FilterEventMock();
        Filter.FilterEvent mockEvent2 = new FilterEventMock();
    Filter filter = new Filter();
    filter.add(mockEvent1);
    filter.add(mockEvent2);
    filter.add(null);
    Filter filter2 = new Filter();
    filter2.add(mockEvent1);
    filter2.add(mockEvent2);
    filter2.add(null);
        // get the internal events list and make sure it's a copy of the original list
        List<Filter.FilterEvent> events = filter.getEventsInternal();
        filter2.getEventsInternal();
        assertNotSame(events, filter2.getEventsInternal());
    }

    static class FilterEventMock implements Filter.FilterEvent {

        @Override
        public Object getJsonEventObject() {
            return "MockObject";
        }
    }
}

