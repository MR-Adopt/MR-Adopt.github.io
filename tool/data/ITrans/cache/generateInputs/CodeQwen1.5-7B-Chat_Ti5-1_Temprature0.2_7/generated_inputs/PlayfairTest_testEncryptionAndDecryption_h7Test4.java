package com.thealgorithms.ciphers;

import com.thealgorithms.ciphers.PlayfairCipher;
import com.thealgorithms.ciphers.PlayfairCipher.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class PlayfairTest_testEncryptionAndDecryption_h7Test4 {

    @Test
    public void testEncryptionAndDecryption_h7Test4() {
    PlayfairCipher playfairCipher = new PlayfairCipher("CIPHER");
    String plaintext = "ENCRYPT";
    String textTodecrypt = "JJJJJJJJJ";
        String encryptedText = playfairCipher.encrypt(plaintext);
        String decryptedText = playfairCipher.decrypt(textTodecrypt);
        assertEquals(plaintext, decryptedText);
    }
}

