/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package graph_algorithms;

import java.util.LinkedList;

/**
 *
 * @author Manish_Madugula
 */
public class Queue<E> {
    
    private LinkedList<E> queue;
    
    public Queue(){
        queue=new LinkedList<E>();
    }
    
    public int length(){
        return queue.size();
    }
    public void enqueue(E V){
        queue.add(V);
    }
    
    public E dequeue(){
        E c=queue.getFirst();
        queue.removeFirst();
        return c;
    }
    
    
}
