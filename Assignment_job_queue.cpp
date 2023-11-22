
/*
        Queues are frequently used in the computer programming
        and a typical example is the creation of job queue by an
        operating system. If the operating system does not use
        priorities, then the jobs processed in the order they enter the system.
        Write C++ program for simulating job queue. Write functions to add
        and delete the job from queue.
 */

#include<iostream>
using namespace std;

class Job{
public:
    string post;
    int salary;
    Job(string p, int s){
        salary=s;
        post=p;
    }
    void printDetails(){
        cout<<"************************************"<<endl;
        cout<<"Job post: "<<post<<endl;
        cout<<"Salary: "<<salary<<endl;
        cout<<"************************************"<<endl;
    }
};

class Queue{
private:
    int size, rear;
    Job *jobs[];
public:
    Queue(int size){
        this->size=size;
        rear=-1;
        jobs[size];
    }
    // function to check whether the queue is empty or not.
    bool isEmpty(){
        return rear==-1;
    }
    // function to check whether queue is full or not.
    bool isFull(){
        return rear==size-1;
    }
    // function to add element in the queue.
    void add(){
        if(isFull()){
            cout<<"Since queue is full, no more jobs to add!"<<endl;
        }
        else{
            string p;
            int s;
            cout<<"Enter the post: ";
            cin>>p;
            cout<<"Enter the salary: ";
            cin>>s;
            Job *j=new Job(p, s);
            jobs[++rear]=j;
            cout<<"Job added successfully!"<<endl;
        }
    }
    // function to remove/delete the element from the queue.
    Job* remove(){
        if(isEmpty()){
            cout<<"Since the queue is empty, no more jobs to remove!"<<endl;
            return NULL;
        }
        else{
            Job *j=jobs[0];
            // for the case if there exists only one job, otherwise works fine with
            // all the cases, with no problem.
            jobs[0]=NULL;
            // rearranging the arrangement of the elements in the queue.
            for(int x=0; x<rear; x++){
                jobs[x]=jobs[x+1];
            }
            rear--;
            cout<<"Job removed successfully!"<<endl;
            return j;
        }
    }
    // function to print all the elements(jobs) of the queue.
    void jobList(){
        if(isEmpty()){
            cout<<"No more jobs to print their details!"<<endl;
        }
        else{
            cout<<"The list of the jobs is as follows,"<<endl;
            for(int x=0; x<=rear; x++){
                jobs[x]->printDetails();
            }
        }
    }
};

int main(){

    int ans=1, size;
    cout<<"Enter the size of the queue: ";
    cin>>size;
    Queue *q=new Queue(size);

    try {
        while (ans == 1) {
            int res;
            cout << "What would you like to perform?"<<endl;
            cout<<"1. Print all the jobs with details."<<endl;
            cout<<"2. Add a new job."<<endl;
            cout<<"3. Delete a job."<<endl;
            cout<<"Your response(1, 2, 3):";
            cin>>res;
            if(res!=1 && res!=2 && res!=3){
                throw res;
            }
            else{
                switch(res){
                    case 1:{
                        q->jobList();
                        break;
                    }
                    case 2:{
                        q->add();
                        break;
                    }
                    case 3:{
                        q->remove();
                        break;
                    }
                }
            }
            cout<<"Do you want to continue manipulating with the job queue?"<<endl;
            cout<<"Your response(Yes-1, No-2): ";
            cin>>ans;
            if(ans!=1 && ans!=2){
                throw ans;
            }
        }
    }
    catch(int res){
        cout<<"Invalid input!"<<endl;
    }






    return 0;
}
