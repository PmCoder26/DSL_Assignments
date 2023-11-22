
#include<iostream>
#include<string>
using namespace std;


static class Stack{
    // stack using the array.

private:
    int size;
    int rear;
    char st[];

public:
    Stack(int size){
        this->size=size;
        st[size];
        rear=-1;
    }
    // function to check whether the stack is empty or not.
    bool isEmpty(){
        return rear==-1;
    }
    // function to check whether the stack is full or not.
    bool isFull(){
        return rear==size-1;
    }
    // function to push data in the stack.
    void push(char c){
        if(isFull()){
            cout<<"The stack is completely full!"<<endl;
        }
        else{
            st[++rear]=c;
        }
    }
    // function to pop data from the stack.
    char pop(){
        if(isEmpty()){
            cout<<"The stack is empty!"<<endl;
        }
        else{
            char c=st[rear--];
            return c;
        }
    }
    // function to peek the element from the stack.
    char peek(){
        if(isEmpty()){
            cout<<"The stack is empty!"<<endl;
            return ' ';
        }
        else{
            return st[rear];
        }
    }

};

// function to check the valid parenthesis.
bool isValidParenthesis(Stack st, string exp){
    if(exp.length()==0){
        return true;
    }
    else{
        for(int x=0; x<exp.length(); x++){
            char c=exp[x];
            // if the character is the alphabets or operators then skip the iteration.
            if(c!='[' && c!='{' && c!='(' && c!=')' && c!='}' && c!=']'){
                continue;
            }
            else {
                if (c == '[' || c == '{' || c == '(') {
                    st.push(c);
                } else {
                    // if the stack is empty, hence no match found for any closing bracket.
                    if (st.isEmpty()) {
                        return false;
                    } else {
                        // the current upper element in the stack.
                        char curr = st.peek();
                        if ((curr == '{' && c == '}') || (c == ']' && curr == '[') || (curr == '(' && c == ')')) {
                            // as match is found then remove it from the stack for further pair checking.
                            st.pop();
                        } else {
                            return false;
                        }
                    }
                }
            }
        }
        // if the stack is completely empty, that means the expression is valid
        // and all the parenthesis pairs have been matched and popped from the stack.
        if(st.isEmpty()){
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
            int size;
            cout<<"Enter the size of the stack: ";
            cin>>size;
            Stack st(size);
            string exp;
            cout << "Enter the expression:";
            cin >> exp;

            // checking the parenthesis.
            int v = isValidParenthesis(st, exp);
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
