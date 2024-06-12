package com.thealgorithms.ciphers;

import com.thealgorithms.ciphers.PlayfairCipher;
import com.thealgorithms.ciphers.PlayfairCipher.*;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

public class PlayfairTest_testEncryptionAndDecryption_hTest {

    @Test
    public void testEncryptionAndDecryption_h() {
        PlayfairCipher playfairCipher = new PlayfairCipher("KEYWORD");

        String plaintext = "PLAYFAIR";
        String encryptedText = playfairCipher.encrypt(plaintext);
        assertEquals("SHHAHRFB", encryptedText);
        String textTodecrypt = "SHHAHRFB";
        String decryptedText = playfairCipher.decrypt(textTodecrypt);

        assertEquals(plaintext, decryptedText);
    }
}