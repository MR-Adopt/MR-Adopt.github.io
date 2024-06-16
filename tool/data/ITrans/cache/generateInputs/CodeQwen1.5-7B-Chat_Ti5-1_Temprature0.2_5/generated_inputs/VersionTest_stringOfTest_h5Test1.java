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
public class VersionTest_stringOfTest_h5Test1 {

    @Test
    public void stringOfTest_h5Test1() {
    String v = "1.1.0";
        String v1 = "1.0.0";
        Version version = Version.valueOf(v);
        Version version1 = Version.valueOf(v1);
        assertEquals(v, version.stringOf());
        assertEquals(v, Version.stringOf(version1));
    }
}

