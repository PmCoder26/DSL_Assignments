
/*
    Assignment-8 (Group-C).
        Problem Statement:
            Second year CE class, set A of students like vanilla ice-cream and
            set B of students like butter-scotch ice-cream. Write C++ program
            to store two sets using linked list, compute and display:
                1. Set of students who like both vanilla and butter-scotch.
                2. Set of students who like neither vanilla nor butter-scotch.
                3. Set of students who like either vanilla or butter-scotch but
                   not both.
 */


#include<iostream>
using namespace std;

// Node class of the linked list.
class Node{
    public:
        string name;
        Node* next;
        Node(string name){
            this->next=NULL;
            this->name=name;
        }
};

// Functions.

// function for creating the students' list.
Node* createList(){
    try {
        int n;
        cout << "Enter the no.of students: ";
        cin >> n;
        if(n<0){
            throw(n);
        }
        else{
            Node* list=NULL;
            for(int i=0; i<n; i++){
                string name;
                char flav1, flav2;
                cout<<"Enter name: ";
                cin>>name;
                Node* temp=new Node(name);
                temp->next=list;
                list=temp;
            }
            return (list);
        }
    }
    catch(int n){
        cout<<"Invalid input!"<<endl;
        return NULL;
    }
}

// function to print the student list.
void printList(Node* list){
    if(list==NULL){
        cout<<"List is empty!"<<endl;
    }
    else{
        cout<<"The students are: "<<endl;
        while(list!=NULL){
            cout<<list->name<<endl;
            list=list->next;
        }
    }
}

// function to check whether name is present in the list or not.
bool contains(Node* node, string name){
    if(node==NULL){
        return false;
    }
    else{
        while(node!=NULL){
            if(node->name==name){
                return true;
            }
            node=node->next;
        }
        return false;
    }
}

// function to find the union of A and B.
Node* vOrB(Node* A, Node* B){
    if(A==NULL &&  B==NULL){
        return A;
    }
    else{
        Node* ans=NULL;
        // filling the non-repeating elements of set B.
        while(B!=NULL){
            Node* newNode=new Node(B->name);
            newNode->next=ans;
            ans=newNode;
            B=B->next;
        }
        // filling the elements of A which is not in ans.
        while(A!=NULL){
            if(!contains(ans, A->name)){
                Node* newNode=new Node(A->name);
                newNode->next=ans;
                ans=newNode;
            }
            A=A->next;
        }
        return ans;
    }
}

// function to find the students who like both vanilla and butter-scotch.
Node* vAndBList(Node* A, Node* B){
    // if one of the list is empty then no sense to find the students.
    if(A==NULL || B==NULL){
        return NULL;
    }
    else{
        Node* both=NULL;
        while(A!=NULL){
            Node *temp=B;
            while(temp!=NULL){
                // if the student is in both the list.
                if(temp->name==A->name){
                    Node* newNode=new Node(temp->name);
                    newNode->next=both;
                    both=newNode;
                    break;
                }
                temp=temp->next;
            }
            A=A->next;
        }
        return (both);
    }
}

// function to find the students who like neither vanilla nor butter-scotch.
Node* nVnBList(Node* list, Node* A, Node* B){
    if(list==NULL){
        return list;
    }
    else{
        Node* ans=NULL;
        Node* unionList= vOrB(A, B);
        while(list!=NULL){
            if(!contains(unionList, list->name)){
                Node* newNode=new Node(list->name);
                newNode->next=ans;
                ans=newNode;
            }
            list=list->next;
        }
        return (ans);
    }
}

// function to print the students who like either vanilla or butter-scotch but
// not both.
Node* vOrB_ButNotBoth(Node* list, Node* A, Node* B){
    if(A==NULL && B==NULL){
        return A;
    }
    else{
        // intersection of A and B.
        Node* intersection= vAndBList(A, B);
        // union of A and B.
        Node* unionList= vOrB(A, B);
        Node* ans=NULL;
        // final answer.
        while(unionList!=NULL){
            if(!contains(intersection, unionList->name)){
                Node* temp=new Node(unionList->name);
                temp->next=ans;
                ans=temp;
            }
            unionList=unionList->next;
        }
        return ans;
    }
}

int main(){

    int res=1;
    while(res==1) {
        // list of total no.of students in class.
        Node *list;
        // creating the list of total no.of students in class.
        cout << "Creating the list of total no.of students in the class." << endl;
        list = createList();

        // printing the list of students of the class.
        cout << "The total students:" << endl;
        printList(list);

        // creating and printing the list of students who like vanilla flavour.
        cout << "Enter the details of students who like vanilla ice-cream." << endl;
        Node *A = createList();
        cout << "List of students who like vanilla:" << endl;
        printList(A);

        // creating and printing the list of students who like butter-scotch flavour.
        cout << "Enter the details of students who like butter-scotch ice-cream." << endl;
        Node *B = createList();
        cout << "List of students who like butter-scotch:" << endl;
        printList(B);

//    // printing the list of students who like both vanilla and butter-scotch.
        cout << "The list of the students who like both vanilla and butter-scotch is:" << endl;
        printList(vAndBList(A, B));
//
//    // printing the list of the students who like neither vanilla nor butter-scotch.
        cout << "The list of the students who like neither vanilla nor butter-scotch is:" << endl;
        printList(nVnBList(list, A, B));

//    // printing the list of Set of students who like either vanilla or butter-scotch but
//    // not both.
        cout << "The list of students who like either vanilla or butter-scotch but not both is: " << endl;
        printList(vOrB_ButNotBoth(list, A, B));

        cout<<"Do you want to continue the program?\n1. Yes\n2. No"<<endl;
        cout<<"Your Response-";
        cin>>res;
    }




    return 0;
}














