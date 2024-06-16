package org.mitre.synthea.engine;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;
import org.junit.Test;
import org.mitre.synthea.engine.ExpressedSymptom.SymptomInfo;
import org.mitre.synthea.engine.ExpressedSymptom.SymptomSource;


import org.mitre.synthea.engine.ExpressedSymptom;
import org.mitre.synthea.engine.ExpressedSymptom.*;
import java.util.List;
import java.util.Arrays;

public class ExpressedSymptomTest_testExpressedSymtpom {
    public static List<Object> inputTransformation_testExpressedSymtpom(ExpressedSymptom symptom, String module) {
        ExpressedSymptom symptom2 = symptom;
        String module2 = module;
        List<Object> transformed_inputs = Arrays.asList(symptom2, module2);
        return transformed_inputs;
    }
}