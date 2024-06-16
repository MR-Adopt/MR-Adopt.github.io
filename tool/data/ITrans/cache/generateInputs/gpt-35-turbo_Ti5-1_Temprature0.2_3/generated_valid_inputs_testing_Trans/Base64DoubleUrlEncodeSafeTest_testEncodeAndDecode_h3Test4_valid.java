package org.tsugi.util;

import org.tsugi.util.Base64DoubleUrlEncodeSafeTest_testEncodeAndDecode;

import org.tsugi.util.Base64DoubleUrlEncodeSafe.*;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;
import static org.junit.Assert.assertFalse;
import org.junit.Test;
import org.tsugi.util.Base64DoubleUrlEncodeSafe;

public class Base64DoubleUrlEncodeSafeTest_testEncodeAndDecode_h3Test4_valid {

    public static String[] testStrings = { "Hello, Base64DoubleUrlEncodeSafe!", "Testing encoding and decoding.", "12345", "This is a longer string with more characters.", "A tree 🌲 was here", "A", "https://www.tsugicloud.org/lti/store/?x=42&y=26", "https://www.tsugicloud.org/lti_store/?x=42&y=26", "https://chat.openai.com/failed/to_solve!this[problem]with{auto}generated:code;", " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~", "  !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~", "   !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~", "    !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~", // Lets throw in some mean Unicode stuff
    "ஹ௸௵꧄.ဪ꧅⸻𒈙𒐫﷽𒌄𒈟𒍼𒁎𒀱𒈓𒍙𒊎𒄡𒅌𒁏𒀰𒐪𒈙𒐫𱁬𰽔𪚥䨻龘䲜       𓀐𓂸😃⃢👍༼;´༎ຶ ۝ ༎ຶ༽", "hÃllo What is the weather tomorrow Göödnight 😊", "Ḽơᶉëᶆ ȋṕšᶙṁ ḍỡḽǭᵳ ʂǐť ӓṁệẗ, ĉṓɲṩḙċťᶒțûɾ ấɖḯƥĭṩčįɳġ ḝłįʈ, șếᶑ ᶁⱺ ẽḭŭŝḿꝋď ṫĕᶆᶈṓɍ ỉñḉīḑȋᵭṵńť ṷŧ ḹẩḇőꝛế éȶ đꝍꞎôꝛȇ ᵯáꞡᶇā ąⱡîɋṹẵ.", " ăѣ𝔠ծềſģȟᎥ𝒋ǩľḿꞑȯ𝘱𝑞𝗋𝘴ȶ𝞄𝜈ψ𝒙𝘆𝚣1234567890!@#$%^&*()-_=+[{]};:'\",<.>/?~𝘈Ḇ𝖢𝕯٤ḞԍНǏ𝙅ƘԸⲘ𝙉০Ρ𝗤Ɍ𝓢ȚЦ𝒱Ѡ𝓧ƳȤѧᖯć𝗱ễ𝑓𝙜Ⴙ𝞲𝑗𝒌ļṃŉо𝞎𝒒ᵲꜱ𝙩ừ𝗏ŵ𝒙𝒚ź1234567890!@#$%^&*()-_=+[{]};:'\",<.>/?~АḂⲤ𝗗𝖤𝗙ꞠꓧȊ𝐉𝜥ꓡ𝑀𝑵Ǭ𝙿𝑄Ŗ𝑆𝒯𝖴𝘝𝘞ꓫŸ𝜡ả𝘢ƀ𝖼ḋếᵮℊ𝙝Ꭵ𝕛кιṃդⱺ𝓅𝘲𝕣𝖘ŧ𝑢ṽẉ𝘅ყž1234567890!@#$%^&*()-_=+[{]};:'\",<.>/?~Ѧ𝙱ƇᗞΣℱԍҤ١𝔍К𝓛𝓜ƝȎ𝚸𝑄Ṛ𝓢ṮṺƲᏔꓫ𝚈𝚭𝜶Ꮟçძ𝑒𝖿𝗀ḧ𝗂𝐣ҝɭḿ𝕟𝐨𝝔𝕢ṛ𝓼тú𝔳ẃ⤬𝝲𝗓1234567890!@#$%^&*()-_=+[{]};:'\",<.>/?~𝖠Β𝒞𝘋𝙴𝓕ĢȞỈ𝕵ꓗʟ𝙼ℕ০𝚸𝗤ՀꓢṰǓⅤ𝔚Ⲭ𝑌𝙕𝘢𝕤 – Andrew Feb 10, 2019 at 14:41", // https://jeff.cis.cabrillo.edu/tools/homoglyphs
    "Ǐ ᴛ𝕙ȋṉ𝔨 Ꮥɑ𝝹𝛂îꝒⱡů𝒔 ị𝗌 𝑎 𝝂𝕖ᵳℽ ƈθꝋȴ ŵ𝕒ɣ ṫố ɪṅⱦẽ𝑔ṛѧȶể Ṥảⱪȁ𝗶 Ꭵℼṱᴏ Ḉ𝜶𝕟ṽ𝜶𝗌, 𝘿2𝕷, ąп𝔡 Бḻáċĸѣò𝐚ȑ𝒹", "" };

    @Test
    public void testEncodeAndDecode_h3Test4() throws java.io.UnsupportedEncodingException {
    String input = "Hello, World!";
    String encoded2  = Base64DoubleUrlEncodeSafeTest_testEncodeAndDecode.inputTransformation_testEncodeAndDecode(input);
        String encoded = Base64DoubleUrlEncodeSafe.encode(input);
        String decoded = Base64DoubleUrlEncodeSafe.decode(encoded2);
        assertEquals("Decoding did not produce the original string for input: " + input, input, decoded);
        try {
            String urlEncoded = java.net.URLEncoder.encode(encoded, "UTF-8");
        } catch (java.io.UnsupportedEncodingException e) {
            fail("Unxpected UnsupportedEncodingException for URLEncoder " + encoded);
        }
    }
    // Make sure at least one of the testStrings produces a string that changes upon URLEncoding to
}

