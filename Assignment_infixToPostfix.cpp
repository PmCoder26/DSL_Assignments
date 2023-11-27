

#include<iostream>
#include<string>
using namespace std;

class Stack{
private:
    int size, rear;
    char st[];
public:
    Stack(int size){
        this->size=size;
        st[this->size];
        rear=-1;
    }
    bool isEmpty(){
        return rear==-1;
    }
    bool isFull(){
        return rear==size-1;
    }
    void push(char c){
        if(isFull()){
            cout<<"Stack is empty!"<<endl;
        }
        else{
            st[++rear]=c;
        }
    }
    char pop(){
        if(isEmpty()){
            cout<<"The stack is empty!"<<endl;
        }
        else{
            return st[rear--];
        }
    }
    char peek(){
        if(isEmpty()){
            cout<<"The stack is empty!"<<endl;
        }
        else{
            return st[rear];
        }
    }
};

bool isOperator(char c){
    if(c=='+' || c=='-' || c=='/' || c=='*' || c=='%'){
        return true;
    }
    else{
        return false;
    }
}
bool isChar(char c){
    if((c>='A' && c<='Z') || (c>='a' && c<='z')){
        return true;
    }
    else{
        return false;
    }
}
int precedence(char c){
    // here, 1 is high and 0 is low.
    if(c=='+' || c=='-'){
        return 0;
    }
    else if(c=='/' || c=='*' || c=='%'){
        return 1;
    }
    else{
        return -1;
    }
}

string infixToPostix(Stack st, string exp) {
    if (exp.empty()) {
        cout << "Empty expression!" << endl;
        return exp;
    } else {
        string ans="";
        for(int x=0; x<exp.length(); x++) {
            char c = exp[x];
            // checking whether 'c' is character or not.
            if(isChar(c)){
                ans+=c;
            }
            // checking whether 'c' is operator or not.
            else if(isOperator(c)){
                // if the stack is empty then directly push c in stack.
                if(st.isEmpty()){
                    st.push(c);
                }
                else{
                        // checking for the precedence.
                     // if the precedence of the 'c' is grater than the last of stack.
                    if(precedence(c)>precedence(st.peek())){
                        st.push(c);
                    }
                    else{
                        // add the characters till the precedence doesn't match
                        // or condition is satisfied as,
                        if(!st.isEmpty() && (precedence(c)<=precedence(st.peek()))){
                            ans+=st.pop();
                        }
                        // after then push the 'c' as its precedence is high.
                        st.push(c);
                    }
                }
            }
            // checking for the brackets.
            else{
                if(c=='(' || c=='{' || c=='['){
                    st.push(c);
                }
                else{
                    if(c==')'){
                        while(!st.isEmpty() && st.peek()!='('){
                            ans+=st.pop();
                        }
                        if(!st.isEmpty() && st.peek()=='('){
                            st.pop();
                        }
                    }
                    else if(c=='}'){
                        while(!st.isEmpty() && st.peek()!='{'){
                            ans+=st.pop();
                        }
                        if(!st.isEmpty() && st.peek()=='{'){
                            st.pop();
                        }
                    }
                    else if(c==']'){
                        while(!st.isEmpty() && st.peek()!='['){
                            ans+=st.pop();
                        }
                        if(!st.isEmpty() && st.peek()=='['){
                            st.pop();
                        }
                    }
                }
            }
        }

        // for the remaining elements.
        while(!st.isEmpty())
        {
            ans += st.pop();
        }
        return ans;
    }
}
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
                        if ((curr == '{' && c == '}') || (c == ']' && curr == '[')
                            || (curr == '(' && c == ')')) {
                            // as match is found then remove it from the stack
                            // for further pair checking.
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

    int ans=1;
    try {
        while (ans == 1) {
            int n;
            cout << "Enter the size of the stack: ";
            cin >> n;
            Stack st(n);
            string exp;
            cout << "Enter the expression in the form of infix: ";
            cin >> exp;
            if (!isValidParenthesis(st, exp)) {
                cout << "The expression is not well parenthesised!" << endl;
                cout << "Hence cannot proceed further!" << endl;
            } else {
                cout << "The postfix form of the infix expression is: " << infixToPostix(st, exp) << endl;
            }
            cout << "Do you want to continue the program?(Yes - 1, No - 2)" << endl;
            cout << "Your response(1 or 2): ";
            cin >> ans;
            if(ans!=1 && ans!=2){
                throw ans;
            }
        }
    }
    catch(int x){
        cout<<"Invalid input!"<<endl;
    }

}
