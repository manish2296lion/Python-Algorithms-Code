package arrays;

import java.util.*;

class Array{
        
    public static void main(String[] args){
        
        Scanner s=new Scanner(System.in);
        
        ArrayList<Integer> al= new ArrayList<Integer>();
        
        System.out.println("Enter the array as a string eg-23 32 43 532 -323");
        
        String[] integerArray=s.nextLine().split("\\s");
        
        int n=integerArray.length;
        
        for(String str:integerArray){
        al.add(Integer.parseInt(str));
        }
        

//        For Maximum Subarray Part
//        int max_val=MaxSubArray.kadaneAlgo(n, al);

        //This is for minimum length sub array problem
       
        System.out.println("Enter the value which the subarray must be more than");
        
        
        
        
        //For output;
//        System.out.println(max_val);
            
        
    }
    
    
    
    
    
    
}