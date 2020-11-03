


public class Lab4 {

    public boolean commonEnd(int[] a, int[] b)
    {
        if(a[0] == b[0] || a[a.length - 1] == b[b.length - 1]){
            return true;
        }
        else{
            return false;
        }

    }
    public boolean sameFirstLast(int[] nums) {
        if(nums.length >= 1 && nums[0] == nums[nums.length - 1])
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    public boolean firstLast6(int[] nums) {
        int len = nums.length;
        if(nums[0] == 6 || nums[len-1] == 6){
            return true;
        }
        else{
            return false;
        }
    }
    public int[] plusTwo(int[] a, int[] b) {
        int Res[] = new int [4];
        for(int i = 0; i < Res.length; i++){
            if(i >= 2)
            {
                Res[i] = b[i-2];
            }
            else
            {
                Res[i] = a[i];
            }

        }
        return Res;
    }



}