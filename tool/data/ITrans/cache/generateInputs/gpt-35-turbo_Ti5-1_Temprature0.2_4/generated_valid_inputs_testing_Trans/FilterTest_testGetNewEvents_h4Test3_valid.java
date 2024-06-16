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

import org.ethereum.rpc.FilterTest_testGetNewEvents;

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

class FilterTest_testGetNewEvents_h4Test3_valid {

    Filter filter;

    @BeforeEach
    void setUp() {
        filter = new Filter();
    }

    @Test
    void testGetNewEvents_h4Test3() {
    Filter.FilterEvent mockEvent = new FilterEventMock();
    Filter filter = null;
		List<Object> transformed_inputs = FilterTest_testGetNewEvents.inputTransformation_testGetNewEvents(mockEvent, filter);
    Filter.FilterEvent mockEvent2  = (Filter.FilterEvent) transformed_inputs.get(0);
    Filter filter2  = (Filter) transformed_inputs.get(1);
        filter.add(mockEvent);
        filter2.add(mockEvent2);
        Object[] events1 = filter2.getNewEvents();
        assertArrayEquals(new Object[] { mockEvent.getJsonEventObject() }, events1);
    }

    static class FilterEventMock implements Filter.FilterEvent {

        @Override
        public Object getJsonEventObject() {
            return "MockObject";
        }
    }
}

