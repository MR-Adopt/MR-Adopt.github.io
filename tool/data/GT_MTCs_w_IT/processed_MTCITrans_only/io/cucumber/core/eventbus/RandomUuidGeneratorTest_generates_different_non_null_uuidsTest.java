package io.cucumber.core.eventbus;

import io.cucumber.core.eventbus.UuidGenerator;
import io.cucumber.core.eventbus.UuidGenerator.*;

import org.junit.jupiter.api.Test;

import java.util.UUID;

import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;

class RandomUuidGeneratorTest_generates_different_non_null_uuidsTest {
//     @Test
//     void generates_different_non_null_uuids_h() {
//         // Given
//         UuidGenerator generator = new RandomUuidGenerator();
//         UuidGenerator generator2 = new RandomUuidGenerator();
//         UUID uuid1 = generator.generateId();
// 
//         // When
//         UUID uuid2 = generator2.generateId();
// 
//         // Then
//         assertNotNull(uuid1);
//         assertNotNull(uuid2);
//         assertNotEquals(uuid1, uuid2);
//     }
// 
// //     public static UuidGenerator inputTransformation_generates_different_non_null_uuids(UuidGenerator generator) {
// //         UuidGenerator generator2  = generator;
// //         return generator2;
// //     }
// // 
    @Test
    void generates_different_non_null_uuids_IT() {
        // Given
        UuidGenerator generator = new RandomUuidGenerator();
        UuidGenerator generator2 = RandomUuidGeneratorTest_generates_different_non_null_uuids.inputTransformation_generates_different_non_null_uuids(generator);
        UUID uuid1 = generator.generateId();

        // When
        UUID uuid2 = generator2.generateId();

        // Then
        assertNotNull(uuid1);
        assertNotNull(uuid2);
        assertNotEquals(uuid1, uuid2);
    }
}