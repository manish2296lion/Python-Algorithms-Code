/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package graph_algorithms;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
/**
 *
 * @author Manish_Madugula
 */
public class DFSandBFS {    
    
    public static void main(String[] args) {
        //Initailize the graph;
        
        String[] v = {"a1","b1","c1","d1","e1","f1"};
        ArrayList<Vertex> vertices = new ArrayList<Vertex>();
        for(String name:v){
            vertices.add(new Vertex(name));
        }
        
//        Lets add a reference to all vertices
        
        Vertex a=vertices.get(0);
        Vertex b=vertices.get(1);
        Vertex c=vertices.get(2);
        Vertex d=vertices.get(3);
        Vertex e=vertices.get(4);
        Vertex f=vertices.get(5);
        
        
        
        HashMap<Vertex,LinkedList<Vertex>> hm=new HashMap<Vertex,LinkedList<Vertex>>();
        
        LinkedList a_list=new LinkedList<Vertex>();
        LinkedList b_list=new LinkedList<Vertex>();
        LinkedList c_list=new LinkedList<Vertex>();
        LinkedList d_list=new LinkedList<Vertex>();
        LinkedList e_list=new LinkedList<Vertex>();
        LinkedList f_list=new LinkedList<Vertex>();

//        Adding to linked list
        a_list.add(d);
        b_list.add(d);
        d_list.add(c);
        f_list.add(a);
        f_list.add(b);
        
//        Mapping Vertex and its adjacency list
        hm.put(a,a_list);
        hm.put(b,b_list);
        hm.put(d,d_list);
        hm.put(f,f_list);
        
        
        
//        Creating Graph
        
        Graph graph=new Graph(vertices,hm);
        //ArrayList<String> list =new ArrayList<String>();
        
//        I actually implement topological sort
        
        //depthFirstSearch(graph,f,list);
        //Collections.reverse(list);
        
        //for(String s:list){
//            System.out.println(s);
        //}
        
//        Now I implement shortest distance
        
        breadthFirstSearch(graph, f);
        for (Vertex vert:vertices){
            System.out.println(vert.distance());
        }
        
    }
    
    
    public static void depthFirstSearch(Graph graph,Vertex s,ArrayList<String> list){
        
        s.visit();
        if(graph.adjecentElement(s)==null){
            s.finish();
            list.add(s.name());
            return;
        }
        for(Vertex v:graph.adjecentElement(s)){
            if(!v.visited()){
            depthFirstSearch(graph,v,list);
            }
        }
        
        s.finish();
        list.add(s.name());
    }
    
    public static void breadthFirstSearch(Graph graph,Vertex s){
        s.visit();
        s.distance(0);
        Queue<Vertex> q= new Queue<Vertex>();
        q.enqueue(s);
        while(q.length()>0){
            Vertex v=q.dequeue();
            if(graph.adjecentElement(v)!=null){
                
                for(Vertex vert:graph.adjecentElement(v)){
                    if(!vert.visited()){
                        vert.parent(v);
                        vert.distance(vert.parent().distance()+1);
                        vert.visit();
                        q.enqueue(vert);
                    }
                }
                
            }
            
        }
    }
    
}
