package com.thealgorithms.ciphers;

import com.thealgorithms.ciphers.PlayfairCipher;
import com.thealgorithms.ciphers.PlayfairCipher.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class PlayfairTest_testEncryptionAndDecryption_h7Test3 {

    @Test
    public void testEncryptionAndDecryption_h7Test3() {
    PlayfairCipher playfairCipher = new PlayfairCipher("DEMO");
    String plaintext = "DEMOGRAPHICS";
    String textTodecrypt = "JJJJJJJJJ";
        String encryptedText = playfairCipher.encrypt(plaintext);
        String decryptedText = playfairCipher.decrypt(textTodecrypt);
        assertEquals(plaintext, decryptedText);
    }
}

