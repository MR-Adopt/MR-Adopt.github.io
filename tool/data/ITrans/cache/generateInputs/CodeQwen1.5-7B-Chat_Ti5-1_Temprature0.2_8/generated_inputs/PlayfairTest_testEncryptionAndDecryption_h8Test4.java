package com.thealgorithms.ciphers;

import com.thealgorithms.ciphers.PlayfairCipher;
import com.thealgorithms.ciphers.PlayfairCipher.*;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class PlayfairTest_testEncryptionAndDecryption_h8Test4 {

    @Test
    public void testEncryptionAndDecryption_h8Test4() {
    PlayfairCipher playfairCipher = new PlayfairCipher("ALGORITHM");
    String plaintext = "COMPUTER";
    String textTodecrypt = playfairCipher.encrypt(plaintext);
        String encryptedText = playfairCipher.encrypt(plaintext);
        String decryptedText = playfairCipher.decrypt(textTodecrypt);
        assertEquals(plaintext, decryptedText);
    }
}

