package software.amazon.event.ruler;

import software.amazon.event.ruler.NameState;
import software.amazon.event.ruler.NameState.*;
import org.junit.Test;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import static java.util.Arrays.asList;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertTrue;

public class NameStateTest_testNextNameStateWithAdditionalNameStateReuse_h0Test2 {

    @Test
    public void testNextNameStateWithAdditionalNameStateReuse_h0Test2() {
    NameState nameState = new NameState();
    NameState nextNameState = new NameState();
    String key = "key2";
    String key2 = "key2";
    NameState nameState2 = nameState;
        nameState.addNextNameState(key, nextNameState);
        assertEquals(nextNameState, nameState2.getNextNameState(key2));
    // nameState.removeNextNameState("key");
    // assertNull(nameState.getNextNameState("key"));
    }
}

