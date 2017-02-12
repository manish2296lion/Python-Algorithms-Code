/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package arrays;

import java.util.ArrayList;

/**
 *
 * @author Manish_Madugula
 */
public class MaxSubArray {
    
    public static int badAlgo(int n,ArrayList<Integer> al)
    {
        
        int max_val=al.get(0);
            
        for(int k=0;k<n;k++)
        {
            for(int i=n-1;i>k-1;i--)
            {
                int sum=0;
                for(int l=k;l<=i;l++)
                {
                    sum=sum+al.get(l);
                }
                if (sum>max_val)
                {
                    max_val=sum;
                }
            }

        }
        return max_val;
    }
    
    public static int kadaneAlgo(int n,ArrayList<Integer> al){
        int currentSum=al.get(0);
        int maxSum=al.get(0);
        for(int i=1;i<n;i++)
        {       
            currentSum=max(al.get(i),currentSum+al.get(i));
            System.out.println(currentSum);
            if(currentSum>maxSum)
            {
                maxSum=currentSum;
            }
        }
        return maxSum;
    }
    
    public static int max(int a,int b){
        if(a<b){
        return b;
        }
        else if(a>b){
        return a;
        }
        else{
        return b;
        }
    }
    
}
