/* Copyright (C) 2003-2007  The Chemistry Development Kit (CDK) project
 *
 * Contact: cdk-devel@lists.sourceforge.net
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public License
 * as published by the Free Software Foundation; either version 2.1
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 */
package org.openscience.cdk;

import org.openscience.cdk.Association;
import org.openscience.cdk.Association.*;
import java.util.Arrays;
import java.util.List;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.openscience.cdk.interfaces.IAtom;
import org.openscience.cdk.test.CDKTestCase;

/**
 * Checks the functionality of the Association class.
 *
 * @cdk.module test-extra
 *
 * @see org.openscience.cdk.Association
 */
class AssociationTest_testGetAtomAt_h1Test7 extends CDKTestCase {

    @Test
    void testGetAtomAt_h1Test7() {
    int position = 3;
    Atom n = new Atom("N");
    association.setAtomAt(n, position);
    Association association2 = new Association(c, o);
        // Assertions.assertEquals(c, association.getAtomAt(0));
        // Assertions.assertEquals(o, association.getAtomAt(1));
        association.setAtomAt(n, position);
        Assertions.assertEquals(n, association2.getAtomAt(position2));
    }
}
