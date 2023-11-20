
#include<iostream>
#include<string>
using namespace std;


// Node class for the stack.
static class Node{
public:
    char data;
    Node *next;
    Node(char data){
        this->data=data;
        this->next=NULL;
    }
};

static Node *head=NULL;

// function to check whether the stack is empty or not.
static bool isEmpty(){
    return head==NULL;
}

// function to push data in the stack.
static void push(char c){
    if(isEmpty()){
        head=new Node(c);
    }
    else{
        Node *newNode=new Node(c);
        newNode->next=head;
        head=newNode;
    }
}

// function to pop data from the stack.
static char pop(){
    if(isEmpty()){
        cout<<"The stack is empty!"<<endl;
    }
    else{
        char c=head->data;
        head=head->next;
        return c;
    }
}

// function to peek the element from the stack.
static char peek(){
    if(isEmpty()){
        cout<<"The stack is empty!"<<endl;
        return ' ';
    }
    else{
        return head->data;
    }
}

// function to print the stack.
static void printStack(){
    if(isEmpty()){
        cout<<"The stack is empty!"<<endl;
        return;
    }
    else{
        Node *curr=head;
        while(curr!=NULL){
            cout<<curr->data<<" ";
            curr=curr->next;
        }
        cout<<endl;
    }
}

// function to check the valid parenthesis.
bool isValidParenthesis(string exp){
    if(exp.length()==0){
        return true;
    }
    else{
        for(int x=0; x<exp.length(); x++){
            char c=exp[x];
            if(c=='[' || c=='{' || c=='('){
                push(c);
            }
            else{
                // if the stack is empty, hence no match found for any closing bracket.
                if(isEmpty()){
                    return false;
                }
                else{
                    if((peek()=='{' && c=='}') || (c==']' && peek()=='[') || (peek()=='(' && c==')')){
                        // as match is found then remove it from the stack for further pair checking.
                        pop();
                    }
                    else{
                        return false;
                    }
                }
            }
        }
        // if the stack is completely empty, that means the expression is valid
        // and all the parenthesis pairs have been matched and popped from the stack.
        if(isEmpty()){
            return true;
        }
        else{
            return false;
        }
    }
}

int main(){

    int choice=1;
    try {
        while(choice==1) {
            head = NULL;
            string exp;
            cout << "Enter the expression:";
            cin >> exp;

            // checking the parenthesis.
            int v = isValidParenthesis(exp);
            if (v == 0) {
                cout << "The validity of the expression is: false" << endl;
            } else {
                cout << "The validity of the expression is: true" << endl;
            }
            cout<<"Do you want to continue the program?(1. Yes, 2. No)"<<endl;
            cout<<"Your Response: ";
            cin>>choice;
            if(choice!=1 && choice!=2){
                throw choice;
            }
        }
    }
    catch(int choice){
        cout<<"Invalid choice!"<<endl;
    }










    return 0;
}
