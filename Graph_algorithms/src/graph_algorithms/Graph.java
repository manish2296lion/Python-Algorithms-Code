/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package graph_algorithms;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;


public class Graph {

    private ArrayList<Vertex> vertices;
    private HashMap<Vertex,LinkedList<Vertex>> adjacencyList;
    
    public Graph(ArrayList<Vertex> V,HashMap<Vertex,LinkedList<Vertex>> A){
        this.vertices=V;
        this.adjacencyList=A;
    }
    
    public LinkedList<Vertex> adjecentElement(Vertex v){
        return adjacencyList.get(v);
    }
    
    public ArrayList<Vertex> getVertices(){
        return vertices;
    }
    
}
