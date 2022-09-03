class Solution {
    public String solution(int n) {
        //즉 1,2,4 를 통해 만들 수 있는 n가지 숫자들 중 n번째 가장 큰 녀석을 구해라 
        // 경우의 수가 점차 적으로 증가한다. 
        // 일의 자리 수 3개
        // 십의 자리 수 3개 * 3
        // 백의 3*3*3 
        // 해당 n 이 3으로 나눠지는가? 계속해서 나눈 뒤 
        // 몫만큼 해당 값을 skip, 0 만큼 새로이 시작.
        String[] num  = {"4","1","2"};
        String answer = "";
        while(n>0){
            int left = n%3;
            n/= 3;
            if(left == 0){
                n--;
            }
            answer = num[left] + answer;
        }
        return answer;
    }
}