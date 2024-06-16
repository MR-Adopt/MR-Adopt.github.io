package software.amazon.event.ruler;

import software.amazon.event.ruler.SubRuleContext;
import software.amazon.event.ruler.SubRuleContext.*;

import org.junit.Test;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertTrue;

public class SubRuleContextTest_testEquals_hTest {

    private static final String NAME = "name";

    @Test
    public void testEquals_h() {
        String NAME = "name";
        SubRuleContext.Generator generatorA = new SubRuleContext.Generator();
        SubRuleContext contextA1 = generatorA.generate(NAME);
        // SubRuleContext contextA2 = generatorA.generate(NAME);
        
        String NAME2 = "name";
        SubRuleContext.Generator generatorB = new SubRuleContext.Generator();
        SubRuleContext contextB1 = generatorB.generate(NAME2);

        assertTrue(contextA1.equals(contextB1));
        // assertFalse(contextA2.equals(contextB1));
    }
}