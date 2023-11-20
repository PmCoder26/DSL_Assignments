#include<iostream>
using namespace std;


class Order{
public:
    string name;
    int price;
    string size;
    void printBill(){
        cout<<"\t\t\t\tBill."<<endl;
        cout<<"\t\tName:"<<name<<endl;
        cout<<"\t\tSize:"<<size<<endl;
        cout<<"\t\tprice:"<<price<<endl;
    }
};

static int front=-1 , rear=-1, size, bill;
// arrays for the prices of the pizza
static int pizza[4][3];
// arrays for the pizza types in menu and its sizes respectively.
static string m[4], ps[3];

void displayMenu(){
    cout<<"Welcome to the pizza restaurant!"<<endl;
    for(int x=0; x<4; x++){
        cout<<x<<"."<<m[x]<<endl;
    }
}

void createMenu(){
    m[0]="Plain Pizza";
    pizza[0][0]=100;
    pizza[0][1]=150;
    pizza[0][2]=200;
    m[1]="Cheese Pizza";
    pizza[1][0]=200;
    pizza[1][1]=250;
    pizza[1][2]=350;
    m[2]="Paneer Pizza";
    pizza[2][0]=250;
    pizza[2][1]=550;
    pizza[2][2]=450;
    m[3]="Mushroom Pizza";
    pizza[3][0]=250;
    pizza[3][1]=350;
    pizza[3][2]=450;

    ps[0]="Small";
    ps[1]="Medium";
    ps[2]="Large";
}

bool isEmpty(){
    return front==-1 && rear==-1;
}

bool isFull(){
    return (rear+1)%size==front;
}

void setOrder(Order q[], string pizzaName, string pizzaSize, int price, int count){
    if(isFull()){
        cout<<"Sorry, no more orders are accepted!"<<endl;
    }
    else{
        if(front==-1){
            front=0;
        }
        rear=(rear+1)%size;
        q[rear].name=pizzaName;
        q[rear].size=pizzaSize;
        q[rear].price=price*count;
        cout<<"Order placed successfully!"<<endl;
    }
}

void removeOrder(Order q[]){
    if(isEmpty()){
        return;
    }
    else{
        // removing the last element.
        if(front==rear){
            front=rear=-1;
        }
        else{
            front=(front+1)%size;
        }
    }
}


int main() {

    int res=1;

    // creating the menu.
    createMenu();

    // setting the size of the circular queue.
    cout << "Enter the maximum no.of orders: ";
    cin >> size;

    // creating the queue with size.
    Order q[size];

    while(res==1) {
        // if the queue is full then stop taking the orders.
        if (isFull()) {
           cout<<"No more orders to take!"<<endl;
           break;
        } else {
            try {

                // displaying the menu.
                displayMenu();

                // getting the user choice for the pizza.
                int p;
                cout << "Enter your choice (0 to 3): ";
                cin >> p;
                // handling the error if the user enters the invalid choice.
                if (p > 3) {
                    throw p;
                }
                // displaying the size and price of the pizza selected.
                for (int x = 0; x < 3; x++) {
                    cout << x << "." << "Size: " << ps[x] << "\tPrice: " << pizza[p][x] << endl;
                }

                // getting the price of the pizza w.r.t. chosen size.
                int ch;
                cout << "Enter your choice (0 to 2): ";
                cin >> ch;
                // handling the error if the user enters the invalid choice.
                if (ch > 2) {
                    throw ch;
                }

                // reading the quantity of the pizzas.
                int count;
                cout << "Enter the quantity: ";
                cin >> count;
                // handling the error if the user enters the invalid choice.
                if (count <= 0) {
                    throw count;
                }

                // placing the order.
                setOrder(q, m[p], ps[ch], pizza[p][ch], count);

                // printing the bill of the order.
                q[rear].printBill();

                // removing the orders if the order is delivered.
                char isDelivered;
                cout << "Did you received your order? (Yes - y, No - n): ";
                cin >> isDelivered;
                if((isDelivered!='y' || isDelivered!='Y' ) && (isDelivered!='n' || isDelivered=='N')){
                    throw -1;
                }
                // if the item is delivered, then updating the position of 'rear'.
                if (isDelivered == 'y' || isDelivered == 'Y') {
                    removeOrder(q);
                }
                else {
                    cout << "Sorry for inconvenience!\nSince, order cannot be canceled, wait for some time!" << endl;
                }
            }
            catch (int x) {
                cout << "Invalid Input!" << endl;
            }

            cout << "Do you want to place orders any more? (1. Yes, 2.No): ";
            cin >> res;

        }
    }

    return 0;
}
