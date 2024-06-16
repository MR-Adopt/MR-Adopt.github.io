package software.amazon.event.ruler;

import org.junit.Test;
import java.util.HashSet;
import java.util.Set;
import static java.util.Arrays.asList;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;


import software.amazon.event.ruler.NameState;
import software.amazon.event.ruler.NameState.*;
import java.util.List;
import java.util.Arrays;

public class NameStateTest_testNextNameStateWithAdditionalNameStateReuse {
    public static List<Object> inputTransformation_testNextNameStateWithAdditionalNameStateReuse(String key, NameState nextNameState) {
        String key2 = key;
        NameState nameState2 = nextNameState;
        List<Object> transformed_inputs = Arrays.asList(key2, nameState2);
        return transformed_inputs;
    }
}