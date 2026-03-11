import java.util.HashMap;
import java.util.Map;

public class OOPSBannerAppUC8 {

    private static Map<Character, String[]> bannerMap = new HashMap<>();

    public static void buildCharacterPatterns() {
        bannerMap.put('O', new String[]{
            "  ***  ",
            " *   * ",
            " *   * ",
            " *   * ",
            "  ***  "
        });
        
        bannerMap.put('P', new String[]{
            " ****  ",
            " *   * ",
            " ****  ",
            " *     ",
            " *     "
        });
        
        bannerMap.put('S', new String[]{
            "  **** ",
            " *     ",
            "  ***  ",
            "     * ",
            " ****  "
        });
    }

    public static void displayBanner(String message) {
        int numRows = 5;
        
        for (int row = 0; row < numRows; row++) {
            StringBuilder sb = new StringBuilder();
            
            for (int i = 0; i < message.length(); i++) {
                char c = message.charAt(i);
                String[] pattern = bannerMap.get(c);
                
                if (pattern != null) {
                    sb.append(pattern[row]).append("   "); 
                } else {
                    sb.append("       ").append("   ");
                }
            }
            System.out.println(sb.toString());
        }
    }

    public static void main(String[] args) {
        buildCharacterPatterns();
        String targetWord = "OOPS";
        displayBanner(targetWord);
    }
}