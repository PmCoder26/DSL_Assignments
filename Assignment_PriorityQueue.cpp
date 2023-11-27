/*
        Write a program to implement a priority queue in C++ using an inorder list
        to store items in queue. Create a class that includes the data items(which
        should be template) and the priority(should be an integer). The in-ordered list
        should contain these objects, with operator <= overloaded so that the items with
        the highest priority appear at the start of list.
 */


#include<iostream>
using namespace std;

class Node{
public:
    int n, p;   // data - n, and priority - p;
    Node(int n, int p){
        this->n=n;
        this->p=p;
    }
    void printInfo(){
        cout<<"Data - "<<this->n<<", ";
        cout<<"Priority - "<<this->p<<endl;
    }
};

class PriorityQueue{
private:
    int size, rear;
    Node pq[];      // array of nodes.
public:
    PriorityQueue(int size){
        this->size=size;
        rear=-1;
        pq[size];
    }
    bool isEmpty(){
        return rear==-1;
    }
    bool isFull(){
        return rear==size-1;
    }
    void shift(int idx){
        for(int x=rear+1; x>idx && x>0; x--){
            pq[x]=pq[x-1];
        }
    }
    int prioIdx(int p){
        for(int x=0; x<=rear && x<size; x++){
            if(pq[x].p==p){
                return x+1;
            }
            else if(pq[x].p>p){
                return x;
            }
        }
        return rear+1;
    }
    void add(int n, int p){
        if(p<=0){
            cout<<"Invalid data inputs!"<<endl;
            return;
        }
        if(isFull()){
            cout<<"The priority queue is full!"<<endl;
            return;
        }
        else{
                // approach - 1.
            if(rear==-1) {
                // adding the first element.
                pq[++rear] = Node(n, p);
            }
            else{
                // finding the idx where the priority of element at that idx
                // is greater than that of which to be inserted.
                int idx= prioIdx(p);
                // shifting the elements from that idx so that the space
                // will be vacant to insert the element.
                shift(idx);
                // inserting the element at idx.
                pq[idx]=Node(n, p);

                    // approach - 2.
//                pq[++rear]=Node(n, p);
                // sorting the array w.r.t. the priorities using the selection sort.
//                sort();
                rear++;
            }
        }
    }
    Node remove(){
        if(isEmpty()){
            cout<<"The priority queue is empty!"<<endl;
            return Node(-1, -1);
        }
        else{
            Node curr=pq[0];
            // shifting the nodes/elements so that the front's space
            // will be covered.
            for(int x=0; x<rear; x++){
                pq[x]=pq[x+1];
            }
            rear--;
            return curr;
        }
    }
    void sort(){
        if(isEmpty()){
            return;
        }
        else{
            for(int x=0; x<rear; x++){
                int min=x;
                for(int y=x+1; y<=rear; y++){
                    if(pq[min].p > pq[y].p){
                        min=y;
                    }
                }
                Node temp=pq[min];
                pq[min]=pq[x];
                pq[x]=temp;
            }
        }
    }
    void print(){
        if(isEmpty()){
            cout<<"The priority queue is empty!"<<endl;
        }
        else{
            for(int x=0; x<=rear; x++){
                pq[x].printInfo();
            }
        }
    }
};


int main(){

    int ans=1;
    while(ans==1) {
        int res=1, size;
        cout<<"Enter the size of the priority queue: ";
        cin>>size;
        PriorityQueue *pq = new PriorityQueue(size);
        while(res==1){
            int choice;
            cout<<"What would you like to perform?"<<endl;
            cout<<"1.Add element.\n2.Remove element.\n3.Print the priority queue.\nYour response(1 or 2): ";
            cin>>choice;
            if(choice==1){
                int n, p;
                cout<<"Enter the data: ";
                cin>>n;
                cout<<"Enter its priority: ";
                cin>>p;
                pq->add(n, p);
            }
            else if(choice==2){
                pq->remove();
            }
            else if(choice==3){
                pq->print();
            }
            else{
                cout<<"Invalid choice!"<<endl;
            }
            cout<<"Do you want to continue manipulating with same priority queue?"<<endl;
            cout<<"Your response(Yes - 1, No - 2): ";
            cin>>res;
        }
        cout<<"Do you want to continue with the program?"<<endl;
        cout<<"Your response(Yes - 1, No - 2): ";
        cin>>ans;
    }


}