/*
 * Copyright 2018-2023 datagear.tech
 *
 * This file is part of DataGear.
 *
 * DataGear is free software: you can redistribute it and/or modify it under the terms of
 * the GNU Lesser General Public License as published by the Free Software Foundation,
 * either version 3 of the License, or (at your option) any later version.
 *
 * DataGear is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
 * without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License along with DataGear.
 * If not, see <https://www.gnu.org/licenses/>.
 */
package org.datagear.util.version;

import org.datagear.util.version.VersionTest_isHigherThanTest;

import org.datagear.util.version.Version;
import org.datagear.util.version.Version.*;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

/**
 * {@linkplain Version}单元测试类。
 *
 * @author datagear@163.com
 */
public class VersionTest_isHigherThanTest_h6Test0_valid {

    @Test
    public void isHigherThanTest_h6Test0() {
    String v1 = "1.0.1";
    String v2  = VersionTest_isHigherThanTest.inputTransformation_isHigherThanTest(v1);
        String v3 = "1.0";
        String v4 = "2.1";
        Version a = Version.valueOf(v1);
        Version b = Version.valueOf(v2);
        Version c = Version.valueOf(v3);
        Version d = Version.valueOf(v4);
        assertFalse(a.isHigherThan(b));
    }
}

