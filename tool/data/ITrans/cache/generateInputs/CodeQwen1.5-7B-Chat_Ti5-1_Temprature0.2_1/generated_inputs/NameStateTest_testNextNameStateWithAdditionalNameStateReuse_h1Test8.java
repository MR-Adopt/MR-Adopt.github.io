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

public class NameStateTest_testNextNameStateWithAdditionalNameStateReuse_h1Test8 {

    @Test
    public void testNextNameStateWithAdditionalNameStateReuse_h1Test8() {
    NameState nameState = new NameState();
    NameState nextNameState = new NameState();
    String key = "key5";
    String key2 = "key5";
    NameState nameState2 = nameState;
        nameState.addNextNameState(key, nextNameState);
        assertEquals(nextNameState, nameState2.getNextNameState(key2));
    // nameState.removeNextNameState("key");
    // assertNull(nameState.getNextNameState("key"));
    }
}
