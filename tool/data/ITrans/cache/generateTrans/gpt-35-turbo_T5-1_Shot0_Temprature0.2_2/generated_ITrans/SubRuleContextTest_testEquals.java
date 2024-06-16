package software.amazon.event.ruler;

import org.junit.Test;
import java.util.HashSet;
import java.util.Set;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertTrue;


import software.amazon.event.ruler.SubRuleContext;
import software.amazon.event.ruler.SubRuleContext.*;
import java.util.List;
import java.util.Arrays;

public class SubRuleContextTest_testEquals {
    public static List<Object> inputTransformation_testEquals(SubRuleContext.Generator generatorA, String NAME) {
        SubRuleContext.Generator generatorB = new SubRuleContext.Generator();
        String NAME2 = new String(NAME);
        List<Object> transformed_inputs = Arrays.asList(generatorB, NAME2);
        return transformed_inputs;
    }
}