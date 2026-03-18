
class Solution {
    public String maximumTime(String time) {
        
        // hour logic: if first digit is 1 -> second = 9. if 2 -> second 3. 
        // if second digit <=3 -> first = 2. else -> first = 1

        // minutes logic: if first digit is <= 5 -> second = 9. else not possible
        // no matter what the second digit is, first = 5

        char h_1 = time.charAt(0);
        char h_2 = time.charAt(1);

        char m_1 = time.charAt(3);
        char m_2 = time.charAt(4);
        System.out.println("chars "+h_1+" "+ h_2+" "+m_1+" "+m_2);


        if (h_1 == '?' && h_2=='?') {
            h_1 = '2';
            h_2 = '3';
        }
        // second hour digit is known
        else if (h_1=='?') {
            if (Integer.parseInt(h_2+"")<=3) {
                h_1 = '2';
            } else {
                h_1 = '1';
            }
        }
        // first hour digit is known
        else if (h_2=='?') {
            if (Integer.parseInt(h_1+"")==0) {
                h_2 = '9';
            }
            else if (Integer.parseInt(h_1+"")==1) {
                h_2 = '9';
            } else {
                h_2 = '3';
            }
        }

        // minutes logic
        if (m_1=='?') {
            m_1 = '5';
        }
        if (m_2=='?') {
            m_2 = '9';
        }

        System.out.println("chars "+h_1+" "+ h_2+" "+m_1+" "+m_2);

        // String max_time = ""+h_1 + h_2 + ':'+m_1+m_2;
       
        char[] max_chars = {h_1,h_2, ':', m_1, m_2};
        String max_time = new String(max_chars);
        System.out.println(max_time);
        return max_time;
    }
}