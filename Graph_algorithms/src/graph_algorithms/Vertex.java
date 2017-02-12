/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package graph_algorithms;

/**
 *
 * @author Manish_Madugula
 */
public class Vertex {
    
    private boolean visited=false;
    private String name;
    private boolean finished=false;
    private Integer distance=10000000;
    private Vertex parent=null;
    
    public Vertex(String s){
        this.name=s;
    }
    public String name(){
        return this.name;
    }
    public boolean visited(){
        return this.visited;
    }
    public Vertex visit(){
        this.visited=true;
        return this;
    }
    public boolean finished(){
        return this.finished;
    }
    public Vertex finish(){
        this.finished=true;
        return this;
    }
    public Integer distance(){
        return this.distance;
    }
    
    public Integer distance(Integer d){
        this.distance=d;
        return this.distance;
    }
    
    public Vertex parent(){
        return this.parent;
    }
    
    public Vertex parent(Vertex v){
        this.parent=v;
        return this.parent;
    }
    
    
}
