
/*
    Problem statement:
        The ticket booking system of cinemax theater to be implemented
        using C++ program. There are 10 rows and 7 seats in each row.
        Doubly circular linked list has to maintain to keep track of seats
        and rows. Assume some random booking to start. Use array to store
        pointers to each row on demand.
        1. list of available seats is to be displayed.
        2. seats to be booked.
        3. booking can be cancelled.
 */

#include<iostream>
using namespace std;

// Node class for the doubly linked list.
class Node{
public:
    // E - empty, B - booked.
    char isBooked;
    Node *next;
    Node *prev;
    Node(char data){
        this->isBooked=data;
        this->next=NULL;
        this->prev=NULL;
    }
};

// doubly circular linked list class.
class DoublyCLL{
public:
    Node *head=NULL;
    Node *tail=NULL;
    DoublyCLL(){
        // for the first seat.
        head=tail=new Node('E');
        // for remaining 6 seats.
        // creating the row, initializing the values 'E' as initially all seats are vacant.
        for(int x=0; x<6; x++){
            Node *newNode=new Node('E');
            newNode->next=head;
            head->prev=newNode;
            head=newNode;
        }
        // finally making the doubly linked list circular.
        tail->next=head;
        head->prev=tail;
        tail=head;
    }
    void printList(){
        // as initially the position of head is at first node/seat of the row.
        for(int x=0; x<7; x++){
            cout<<head->isBooked<<" ";
            head=head->next;
        }
        cout<<endl;
    }

};

class Cinemax{
private:
    DoublyCLL *seats[10];
public:
    Cinemax(){
        // initializing the array.
        for(int x=0; x<10; x++){
            seats[x]=new DoublyCLL();
        }
    }
    void printSeats(){
        cout<<"The status of the seats is as follows:"<<endl;
        cout<<"*********************************************"<<endl;
        for(int x=0; x<10; x++){
            seats[x]->printList();
        }
        cout<<"*********************************************"<<endl;
    }
    void bookSeat(){
        printSeats();
        cout<<"Note - Row and column number starts from 0."<<endl;
        int r, c;
        cout<<"Enter the row number: ";
        cin>>r;
        cout<<"Enter the column number: ";
        cin>>c;
        Node *curr=seats[r]->head;
        for(int y=0; y<c; y++){
            curr=curr->next;
        }
        if(curr->isBooked=='B'){
            cout<<"The seat is already booked!"<<endl;
            return;
        }
        else {
            curr->isBooked = 'B';
            cout << "Booking is successful!" << endl;
            return;
        }
    }
    void cancelBooking(){
        printSeats();
        cout<<"Note - Row and column number starts from 0."<<endl;
        int r, c;
        cout<<"Enter the row number: ";
        cin>>r;
        cout<<"Enter the column number: ";
        cin>>c;
        Node *curr=seats[r]->head;
            for (int y = 0; y < c; y++) {
               curr=curr->next;
            }

        if(curr->isBooked=='E'){
            cout<<"The seat is already cancelled!"<<endl;
            return;
        }
        else {
            curr->isBooked = 'E';
            cout << "Seat booking is canceled successfully!" << endl;
            return;
        }
    }
};


int main(){

    Cinemax c;
    int ans=1;
    try {
        while (ans == 1) {
            cout << "What operation would you like to do?" << endl;
            cout << "1.Book a seat.\n2.Cancel booking.\n3.Print seat booking status." << endl;
            cout << "Your response(1, 2 or 3): ";
            int choice;
            cin >> choice;
            if (choice!=1 && choice!=2 && choice!=3){
                throw choice;
            }
            else {
                if (choice == 1) {
                    c.bookSeat();
                } else if(choice==2){
                    c.cancelBooking();
                }
                else{
                    c.printSeats();
                }
                cout << "Do you want to continue the service?(Yes-1, No-2)" << endl;
                cout << "Your response(1, 2): ";
                cin >> ans;
                if(ans!=1 && ans!=2){
                    throw ans;
                }
            }
        }
    }
    catch(int r){
        cout<<"Invalid input!"<<endl;
    }



    return 0;
}
