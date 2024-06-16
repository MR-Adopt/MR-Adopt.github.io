package org.openscience.cdk;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.openscience.cdk.interfaces.IAtom;
import org.openscience.cdk.test.CDKTestCase;


import org.openscience.cdk.Association;
import org.openscience.cdk.Association.*;
import java.util.List;
import java.util.Arrays;

public class AssociationTest_testGetAtomAt {
    public static List<Object> inputTransformation_testGetAtomAt(Association association, Atom n, int position)  {
        Association association2 = new Association(n, association.getAtomAt(1));
        int position2 = 0;
        List<Object> transformed_inputs = Arrays.asList(association2, position2);
        return transformed_inputs;
    }
}