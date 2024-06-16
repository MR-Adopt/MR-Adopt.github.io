package io.cucumber.core.eventbus;

import org.junit.jupiter.api.Test;
import java.util.UUID;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;


import io.cucumber.core.eventbus.UuidGenerator;
import io.cucumber.core.eventbus.UuidGenerator.*;
import java.util.List;
import java.util.Arrays;

public class RandomUuidGeneratorTest_generates_different_non_null_uuids {
    public static UuidGenerator inputTransformation_generates_different_non_null_uuids(UuidGenerator generator)  {
        UuidGenerator generator2 = new UuidGenerator();
        return generator2;
    }
}