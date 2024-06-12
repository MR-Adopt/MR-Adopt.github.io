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
class AssociationTest_testGetAtomAt extends CDKTestCase {

    @Test
    void testGetAtomAt_h() {
        Atom c = new Atom("C");
        Atom o = new Atom("O");
        Atom n = new Atom("N");
        Association association = new Association(c, o);

        // Assertions.assertEquals(c, association.getAtomAt(0));
        // Assertions.assertEquals(o, association.getAtomAt(1));

        int position = 0; 
        association.setAtomAt(n, position);
        Association association2 = new Association(n,o);
        int position2 = 0;
        Assertions.assertEquals(n, association2.getAtomAt(position2));
    }


    public static List<Object> inputTransformation_testGetAtomAt(Association association, Atom n, int position) {

        Association association2 = new Association(n, new Atom("O"));
        association2.setAtomAt(n, position);
		List<Object> transformed_inputs = Arrays.asList(association2, position);
		return transformed_inputs;
	}

    @Test
    void testGetAtomAt_IT() {
        Atom c = new Atom("C");
        Atom o = new Atom("O");
        Atom n = new Atom("N");
        Association association = new Association(c, o);
        int position = 0; 

        List<Object> transformed_inputs = inputTransformation_testGetAtomAt(association, n, position);
        
        association.setAtomAt(n, position);
        Association association2 = (Association) transformed_inputs.get(0);
        int position2 = (int) transformed_inputs.get(1);
        Assertions.assertEquals(n, association2.getAtomAt(position2));
    }




}