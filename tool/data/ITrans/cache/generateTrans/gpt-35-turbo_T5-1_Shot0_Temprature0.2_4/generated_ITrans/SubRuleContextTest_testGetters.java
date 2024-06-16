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

public class SubRuleContextTest_testGetters {
    public static List<Object> inputTransformation_testGetters(SubRuleContext.Generator generator, String NAME)  {
        SubRuleContext.Generator generator2 = new SubRuleContext.Generator();
        Double id = -1.7976931348623157E308;
        List<Object> transformed_inputs = Arrays.asList(generator2, id);
        return transformed_inputs;
    }
}